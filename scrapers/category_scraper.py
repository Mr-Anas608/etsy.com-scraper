import sys, os

# Ensure the project's root directory is in the Python path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logs.custom_logging import setup_logging 
import logging
from utils.helpers import Helpers

from parsel import Selector
import re
from typing import Optional, List, Tuple, Dict, Any
import asyncio
import json
from lxml import html
from dataclasses import dataclass


@dataclass
class EtsyCategoryConfig:
    category_tree = ""
    category_name = ""
    products = []
    search_url = ""

    # Helper function to return data in form of Dict
    def to_dict(self) -> Dict[str, Any]:
        return {
            "category_tree": self.category_tree,
            "category_name": self.category_name,
            "products": self.products,
            "search_url": self.search_url
        }

@dataclass
class EtsyProductCardConfig:
    product_id = ""
    product_name = ""
    product_url = ""
    store_review_score = ""
    store_reviews_number = ""
    star_seller = ""
    store_name = ""
    store_url = ""
    is_ad = ""

    # Helper function to return data in form of Dict
    def to_dict(self) -> Dict[str, Any]:
        return {
            "product_name": self.product_name,
            "product_url": self.product_url,
            "product_id": self.product_id,
            "store_review_score": self.store_review_score,
            "store_reviews_number": self.store_reviews_number,
            "star_seller": self.star_seller,
            "store_name": self.store_name,
            "store_url": self.store_url,
            "is_ad": self.is_ad
        }



class EtsyCategoryScraper:
    def __init__(self, url: str = None, proxy: Optional[str] = None, timeout: int = 5):
        self.logger = setup_logging(console_level=logging.DEBUG)
        self.url = url
        self.proxy = proxy
        self.timeout = timeout
        self.store_data = EtsyCategoryConfig()
        self.helpers = Helpers(url=url, proxy=proxy, timeout=timeout)

        self.logger.info(f"🔎 Initialized scraper with URL: {url}")


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

    async def parse_product_card(self, card_selector: Selector) -> Optional[Dict[str, Any]]:
        try:

            store_card_info = EtsyProductCardConfig()

            #--Product ID Extraction--
            try:
                store_card_info.product_id = (
                    card_selector.css('a[class*="listing-link"]::attr("data-listing-id")').get() 
                    or card_selector.xpath('.//div[contains(@class, "js-merch-stash-check-listing v2-listing-card")]/@data-palette-listing-id').get()
                ).strip()
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing product_id: {e}")


           # --Product Name Extraction--
            try:
                store_card_info.product_name = (
                    card_selector.css('h3::text').get()
                    or card_selector.xpath('.//h3[contains(@class, "v2-listing-card__title")]/text()').get()
                ).strip()
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing product_name: {e}")


            # --Product URL Extraction--
            try:
                store_card_info.product_url = (
                    card_selector.css('a[class*="listing-link"]::attr("href")').get()
                    or card_selector.xpath(f'.//a[contains(@data-listing-id, "{store_card_info.product_id}")]').get()
                ).split('?')[0].strip()
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing product_url: {e}")

            # --Store Review Score Extraction--
            try:
                store_review_score = (
                    card_selector.css('input[name="rating"]::attr("value")').get()
                    or card_selector.xpath('.//input[@name="initial-rating"]/@value').get()
                )
                store_card_info.store_review_score = float(store_review_score) if store_review_score else None
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing store_review_score: {e}")<e
            

            # --Store Reviews Number Extraction--
            try:
                store_reviews_number = (
                    card_selector.xpath('.//span[contains(@class, "wt-text-gray wt-display-inline-block")]').re(r'\(([\d, ]+)\)')
                )
                if store_reviews_number:
                    clean_number = store_reviews_number[0].replace(',', '').strip()
                    store_card_info.store_reviews_number = int(clean_number) if clean_number else None
                
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing store_reviews_number: {e}")
          

            # --Store Name Extraction--
            try:
                text = (
                    card_selector.xpath('.//div[contains(@class, "v2-listing-card__info")]/p//span[contains(text(), "From shop")]//text()').get()
                )
                if text:
                    store_card_info.store_name = text.split('From shop')[1].strip()
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing store_name: {e}")
            print("Store Name: ",text)
            

            # --Is Ad Detection--
            try:
                store_card_info.is_ad = bool(
                    card_selector.xpath('.//div[contains(@class, "v2-listing-card__info")]/p//span[contains(@class, "wt-screen-reader-only") and not(@aria-hidden="true") and contains(text(), "Ad")]//text()').get()
                )
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing is_ad: {e}")

    
            store_card_info.store_url = f"https://www.etsy.com/shop/{store_card_info.store_name}" if store_card_info.store_name else None
            store_card_info.star_seller = "Star Seller" in str(card_selector)

            # self.logger.debug(f"🛍️ Parsed Product: {product_name} (ID: {product_id})")

            return store_card_info.to_dict()

        except Exception as e:
            self.logger.debug(f"❌ Failed to parse product card: {e}")
            return None

    async def etsy_category_scraper(self, html_content:str = False) -> dict:
        self.logger.info("🚀 Starting Etsy category scrape...")
        try:
            if not html_content:
                html_content, error_message = await self.helpers.fetch_page()
                if error_message:
                    self.logger.error("⚠️ Skipping parsing due to fetch error. Error: " + error_message)
                    return {
                        "category_tree": None,
                        "category_name": None,
                        "products": [],
                        "search_url": self.url,
                        "error": error_message
                    }
                
            selector = Selector(text=html_content)

            # Deal these 2 values separate to extract information from URLs
            self.store_data.category_tree, self.store_data.category_name = await self.extract_category_tree_from_url(self.url)

            product_cards = (
                selector.xpath('.//div[@data-search-results]//ul//li')
                or selector.css('div[data-page-type="category"]')
            )

            self.logger.info(f"🧩 Found {len(product_cards)} product cards")

            parse_tasks = [self.parse_product_card(card) for card in product_cards]
            parsed_products = await asyncio.gather(*parse_tasks)
            self.store_data.products = [p for p in parsed_products if p]

            self.logger.info(f"✅ Parsed {len(self.store_data.products)} valid products.")

            return self.store_data.to_dict()

        except Exception as e:
            self.logger.error(f"❌ Critical error during category scraping: {str(e)}")
            raise RuntimeError(f"Scraping failed: {str(e)}")


if __name__ == "__main__":
    import time

    # 🔧 Enable full debug logs during testing
    logger = setup_logging(console_level=logging.DEBUG)

    # 🧪 Test URL (can replace with any Etsy category)
    url = "https://www.etsy.com/c/jewelry?explicit=1&instant_download=true&ship_to=GB&order=highest_reviews&page=2"

    logger.info("🔬 Starting standalone test for EtsyCategoryScraper...")

    try:
        start_time = time.time()

        # scraper = EtsyCategoryScraper(url, proxy=None, timeout=10)
        scraper = EtsyCategoryScraper(url=url)

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
