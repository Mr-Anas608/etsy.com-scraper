import sys, os

# Ensure the project's root directory is in the Python path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logs.custom_logging import setup_logging
import logging
from utils.helpers import Helpers

import re, time
from typing import Optional, List, Tuple, Dict, Any
import json
from dataclasses import dataclass
import asyncio
from parsel import Selector 


@dataclass
class EtsyProductConfig:
    product_id = ""
    product_title = ""
    product_url = ""
    main_image = ""
    price_usd = ""
    sale_price_usd = ""
    star_seller = ""
    number_in_basket = ""
    store_name = ""
    store_url = ""
    brand = ""
    store_reviews = ""
    rating_value = ""
    product_reviews = ""
    date_of_latest_review = ""
    digital_download = ""
    date_listed = ""
    number_of_favourties = ""
    category_tree = ""
    category_name = ""
    category_url = ""
    related_searches = ""


    # Helper function to return data in form of Dict
    def to_dict(self)-> Dict[str, Any]:
        return{
            "category_tree": self.category_tree,
            "sale_price_usd": self.sale_price_usd,
            "star_seller": self.star_seller,
            "price_usd": self.price_usd,
            "product_title": self.product_title,
            "number_in_basket": self.number_in_basket,
            "category_name": self.category_name,
            "category_url": self.category_url,
            "product_reviews": self.product_reviews,
            "ratingValue": self.rating_value,
            "store_reviews": self.store_reviews,
            "date_of_latest_review": self.date_of_latest_review,
            "store_name": self.store_name,
            "store_url": self.store_url,
            "brand": self.brand,
            "digital_download": self.digital_download,
            "date_listed": self.date_listed,
            "number_of_favourties": self.number_of_favourties,
            "main_image": self.main_image,
            "product_url": self.product_url,
            "product_id": self.product_id,
            "related_searches": self.related_searches
        
        }
    

class EtsyProductScraper:
    def __init__(self, url: str = None, proxy: Optional[str] = False, timeout: int = 10):
        self.logger = setup_logging(console_level=logging.DEBUG)
        self.url = url
        self.helpers = Helpers(url=url, proxy=proxy, timeout=timeout)
        self.proxy = proxy
        self.timeout = timeout
    
    async def parse_product_page(self, store_page_html: str) -> Optional[Dict[str, Any]]:
        try:
            self.logger.info("🌐 Parsing store page HTML content...")
            selector = Selector(text=store_page_html)
            store_data = EtsyProductConfig()

            if selector:
                self.logger.debug(f"✅ Store page HTML content parsed successfully. selector len = {len(str(selector))} char.")
            else:
                self.logger.error(f"❌ Failed to parse store page HTML content. selector = {selector}")
                return None
            
            # Some Tags container that have inside may useful information

            # Tag1: Json Script tag, for storing good quality main image url, id and other fallback options if available
            product_info_script_tag = selector.xpath(".//script[@type='application/ld+json' and contains(text(), '\"@type\":\"Product\"')]/text()")


            #Tag: Photo container have, image url, best seller & ID fallback if needed
            photo_container = (
                selector.css('#photos')
                or selector.xpath('.//div[contains(@id, "listing-page-cart")]')
            )

            # Tag: Side Cart container have information about the product & Seller like title, price, review count ...etx
            listing_page_cart = (
                selector.css('div#listing-page-cart')
            )

            # Tag: Product container have information about the product details like digital download, description ...etx
            product_details = (
                selector.css('div#product_details')
                or selector.xpath('.//h3[contains(text(), "Highlights" )]/ancestor::div[contains(@class, "appears-ready")]')
            )

            # Tag: Reviews container have all reviews related information like, product reviews, store reviews. latest reviews... etx
            data_reviews_container = (
                selector.css('div#reviews')
                or selector.css('div[data-appears-component-name="listing_page_reviews"]')
            )


            # Tag: Tags Container have all search terms inside.
            tags_section_container = (
                selector.css('div[data-appears-component-name="Listzilla_ApiSpecs_Tags_InternalLanding"]')
                or selector.xpath('.//*[contains(text() , "Explore related searches")]/ancestor::div[contains(@class, "recs-appears-logger")]')
            
            )


            # Tag: Category Container have all category tree inside.
            category_tree_container = (
                selector.xpath('.//div[contains(@data-ui, "listing-breadcrumbs")]//ul')
                or selector.xpath('.//div[contains(@data-selector,"listing-page-content")]//a[contains(text(), "Homepage")]/..')
            )
            
            # ------(: Start parsing the product page data :)----------

            # -- Product ID Extraction --
            try:
                store_data.product_id = (
                    product_info_script_tag.jmespath("sku").get() # ID in "sku" key
                    or selector.xpath('.//input[contains(@name, "listing_id")]/@value').get()
                    or photo_container.xpath('.//button[contains(@data-favorite-label, "Add to Favourites") and @data-listing-id]/@data-listing-id').get()
                ).strip()
            
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing product_id: {e}")


            # -- Product Title Extraction --
            try:
                store_data.product_title = (
                    product_info_script_tag.jmespath("name").get()
                    or listing_page_cart.css('h1::text').get()
                    or listing_page_cart.xpath('//*[@data-buy-box-listing-title]/text()').get()
                ).strip()
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing product_title: {e}")

            # --- Product URL Extraction --
            try:
                store_data.product_url = (
                    json.loads(product_info_script_tag.get()).get('url') # Use json.loads to automatically remove '\' from url
                    or selector.xpath('//link[starts-with(@href, "https://www.etsy.com/listing/")]/@href').get()
                ).strip()
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing product_url: {e}")


            # Main Image Extraction
            try:
                store_data.main_image = (
                    json.loads(product_info_script_tag.get()).get('image', [{}])[0].get("contentURL")  # Use json.loads to automatically remove '\' from url
                    or photo_container.css('img[data-perf-group="main-product-image"])').get()
                    or photo_container.xpath('.//img/@src').get()
                ).strip()
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing image: {e}")


            # Prices ( price_usd & sale_price_usd) Extraction
            try:
                prices = (
                    listing_page_cart.xpath('.//div[contains(@data-appears-component-name, "price")]//p//text()').re(r"\d+(?:[.,]\d+)?")
                    or product_info_script_tag.jmespath("offers.price").get()
                )
                if prices:
                    if len(prices) == 2:
                        # Convert prices to float for comparison
                        prices = [float(price.replace(',', '')) for price in prices]

                        # Simple store big value in price_usd and other in sale_price_usd
                        if prices[0] > prices[1]:
                            store_data.price_usd = prices[0]
                            store_data.sale_price_usd = prices[1]
                        else:
                            store_data.price_usd = prices[1]
                            store_data.sale_price_usd = prices[0]
                    else:
                        # If have only 1 price then its mean sale is ended
                        store_data.price_usd = prices[0]
                        store_data.sale_price_usd = None
                
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing prices: {e}")


            # --Star Seller Detection--
            try:
                store_data.star_seller = bool(
                    # Simple "Start Seller" is unique text, always will exist if seller have star badge
                    listing_page_cart.xpath('.//*[contains(text(), "Star Seller")]').get()
                    # Use this as a fallback Containing information about the seller badge
                    or listing_page_cart.css('.star-seller-badge-listing-page p::text').get()
                )
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing star_seller: {e}")


            # --Number in Basket Detection--
            try:
                store_data.number_in_basket = (
                    # Use only one method, As its container dynamically changing
                    listing_page_cart.xpath('.//div[contains(@data-appears-component-name, "Etsy-Modules-ListingPage-UrgencySignal-RecsRankingApiSpec")]//p//text()').get()
                )
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing number_in_basket: {e}")


            # --Store name, url, brand extraction--
            try:
                store_owner_container = (
                    selector.css('#shop_owners_content_toggle')
                    or selector.xpath('.//div[contains(@class, "wt-thumbnail")]/..')
                )
            
                store_data.store_name = (
                    # First find within store owner container
                    store_owner_container.css('p[class*="wt-text-heading"]::text').get() 
                    # Use fallback and find all a links with prefix and get its text
                    or selector.xpath('.//a[starts-with(@href, "https://www.etsy.com/shop/")]/text()').get()
                ).strip()

                store_data.brand = (
                    store_owner_container.xpath('.//p[contains(text(), "Owner of")]/a/text()').get()
                    or selector.xpath('.//a[starts-with(@href, "https://www.etsy.com/shop/")]/text()').get()
                ).strip()

                store_url = (
                    # "Designed by" container have same url style that we want
                    selector.xpath('.//div[contains(text(), "Designed by")]/a/@href').get()
                    # Otherwise we have to scrape long referral links from owner container
                    or store_owner_container.xpath('.//p[contains(text(), "Owner of")]/a/@href').get()
                ).strip()
                
                # Make url with brand and prefix, if failed then add store url that we have find above
                store_data.store_url = f"https://www.etsy.com/shop/{store_data.brand}" if store_data.brand else store_url

            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing store_name, store_url, brand: {e}")


            # --Store reviews Extraction--
            try:
                store_reviews = (
                    product_info_script_tag.jmespath("aggregateRating.reviewCount").get()
                    or data_reviews_container.xpath('string(.//h2)').re(r"\d+(?:[.,]\d+)?")[0]
                )
                if store_reviews:
                    if ',' in str(store_reviews):
                        store_reviews = store_reviews.replace(', ', '')

                    store_data.store_reviews = int(store_reviews)

                else: 
                    store_data.store_reviews = None

            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing store_reviews: {e}")

            # --Rating Value Extraction--
            try:
                rating_value = (
                    # Give xpath method 1st priority, as it have more accurate digits after decimal
                    data_reviews_container.xpath('.//h2/..//input[contains(@name, "rating")]/@value').get()
                    or product_info_script_tag.jmespath("aggregateRating.ratingValue").get()
                ).strip()
                store_data.rating_value = float(rating_value) if rating_value else None

            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing rating_value: {e}")

            # --Product Reviews Extraction--
            try:
                product_reviews = (
                    data_reviews_container.xpath('.//div[contains(@class, "reviews__tabs")]/button[contains(text(), "This item")]/span/text()').re(r"\d+(?:[., ]\d+)?")[0]
                ).strip()
                store_data.product_reviews = int(product_reviews.replace(', ', '')) if product_reviews else None
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing product_reviews: {e}")


            # --Date of latest review Extraction--
            try:
                store_data.date_of_latest_review = (
                    # For now let's trust only on script tag, as its have more accurate date format
                    product_info_script_tag.jmespath("review[0].datePublished").get()
                ).strip()
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing date_of_latest_review: {e}")


            # --Digital Download Extraction
            try:
                store_data.digital_download = bool(
                    product_details.xpath('.//div[contains(text(), "Digital download")]').get()
                )
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing digital_download: {e}")


            # --Data Listed Extraction--
            try:
                date_listed = (
                    selector.xpath('.//div[contains(text(), "Listed on ")]//text()').get()
                )
                store_data.date_listed = date_listed.split('Listed on')[1].strip() if date_listed else None
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing date_listed: {e}")<e

            # --Number of favourties Extraction--
            try:
                text_of_favourties = (
                    selector.xpath('.//a[contains(text(), " favourites")]//text()').get()
                )
                number_of_favourties = text_of_favourties.split('favourites')[0].strip() if text_of_favourties else None

                if number_of_favourties:
                    if ',' in number_of_favourties:
                        number_of_favourties = number_of_favourties.replace(',', '')
                    store_data.number_of_favourties = int(number_of_favourties)
                else:
                    store_data.number_of_favourties = None

            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing number_of_favourties: {e}")


            # Category tree, name, url Extraction
            try:
                a_tags = (
                     category_tree_container.xpath('.//a')
                )

                text_list = [
                        re.sub(r'\s+', ' ', text).strip()
                        for text in category_tree_container.xpath('.//text()').getall() if text.strip()
                    ]
                
                store_data.category_name = (
                    a_tags[-1].xpath('.//text()').get().strip()
                    or text_list[-1]
                )

                store_data.category_url = (
                    a_tags[-1].xpath('./@href').get().split('?')[0].strip()
                )

                store_data.category_tree = (
                    ' > '.join(text_list)
                    or ' > '.join([link.xpath('./text()').get() for link in a_tags])
                )
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing category_tree, category_name, category_url: {e}")

             # --Related Searches Extraction--
            try: store_data.related_searches = [
                re.sub(r'\s+', ' ', text).strip() # Remove unwanted spaces
                for text in tags_section_container.xpath( 
                    # Used '|' Or operator to match both tags
                    './/h3[contains(@class, "tag-card-title")]//text() | .//a[contains(@class, "wt-btn wt-action-group__item")]//text()'
                ).getall()
            ]
            except Exception as e:
                self.logger.warning(f"⚠️ Error parsing related_searches: {e}")


            return store_data.to_dict()
        except Exception as e:
            self.logger.error(f"❌ Error parsing store page: {e}")
            return None
        

    async def etsy_product_scraper(self) -> Dict[str, Any]:
        self.logger.info("🔎 Starting Etsy product Scraper...")
        try:
            html_content, error_message = await self.helpers.fetch_page()
            if error_message:
                self.logger.error("⚠️ Skipping parsing due to fetch error. Error: " + error_message)
                return {
                    "search_url": self.url,
                    "error": error_message
                }
            
            result = await self.parse_product_page(html_content)
            if not result:
                self.logger.error("⚠️ No data found in the product page.")
                return {
                    "error": "No data found in the product page. Might be URL is wrong, Or Css selectors becomes over dated."
                }
            else:
                self.logger.info("✅ product data successfully parsed.")
                return result


        except Exception as e:
            self.logger.error(f"❌ Critical error during product scraping: {str(e)}")
            raise RuntimeError(f"Scraping failed: {str(e)}")



if __name__ == "__main__":
    # 🔧 Enable full debug logs during testing
    logger = setup_logging(console_level=logging.DEBUG)

    # 🧪 Test URL (can replace with any Etsy Store)
    url = "https://www.etsy.com/listing/1583875617/family-and-couple-annual-budget-google"

    logger.info("🔬 Starting standalone test for EtsyProductScraper...")

    try:
        start_time = time.time()

        scraper = EtsyProductScraper(url, proxy=None, timeout=10)
        result = asyncio.run(scraper.etsy_product_scraper())

        end_time = time.time()
        duration = end_time - start_time

        logger.info(f"⏱️ Scraping completed in {duration:.2f} seconds")
        import pprint
        pprint.pprint(result)
        # 💾 Save output
        output_file = "product.json"
        with open(output_file, "w", encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=4)

        logger.info(f"📁 Data saved to {output_file}")

    except Exception as e:
        logger.error(f"❌ Test run failed: {str(e)}", exc_info=True)

