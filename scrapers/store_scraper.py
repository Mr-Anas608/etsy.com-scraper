
import sys, os

# Ensure the project's root directory is in the Python path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logs.custom_logging import setup_logging 
import logging
from utils.helpers import Helpers

import httpx
from parsel import Selector
import re
from typing import Optional, List, Tuple, Dict, Any
import asyncio
import json
from lxml import html
from dataclasses import dataclass
from seleniumbase import SB
import asyncio
import time


@dataclass
class EtsyStoreConfig:
    store_name = ""
    store_id = ""
    store_url = ""
    store_logo_url = ""
    store_sub_title = ""
    store_country = ""
    star_seller = ""  # boolean (True/False as string or convert later)
    store_reviews = ""
    store_review_score = ""
    store_sales = ""
    store_admirers = ""
    store_description = ""
    store_last_updated = ""
    on_etsy_since = ""
    welcome_to_our_shop_text = ""
    facebook_url = ""
    instagram_url = ""
    pinterest_url = ""
    tiktok_url = ""
    number_of_store_products = ""
    most_recent_product_urls = []  # list of strings
    ""

    # Helper function to return data in form of Dict
    def to_dict(self)-> Dict[str, Any]:
        return {
            "store_name": self.store_name,
            "store_id": self.store_id,
            "store_logo_url": self.store_logo_url,
            "store_description": self.store_description,
            "store_sub_title": self.store_sub_title,
            "store_country": self.store_country,
            "star_seller": self.star_seller,
            "store_review_score": self.store_review_score,
            "store_last_updated": self.store_last_updated,
            "store_reviews": self.store_reviews,
            "store_admirers": self.store_admirers,
            "store_sales": self.store_sales,
            "number_of_store_products": self.number_of_store_products,
            "on_etsy_since": self.on_etsy_since,
            "facebook_url": self.facebook_url,
            "instagram_url": self.instagram_url,
            "pinterest_url": self.pinterest_url,
            "tiktok_url": self.tiktok_url,
            "welcome_to_our_shop_text": self.welcome_to_our_shop_text,
            "store_url": self.store_url,
            "most_recent_product_urls": self.most_recent_product_urls,
        }
    
    # Helper function to filter & covert sales string into integer
    def string_to_int(self, sales_string:str = False, reviews_string:str = False) -> Optional[int]:
        try:
            if sales_string:
                # Find all numbers with optional k/decimals/commas using regex
                match = re.search(r'(\d+[,.]?\d*)\s?k?', sales_string, flags=re.IGNORECASE)
                if not match:
                    return None, "No match found!"
                
                number_str = match.group(1).replace(',', '').lower()
                
                # Handle decimal values (like 75.2k -> 75200)
                if '.' in number_str:
                    number = float(number_str)
                else:
                    number = int(number_str)
                
                # Multiply by 1000 if 'k' present anywhere in the text
                if 'k' in sales_string.lower():
                    return int(number * 1000) , False
                return int(number) , False
            elif reviews_string:
                # Extract the number of reviews
                match = re.search(r'\((\d+\.?\d*)(k?)\)', reviews_string)
                if not match:
                    return None, "No match found!"
                
                number_str = match.group(1)
                if '.' in number_str:
                    number = float(number_str)
                else:
                    number = int(number_str)

                if 'k' in reviews_string.lower():
                    return int(number * 1000), False
                
                return int(number), False
            else:
                return None, "Input was empty, returning None"
        except Exception as e:
            
            return None, e

class EtsyStoreScraper:
    def __init__(self, url: str = None, proxy: Optional[str] = False, timeout: int = 10):
        self.logger = setup_logging()
        self.url = url
        self.proxy = proxy
        self.timeout = timeout
        self.helpers = Helpers(url=url, proxy=proxy, timeout=timeout)


    async def parse_store_page(self, store_page_html: str) -> Optional[Dict[str, Any]]:
        try:
            self.logger.info("🌐 Parsing store page HTML content...")
            selector = Selector(text=store_page_html)
            store_data = EtsyStoreConfig()
            if selector:
                self.logger.debug(f"✅ Store page HTML content parsed successfully. selector len = {len(str(selector))} char.")
            else:
                self.logger.error(f"❌ Failed to parse store page HTML content. selector = {selector}")
                return None


            # Some Tags that have inside have may useful information about the store

            # Tag1: Json Script tag, for storing good quality logo url, and other fallback options if available
            store_info_script_tag = selector.xpath(".//script[@type='application/ld+json' and contains(text(), '\"@type\":\"OnlineStore\"')]/text()")

            # Tag2: Json Script tag, for storing 1st page product urls
            store_products_script_tag = selector.xpath(".//script[@type='application/ld+json' and contains(text(), '\"@type\":\"ItemList\"')]/text()")


            #Tag3: A store header container in html
            shop_header = (
                selector.css('div[class*="shop-home-header-container"]') 
                or selector.xpath('.//div[contains(@class,"trust-signals")]/div/div')
            )

            # Tag4: Section for description and last updated
            announcement_section = (
                selector.css('div[class*= "announcement-section"]')
                or selector.xpath('.//h2[contains(. ,"Announcement" )]/../..')
            )

            # Tag5 Section for social links, Welcome to our shop! & on_etsy_since etx, 
            shop_home_about_section = (
                selector.css('div[data-appears-component-name="shop_home_about_section"]')
                or selector.xpath('.//div[contains(@class, "anchor about-section")]')
            
            )

            # ------(: Start parsing the store data :)----------
            # Store Name Extraction
            try:

                store_data.store_name = ( 
                    store_info_script_tag.jmespath("name").get()
                    or shop_header.css('h1::text').get()
                    or shop_header.xpath('.//div[contains(@class,"shop-name-and-title-container")]//h1//text()').get()
                ).strip()
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing store_name: {e}")
            
            # Store Name is actually an ID in Etsy
            store_data.store_id = store_data.store_name
            
            # Let's made store url link from store ID, So we get Default page with default USD currency.
            store_data.store_url = f"https://www.etsy.com/shop/{store_data.store_id}" if store_data.store_id else self.url

            # Store Logo Url Extraction
            try:
              store_data.store_logo_url = (
                  store_info_script_tag.jmespath("logo").get()
                  or shop_header.css('img[class*="shop-icon-external"]::attr(src)').get()
                  or shop_header.xpath('.//div[contains(@class, "shop-avatar-container")]//img/@src').get()
              ).strip()
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing store_logo_url: {e}")
            
            # Store sub_title extraction
            try:
                store_data.store_sub_title = (
                    shop_header.css('h2::text').get()
                    or shop_header.xpath('.//div[contains(@class,"shop-name-and-title-container")]//h2//text()').get()
                ).strip()
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing store_sub_title: {e}")

            
            # Store country extraction
            try:
                store_data.store_country = (
                    store_info_script_tag.jmespath("location").get()
                    or shop_header.css('span[class*="shop-location"]::text').get()
                    or shop_header.xpath('.//div[contains(@class,"shop-info")]//span//text()').get()
                ).strip()
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing store_country: {e}")

            
            # Star seller detection
            try:
                store_data.star_seller = bool(
                    shop_header.css('.star-seller-badge').get()
                    or shop_header.xpath('.//*[contains(text(), "Star Seller")]').get()
                )
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing star_seller: {e}")


            # Store Reviews Count Extraction
            try:
                store_reviews = (
                    # 1st find on bottom reviews section
                    selector.xpath('string(.//div[contains(@class,"reviews-total")])').get() 
                    # Then check on header as a fallback
                    or shop_header.css('a[class*="reviews-link-shop-info"] span::text').get() 
                    or shop_header.xpath('.//a[contains(@href, "#reviews")]//span//text()').get()
                    or store_info_script_tag.jmespath('aggregateRating.reviewCount').get() # Have not Updated reviews, so keep it down
                )
                # Save only integer number
                clean_reviews_text = re.sub(r'\s+', '', store_reviews)
                review_count, e = store_data.string_to_int(reviews_string=clean_reviews_text)
                if e:
                    self.logger.warning(f"⚠️ Error while converting '{clean_reviews_text}' text to int in store_sales: {e}")
                store_data.store_reviews = review_count

            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing store_reviews: {e}")
            
                
            # Store review score extraction
            try:
                store_review_score = (
                    # 1st find on bottom reviews section
                    selector.xpath('.//div[contains(@class,"reviews-total")]//input[@name = "rating"]/@value').get() 
                    # Then check on header as a fallback
                    or shop_header.css('input[name="rating"]::attr(value)').get()
                )
                if store_review_score:
                    store_data.store_review_score = float(store_review_score)
        
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing store_review_score: {e}")


            # ---Store total Sales number extraction---
            try:
                sales_text = (
                    # First check on below the "Contact shop owner" Button
                    selector.xpath('.//div[contains(@class, "contact-shop-owner-button")]/following-sibling::div[1]/div[1]//text()').get()
                    # Then Use fallbacks on header if it fail
                    or shop_header.css('span:contains("Sales")::text').get()
                    or shop_header.xpath('.//span[contains(., "Sales")]//text()').get()
                )
                store_sales, e = store_data.string_to_int(sales_string=sales_text)
                if e:
                    self.logger.warning(f"⚠️ Error while converting '{sales_text}' text to int in store_sales: {e}")
                store_data.store_sales = store_sales
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing store_sales: {e}")

            # ---Store Admires Extraction---
            try:
                store_admires = (
                    # 1st find on bottom reviews section
                    selector.xpath('//div[contains(@class, "contact-shop-owner-button")]/following-sibling::div[1]/div[2]//text()').get()
                    # Then check on header as a fallback
                    or shop_header.css('a[class*="admires-link-shop-info"] span::text').get()
                    or shop_header.xpath('.//a[contains(@href, "#admires")]//span//text()').get()
                )
                # Save only integer number
                if store_admires and 'Admirers' in store_admires:
                    store_admires = store_admires.split('Admirers')[0]
                clean_admires_text = re.sub(r'\s+', '', store_admires)

                store_data.store_admirers = int(clean_admires_text)
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing store_admires: {e}")


        # ---Store Description Extraction---
            try:
                store_description = (
                    announcement_section.xpath('string(.//span[@data-inplace-editable-text="announcement"])').get()
                )
                store_data.store_description = re.sub(r'\s+', ' ', store_description).strip()
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing store_description: {e}")


            # ---Store Last Updated Extraction---
            try:
                store_data.store_last_updated = (
                    announcement_section.xpath('.//div[contains(@class, "shop-home-wider-sections")]//div[contains(. , "Last updated on")]/span/text()').get()
                    or announcement_section.css('span[class*="wt-no-wrap"]::text').get()
                ).strip()
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing store_last_updated: {e}")


            # ---Store Join data on Etsy--
            try:
                store_data.on_etsy_since = (
                    shop_home_about_section.xpath('.//div[contains(text(), "On Etsy since ")]/span//text()').get()
                ).strip()
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing on_etsy_since : {e}")


            #-- Store "Welcome to our shop!"" text
            try:
                welcome_to_our_shop_text = (
                    shop_home_about_section.xpath('string(.//span[@data-endpoint="AboutPost"])').get()
                )
                store_data.welcome_to_our_shop_text = re.sub(r'\s+', ' ', welcome_to_our_shop_text).strip()

            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing welcome_to_our_shop_text: {e}")
    
            
            #---Store Social links extraction---
            try:
                # Find facebook url
                facebook_url = (
                    shop_home_about_section.css('a[aria-label="Facebook"]::attr(href)').get()
                    or shop_home_about_section.xpath('.//a[contains(@href, "facebook")]/@href').get()
                )
                if facebook_url:
                    store_data.facebook_url = facebook_url

                # Find instagram url
                instagram_url = (
                    shop_home_about_section.css('a[aria-label="Instagram"]::attr(href)').get()
                    or shop_home_about_section.xpath('.//a[contains(@href, "instagram")]/@href').get()
                )
                if instagram_url:
                    store_data.instagram_url = instagram_url
                
                # Find ticktock url
                tiktok_url = (
                    shop_home_about_section.css('a[aria-label="TikTok"]::attr(href)').get()
                    or shop_home_about_section.xpath('.//a[contains(@href, "tiktok")]/@href').get()
                )
                if tiktok_url:
                    store_data.tiktok_url = tiktok_url

                # Find pinterest url
                pinterest_url = (
                    shop_home_about_section.css('a[aria-label="Pinterest"]::attr(href)').get()
                    or shop_home_about_section.xpath('.//a[contains(@href, "pinterest")]/@href').get()
                )
                if pinterest_url:
                    store_data.pinterest_url = pinterest_url
                
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing store_social_links: {e}")


            # --Store number of products
            try:
                number_of_store_products = (
                    selector.xpath('.//li[@aria-selected="true"]/span[contains(text(), "All")]/following-sibling::span//text()').get()
                    or selector.xpath('.//input[contains(@placeholder, "Search all")]/@placeholder').re(r'\d+')[0]
                )

                if number_of_store_products:
                    store_data.number_of_store_products = int(number_of_store_products)
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing number_of_store_products: {e}")

    
            # Store most_recent_product_urls
            try:
                store_recent_products_urls = (
                    store_products_script_tag.jmespath('itemListElement[*].url').getall()
                )
                if store_recent_products_urls:
                    store_data.most_recent_product_urls = store_recent_products_urls
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing store_recent_products_urls: {e}")


            return store_data.to_dict()
        except Exception as e:
            self.logger.error(f"❌ Error parsing store page: {e}")
            return None
    
    async def etsy_store_scraper(self) -> Dict[str, Any]:
        self.logger.info("🔎 Starting Etsy Store Scraper...")
        try:
            html_content, error_message = await self.helpers.fetch_page()
            if error_message:
                self.logger.error("⚠️ Skipping parsing due to fetch error. Error: " + error_message)
                return {
                    "search_url": self.url,
                    "error": error_message
                }
            
            result = await self.parse_store_page(html_content)
            if not result:
                self.logger.error("⚠️ No data found in the store page.")
                return {
                    "error": "No data found in the store page. Might be URL is wrong, Or Css selectors becomes over dated."
                }
            else:
                self.logger.info("✅ Store data successfully parsed.")
                return result


        except Exception as e:
            self.logger.error(f"❌ Critical error during Store scraping: {str(e)}")
            raise RuntimeError(f"Scraping failed: {str(e)}")
        
    
if __name__ == "__main__":
    # 🔧 Enable full debug logs during testing
    logger = setup_logging(console_level=logging.DEBUG)

    # 🧪 Test URL (can replace with any Etsy Store)
    url = "https://www.etsy.com/shop/EqualEats"

    logger.info("🔬 Starting standalone test for EtsyStoreScraper...")

    try:
        start_time = time.time()

        scraper = EtsyStoreScraper(url, proxy=None, timeout=10)
        result = asyncio.run(scraper.etsy_store_scraper())

        end_time = time.time()
        duration = end_time - start_time

        logger.info(f"⏱️ Scraping completed in {duration:.2f} seconds")
        
        print(result)
        # 💾 Save output
        output_file = "store.json"
        with open(output_file, "w", encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=4)

        logger.info(f"📁 Data saved to {output_file}")

    except Exception as e:
        logger.error(f"❌ Test run failed: {str(e)}", exc_info=True)
