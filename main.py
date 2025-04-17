from flask import Flask, request, jsonify
import asyncio
from scrapers.category_scraper import EtsyCategoryScraper

app = Flask(__name__)

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

        # Create instance of the scraper
        scraper = EtsyCategoryScraper(url=url, proxy=proxy, timeout=timeout)

        # Run async scraping task in Flask (via asyncio loop)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(scraper.etsy_category_scraper())

        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run()
