import asyncio
from fake_useragent import UserAgent
import httpx
import sys
import os
import random
import time
import aiohttp
from typing import List, Dict, Any, Optional

# Ensure the project's root directory is in the Python path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logs.custom_logging import setup_logging 
import logging
import json

logger = setup_logging(console_level=logging.DEBUG)

# Corrected proxies (fix the typo and format for httpx)
proxies = {
    'http://': 'http://germanproxy42de:tyF8SSTx27jg@168.119.244.147:13864',
    'https://': 'http://germanproxy42de:tyF8SSTx27jg@168.119.244.147:13864',
}
# proxy_url = "http://germanproxy42de:tyF8SSTx27jg@168.119.244.147:13864"

# ✅ Using Main Gateway:
proxy_url = "http://5.79.73.131:13010"

# # ✅ Using 3 Minutes Gateway (first one):
# proxy_url = "http://173.208.150.242:15001"

# # ✅ Using 15 Minutes Gateway (second one):
proxy_url = "http://163.172.58.253:16001"

# # ✅ Using Residential Proxy:
# proxy_url = "http://204.12.211.114:17088"


async def check_proxy(session: aiohttp.ClientSession = None) -> Optional[str]:
    """Check if the proxy is working"""
    try:
        if session:
            async with session.get('http://www.httpbin.org/ip', proxy=proxy_url) as response:
                if response.status == 200:
                    output = json.loads(await response.text())
                    proxy = output.get("origin")
                    logger.debug(f"{proxy} Proxy is working")
                    return proxy_url, proxy
                else:
                    logger.error(f"Proxy is not working, Status Code: {response.status}")
                    return None, None
        else:
            async with aiohttp.ClientSession() as session:
                logger.warning("Creating new session for proxy check")
                async with session.get('http://www.httpbin.org/ip', proxy=proxy_url) as response:
                    if response.status == 200:
                        output = json.loads(await response.text())
                        proxy = output.get("origin")
                        logger.debug(f"{proxy} Proxy is working")
                        return proxy_url, proxy
                    else:
                        logger.error(f"Proxy is not working, Status Code: {response.status}")
                        return None, None
                    
    except Exception as e:
        logger.error(f"Error checking proxy: {e}")
        return None, None
    

async def fetch_page(session: aiohttp.ClientSession, page: int, headers: dict, proxy:str = None) -> Optional[str]:
    """Make a request with staggered delay"""

    params = {'ref': 'pagination', 'page': str(page)}
    url = f"https://www.etsy.com/c/jewelry?explicit=1&instant_download=true&ship_to=GB&order=highest_reviews&page={page}"

    try:
        start_time = time.perf_counter()
        if proxy:
            response = await session.get(url, headers=headers, params=params, proxy=proxy)
        else:
            response = await session.get(url, headers=headers, params=params)
            
        end_time = time.perf_counter()
        duration = end_time - start_time
        logger.info(f"Page {page} - Status: {response.status}, Length: {len(await response.text())}, - Time taken: {duration:.4f} seconds")

        html_content = await response.text() # await here
        if len(html_content) < 2000:
            logger.info(f"Short response for page {page} - possible block")
            with open(f"utils/debug/Page_{page}_Error.html", "w", encoding="utf-8") as f:
                f.write(html_content)
        else:
            with open(f"utils/debug/Page_{page}_Success.html", "w", encoding="utf-8") as f:
                f.write(html_content)
        return html_content
    except aiohttp.ClientError as e:
        logger.error(f"Error on page {page}: {str(e)}")
        return None
    except asyncio.TimeoutError:
        logger.error(f"Timeout error on page {page}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error on page {page}: {e}")
        return None

async def main():
    """Main async function to run requests with staggered delays"""
    start_overall = time.perf_counter()
    base_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    }
    
    async with aiohttp.ClientSession() as session:
    
        tasks = []
        for i in range(50):
            proxy_url, proxy = await check_proxy(session)
            if proxy_url:
                logger.debug(f"Using proxy: {proxy} from this url {proxy_url}")
                task = asyncio.create_task(fetch_page(session, i + 1, headers=base_headers, proxy=proxy_url))
            else:
                logger.warning("No proxy available, using default headers")

                task = asyncio.create_task(fetch_page(session, i + 1, headers=base_headers))

            tasks.append(task)

            if i < 99:
                delay = random.uniform(1, 3)
                await asyncio.sleep(delay)

        await asyncio.gather(*tasks)
        end_overall = time.perf_counter()
        duration_overall = end_overall - start_overall
        logger.info(f"Total time taken: {duration_overall:.4f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
