# main.py
from flask import Flask, request, jsonify
import asyncio
import concurrent.futures
import os
from functools import partial
from scrapers.category_scraper import EtsyCategoryScraper, batch_scrape
import multiprocessing as mp
import logging
import json
from queue import Queue
import threading
# import uvicorn
from contextlib import asynccontextmanager

# Set up global thread pool for handling requests
# Calculate optimal number of workers based on CPU cores
CPU_COUNT = os.cpu_count() or 4
MAX_WORKERS = CPU_COUNT * 5  # Multiplier can be adjusted

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create request queue for processing
request_queue = Queue()

# Create Flask app
app = Flask(__name__)

# Thread pool executor for CPU-bound tasks
thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS)

# Process pool for true parallel processing
process_pool = concurrent.futures.ProcessPoolExecutor(max_workers=CPU_COUNT)

# Create our own event loop for threading compatibility
event_loop = asyncio.new_event_loop()

async def process_scrape_request(url, proxy=None, timeout=10):
    """Process a single scrape request asynchronously"""
    scraper = EtsyCategoryScraper(
        url=url, 
        proxy=proxy, 
        timeout=timeout, 
        max_concurrency=50,  # Control concurrent connections per request
        connection_limit=100  # Total connection pool size
    )
    return await scraper.etsy_category_scraper()

def run_async_task(url, proxy, timeout):
    """Run an async task in the event loop, for use in thread pool"""
    return event_loop.run_until_complete(
        process_scrape_request(url, proxy, timeout)
    )

# Background worker thread function
def request_processor():
    """Process requests from the queue"""
    while True:
        try:
            # Get job from queue
            job = request_queue.get()
            if job is None:  # Shutdown signal
                break
                
            # Unpack job data
            url, proxy, timeout, callback = job
            
            # Submit to thread pool
            future = thread_pool.submit(run_async_task, url, proxy, timeout)
            result = future.result()
            
            # Call callback with result
            if callback:
                callback(result)
                
        except Exception as e:
            logger.error(f"Error processing request: {e}")
        finally:
            request_queue.task_done()

# Start worker threads
NUM_WORKER_THREADS = MAX_WORKERS 
worker_threads = []

for _ in range(NUM_WORKER_THREADS):
    worker = threading.Thread(target=request_processor, daemon=True)
    worker.start()
    worker_threads.append(worker)

@app.route('/category', methods=['POST'])
def handle_category():
    try:
        # Get input JSON
        data = request.get_json()
        url = data.get('url')
        proxy = data.get('proxy', None)
        timeout = data.get('timeout', 10)
        
        # Validate input
        if not url:
            return jsonify({"error": "Missing 'url' field"}), 400
        
        # Direct processing for individual requests (not going through queue)
        result = run_async_task(url, proxy, timeout)
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

@app.route('/batch', methods=['POST']) 
def handle_batch():
    """Process multiple URLs in a single request"""
    try:
        # Get input JSON
        data = request.get_json()
        urls = data.get('urls', [])
        proxy = data.get('proxy', None)
        timeout = data.get('timeout', 10)
        
        # Validate input
        if not urls or not isinstance(urls, list):
            return jsonify({"error": "Missing or invalid 'urls' field"}), 400
            
        # Use the event loop to run the batch
        results = event_loop.run_until_complete(
            batch_scrape(urls, proxy, timeout)
        )
        
        return jsonify({"results": results}), 200
    
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

# Implement a route that returns current server stats
@app.route('/stats', methods=['GET'])
def get_stats():
    return jsonify({
        "queue_size": request_queue.qsize(),
        "workers": NUM_WORKER_THREADS,
        "thread_pool_size": MAX_WORKERS,
        "cpu_count": CPU_COUNT
    })

@app.route('/test_async')
async def test_async():
    await asyncio.sleep(5)  # Simulate a 5-second I/O operation
    return jsonify({"message": "Async test complete"}), 200

if __name__ == '__main__':
    # Use a production-grade WSGI server instead of Flask's built-in server
    # For testing, you can still use Flask:
    app.run(threaded=True, host='0.0.0.0', port=5000)
    
    # Clean shutdown
    for _ in range(NUM_WORKER_THREADS):
        request_queue.put(None)  # Signal workers to shut down
    
    for worker in worker_threads:
        worker.join()
        
    thread_pool.shutdown()
    process_pool.shutdown()