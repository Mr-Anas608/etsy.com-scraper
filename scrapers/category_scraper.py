import sys, os

# Ensure the project's root directory is in the Python path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logs.custom_logging import setup_logging 
import logging

import httpx
from bs4 import BeautifulSoup
import re
from typing import Optional, List, Tuple, Dict, Any
import asyncio
import json
from lxml import html


class EtsyCategoryScraper:
    def __init__(self, url: str, proxy: Optional[str] = None, timeout: int = 5):
        self.logger = setup_logging(console_level=logging.DEBUG)
        self.url = url
        self.proxy = proxy
        self.timeout = timeout
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }

        self.logger.info(f"🔎 Initialized scraper with URL: {url}")

    async def fetch_page(self) -> Optional[str]:
        try:
            self.logger.info("🌐 Fetching HTML content from Etsy category page...")
            async with httpx.AsyncClient(headers=self.headers, timeout=self.timeout, follow_redirects=True) as client:
                response = await client.get(self.url)
                response.raise_for_status()
                self.logger.info(f"✅ Page fetched successfully with status: {response.status_code}")
                return response.text, None
        except httpx.RequestError as exc:
            error_message = f"❌ Network error at {exc.request.url}: {exc}"
            self.logger.error(error_message)
            return None, error_message
        except httpx.HTTPStatusError as exc:
            error_message = f"❌ HTTP error {exc.response.status_code} at {exc.request.url}"
            self.logger.error(error_message)
            return None, error_message
        except Exception as exc:
            error_message = f"❌ Unexpected error during fetch: {exc}"
            self.logger.error(error_message)
            return None, error_message

    async def extract_category_tree_from_url(self, url: str) -> Tuple[Optional[str], Optional[str]]:
        try:
            if "/c/" not in url:
                return None, None
            path_part = url.split("/c/", 1)[1]
            path = path_part.split("?", 1)[0]
            parts = [p for p in path.strip("/").split("/") if p]
            if not parts:
                return None, None
            formatted_parts = [p.replace("-", " ").title() for p in parts]
            category_tree = "Homepage > " + " > ".join(formatted_parts)
            category_name = formatted_parts[-1]
            self.logger.debug(f"🧭 Extracted Category Tree: {category_tree}")
            return category_tree, category_name
        except Exception as e:
            error_message = f"❌ Failed to parse category from URL: {e}"
            self.logger.error(error_message)
            return None, None

    async def parse_product_card(self, card: BeautifulSoup) -> Optional[Dict[str, Any]]:
        try:
            tree = html.fromstring(str(card))

            product_id = card.get('data-listing-id') or (
                tree.xpath(".//a[@data-listing-id]/@data-listing-id")[0].strip()
                if tree.xpath(".//a[@data-listing-id]/@data-listing-id") else None
            )
            if not product_id:
                self.logger.debug("⛔ Skipping card: No product ID found.")
                return None

            title_tag = card.select_one("h3.v2-listing-card__title")
            product_name = title_tag.get_text(strip=True) if title_tag else (
                tree.xpath("//h3/text()")[0].strip()
                if tree.xpath("//h3/text()") else None
            )

            link_tag = card.select_one("a.listing-link")
            product_url = link_tag["href"] if link_tag else (
                tree.xpath(".//a[@data-listing-id]/@href")[0].strip()
                if tree.xpath(".//a[@data-listing-id]/@href") else None
            )

            rating_input = card.select_one("input[name='rating']")
            store_review_score = float(rating_input.get('value')) if rating_input and rating_input.get('value') else None

            store_reviews_number = None
            review_count_tag = card.select_one("span.wt-text-gray.wt-display-inline-block")
            if review_count_tag:
                match = re.search(r'\(([\d,]+)\)', review_count_tag.get_text(strip=True))
                if match:
                    store_reviews_number = int(match.group(1).replace(',', ''))

            store_name = None
            is_ad = False
            seller_info_p = card.select_one("p.wt-text-caption.wt-mb-xs-1")
            if seller_info_p:
                words = re.split(r'\s+', seller_info_p.get_text(strip=True))
                if "ad" in words and "by" in words:
                    is_ad = True
                    try:
                        store_name = words[words.index("by") + 1]
                    except Exception:
                        pass
                elif words:
                    store_name = words[-1]

            store_url = f"https://www.etsy.com/uk/shop/{store_name}" if store_name else None
            star_seller = "Star Seller" in str(card)

            self.logger.debug(f"🛍️ Parsed Product: {product_name} (ID: {product_id})")

            return {
                "product_name": product_name,
                "product_url": product_url,
                "product_id": product_id,
                "store_review_score": store_review_score,
                "store_reviews_number": store_reviews_number,
                "star_seller": star_seller,
                "store_name": store_name,
                "store_url": store_url,
                "is_ad": is_ad
            }

        except Exception as e:
            self.logger.debug(f"❌ Failed to parse product card: {e}")
            return None

    async def etsy_category_scraper(self) -> dict:
        self.logger.info("🚀 Starting Etsy category scrape...")
        try:
            html_content, error_message = await self.fetch_page()
            if error_message:
                self.logger.error("⚠️ Skipping parsing due to fetch error. Error: " + error_message)
                return {
                    "category_tree": None,
                    "category_name": None,
                    "products": [],
                    "search_url": self.url,
                    "error": error_message
                }

            soup = BeautifulSoup(html_content, "html.parser")
            category_tree, category_name = await self.extract_category_tree_from_url(self.url)

            product_cards = soup.select("div.v2-listing-card")
            self.logger.info(f"🧩 Found {len(product_cards)} product cards")

            parse_tasks = [self.parse_product_card(card) for card in product_cards]
            parsed_products = await asyncio.gather(*parse_tasks)
            products = [p for p in parsed_products if p]

            self.logger.info(f"✅ Parsed {len(products)} valid products.")

            return {
                "category_tree": category_tree,
                "category_name": category_name,
                "products": products,
                "search_url": self.url
            }

        except Exception as e:
            self.logger.error(f"❌ Critical error during category scraping: {str(e)}")
            raise RuntimeError(f"Scraping failed: {str(e)}")


if __name__ == "__main__":
    import time

    # 🔧 Enable full debug logs during testing
    logger = setup_logging(console_level=logging.DEBUG)

    # 🧪 Test URL (can replace with any Etsy category)
    url = "https://www.etsy.com/uk/c/jewelry?explicit=1&instant_download=true&ship_to=GB&order=highest_reviews&page=8"

    logger.info("🔬 Starting standalone test for EtsyCategoryScraper...")

    try:
        start_time = time.time()

        scraper = EtsyCategoryScraper(url, proxy=None, timeout=10)
        result = asyncio.run(scraper.etsy_category_scraper())

        end_time = time.time()
        duration = end_time - start_time

        logger.info(f"⏱️ Scraping completed in {duration:.2f} seconds")
        
        # 💾 Save output
        output_file = "category.json"
        with open(output_file, "w", encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=4)

        logger.info(f"📁 Data saved to {output_file}")

    except Exception as e:
        logger.error(f"❌ Test run failed: {str(e)}", exc_info=True)
