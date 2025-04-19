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
from dataclasses import dataclass
from seleniumbase import SB
import asyncio
@dataclass
class EtsyCategoryKeys:
    category_tree = ""
    sale_price_usd = ""
    star_seller = ""
    price_usd = ""
    product_title = ""
    number_in_basket = ""
    category_name = ""
    category_url = ""
    product_reviews = ""
    ratingValue = ""
    store_reviews = ""
    date_of_latest_review = ""
    store_name = ""
    store_url = ""
    brand = ""
    more_from_this_shop_names = ""
    more_from_this_shop_urls = ""
    similar_products_names = ""
    similar_products_urls = ""
    digital_download = ""
    image = ""
    related_searches = ""
    date_listed = ""
    number_of_favourties = ""
    main_image = ""
    last_24_hours = ""
    product_url = ""
    product_id = ""

@dataclass
class ListingPageCart:
    sale_price_usd = ""
    star_seller = ""
    price_usd = ""
    product_title = ""
    number_in_basket = ""
    store_name = ""
    store_url = ""
    brand = ""
   

    def get_listing_page_cart(self) -> Optional[str]:
        try:
            self.logger.info("🌐 Extracting listing page cart...")
            script_tag = self.soup.find('script', text=re.compile(r'window\.__INITIAL_STATE__'))
            if script_tag:
                json_text = re.search(r'window\.__INITIAL_STATE__\s*=\s*(.*?);', script_tag.string).group(1)
                return json.loads(json_text)
            else:
                self.logger.error("❌ No script tag found with the expected pattern.")
                return None
        except Exception as e:
            self.logger.error(f"❌ Error extracting listing page cart: {e}")
            return None


class EtsyProductScraper:
    def __init__(self):
        self.logger = setup_logging(console_level=logging.DEBUG)
        # self.Keys = EtsyProductKeys()

    async def fetch_listing_page_cart(listing_page_cart_html):
        pass

    async def sb_test(self) -> str:
        with SB(browser="chrome",
        headless=True,
        headless2=True,  # New headless mode
        uc=True,
        chromium_arg="--no-sandbox --disable-dev-shm-usage --disable-gpu",
        binary_location="/usr/bin/google-chrome",
        page_load_strategy="eager",
        ) as sb:
            sb.open("https://www.etsy.com/uk/listing/1583875617/family-and-couple-annual-budget-google?ref=landingpage_similar_listing_bot-1&pro=1&sts=1&listing_id=1583875617&listing_slug=family-and-couple-annual-budget-google&logging_key=cac5e902bc9a84971f59bffc3fd67c092b91d3ce%3A1583875617")
            sb.sleep(2)
            page_source = sb.get_page_source()

        return page_source

        
if __name__ == "__main__":
    scraper = EtsyProductScraper()
    print(asyncio.run(scraper.cr_test()))