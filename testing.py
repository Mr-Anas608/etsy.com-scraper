import asyncio
import aiohttp
import time
import json
from collections import defaultdict
from tqdm import tqdm
from aiohttp import TCPConnector

# 📡 Your FastAPI deployed endpoint
API_URL = "https://etsy-com-scraper.onrender.com/category"

# 🌐 Etsy URLs to test
URLS = [
    f"https://www.etsy.com/uk/c/jewelry?explicit=1&instant_download=true&ship_to=GB&order=highest_reviews&page={i}"
    for i in range(1, 50)  # Adjust number of pages as needed
]

REQUESTS_PER_SECOND = 10
CLIENT_TIMEOUT = 30
DURATION_SECONDS = len(URLS) // REQUESTS_PER_SECOND  # Total seconds of load

results = []

# 🔁 One concurrent POST request
async def send_request(session, request_id, url, batch_id):
    start = time.time()
    try:
        payload = {"url": url}
        async with session.post(API_URL, json=payload, timeout=CLIENT_TIMEOUT) as response:
            text = await response.text()
            duration = round(time.time() - start, 3)

            results.append({
                "id": request_id,
                "url": url,
                "status": response.status,
                "duration": duration,
                "batch": batch_id,
                "response": text[:80]
            })
            return response.status
    except Exception as e:
        duration = round(time.time() - start, 3)
        results.append({
            "id": request_id,
            "url": url,
            "status": "error",
            "duration": duration,
            "batch": batch_id,
            "error": str(e)
        })
        return None

# 🧪 Fire all requests in batches
async def fire_all_requests():
    all_tasks = []
    request_id = 1
    url_index = 0

    connector = TCPConnector(limit=0, ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        with tqdm(total=len(URLS)) as pbar:
            for second in range(DURATION_SECONDS):
                batch_start = time.time()
                print(f"\n🔁 Sending batch at second {second} (Total so far: {request_id - 1})")

                for _ in range(REQUESTS_PER_SECOND):
                    if url_index >= len(URLS):
                        break
                    task = asyncio.create_task(
                        send_request(session, request_id, URLS[url_index], batch_id=second)
                    )
                    all_tasks.append(task)
                    request_id += 1
                    url_index += 1
                    pbar.update(1)

                elapsed = time.time() - batch_start
                await asyncio.sleep(max(0, 1 - elapsed))

        print(f"\n🚀 All {request_id - 1} requests fired. Now waiting for responses...\n")
        await asyncio.gather(*all_tasks)

async def main():
    total_start = time.time()
    await fire_all_requests()
    total_end = time.time()

    # 🧾 Group results by batch
    batches = defaultdict(list)
    for r in results:
        batches[r["batch"]].append(r)

    for sec in sorted(batches):
        print(f"\n📦 Batch from second {sec} ➜")
        for r in batches[sec][:5]:  # Show first 5 of each batch
            print(f"  ID {r['id']} | Status: {r['status']} | {r['duration']}s")

    # ✅ Final Summary
    total_success = sum(1 for r in results if r["status"] == 200)
    total_failed = len(results) - total_success
    durations = [r["duration"] for r in results]

    print("\n🧾 Final Summary")
    print("-------------------------")
    print(f"✅ Success: {total_success}")
    print(f"❌ Failed : {total_failed}")
    print(f"⏱ Total time: {round(total_end - total_start, 2)}s")
    print(f"🐢 Slowest: {max(durations):.2f}s")
    print(f"⚡ Fastest: {min(durations):.2f}s")
    print(f"📊 Avg Time: {sum(durations)/len(durations):.2f}s")

    # 💾 Save full logs
    with open("load_test.log", "w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    print(f"\n🌐 Starting load test for {len(URLS)} URLs")
    asyncio.run(main())
