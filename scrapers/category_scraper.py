import sys, os

# Ensure the project's root directory is in the Python path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logs.custom_logging import setup_logging 

import httpx
from bs4 import BeautifulSoup
import re
from typing import Optional, List, Tuple, Dict, Any
import asyncio
import json
from lxml import html


class EtsyCategoryScraper:
    def __init__(self, url: str, proxy: Optional[str] = None, timeout: int = 5):
        self.logger = setup_logging()
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



    async def fetch_page(self) -> Optional[str]:
        try:
            async with httpx.AsyncClient(headers=self.headers, timeout=self.timeout, follow_redirects=True) as client:
                response = await client.get(self.url)
                response.raise_for_status() # Raise exception for 4xx/5xx status codes
                return response.text, None
        except httpx.RequestError as exc:
            error_message = f"Network error occurred while requesting {exc.request.url}: {exc}"
            self.logger.error(error_message)
            return None, error_message
        except httpx.HTTPStatusError as exc:
            error_message = f"Error response {exc.response.status_code} while requesting {exc.request.url}."
            self.logger.error(error_message)
            return None, error_message
        except Exception as exc:
            error_message = f"An unexpected error occurred during fetch: {exc}"
            self.logger.error(error_message)
            return None, error_message

        
    async def extract_category_tree_from_url(self, url: str) -> Tuple[Optional[str], Optional[str]]:
        """
        Extracts category tree and name from an Etsy /c/ URL.
        Returns (None, None) if parsing fails or URL format is unexpected.
        """
        try:
            if "/c/" not in url:
                return None, None
            # Extract the part after /c/ and before '?'
            path_part = url.split("/c/", 1)[1]
            path = path_part.split("?", 1)[0]
            # Split, remove empty segments, format
            parts = [p for p in path.strip("/").split("/") if p]
            if not parts:
                return None, None
            formatted_parts = [p.replace("-", " ").title() for p in parts]
            # Construct category tree and name
            category_tree = "Homepage > " + " > ".join(formatted_parts)
            category_name = formatted_parts[-1]
            return category_tree, category_name
        
        except Exception as e:
            # Catch potential errors during splitting/
            error_message = f"Error parsing URL {url}: {e}"
            self.logger.error(error_message)
            return None, None # Return None on any parsing error
        
    async def etsy_category_scraper(self) -> dict:
        try:
            html_content, error_message = await self.fetch_page()
            if error_message:
                return {
                "category_tree": None, "category_name": None,
                "products": [], "search_url": self.url, "error": error_message
                }
            
            soup = BeautifulSoup(html_content, "html.parser")

    
            category_tree, category_name = await self.extract_category_tree_from_url(self.url)
            
            products: List[Dict[str, Any]] = []

            product_cards = soup.select("div.v2-listing-card")
            
            for card in product_cards:
                try:
                    tree = html.fromstring(str(card))
                    # --- Get Product ID (from card div attribute) ---
                    product_id = card.get('data-listing-id')
                    if not product_id:
                        product_id = tree.xpath(".//a[@data-listing-id]/@data-listing-id")
                        if product_id:
                            product_id = product_id[0].strip()
                        if not product_id:
                            continue # Skip this iteration if no ID found
                    
                    # --- Get Product Name ---
                    title_tag = card.select_one("h3.v2-listing-card__title")
                    product_name = title_tag.get_text(strip=True) if title_tag else None
                    if not product_name:
                        product_name = tree.xpath("//h3/text()")
                        if product_name:
                            product_name = product_name[0].strip()
                        else:
                            None
        
                    # --- Get Product URL ---
                    link_tag = card.select_one("a.listing-link")
                    product_url = link_tag["href"] if link_tag else None
                    if not product_url:
                        product_url = tree.xpath(".//a[@data-listing-id]/@href")
                        if product_url:
                            product_url = product_url[0].strip()
                        else:
                            None
            
                    # --- Get Reviews (Score & Count) ---
                    rating_input = card.select_one("input[name='rating']")
                    if rating_input:
                        rating_value_str = rating_input.get('value')
                        if rating_value_str:
                            try: store_review_score = float(rating_value_str)
                            except (ValueError, TypeError): pass # Ignore conversion errors
                        else:
                            store_review_score = None

                    # Refined selector for review count span might be needed if ambiguous
                    review_count_tag = card.select_one("span.wt-text-gray.wt-display-inline-block")
                    if review_count_tag:
                        review_count_text = review_count_tag.get_text(strip=True)
                        if review_count_text:
                            match = re.search(r'\(([\d,]+)\)', review_count_text)
                            if match:
                                review_count_str = match.group(1).replace(',', '') # Remove commas to get the pure number
                                try: store_reviews_number = int(review_count_str)
                                except (ValueError, TypeError): pass # Ignore conversion errors
                            else:
                                store_reviews_number = None

                    # --- Get Seller Info & Ad Status ---
                    store_name = None
                    is_ad = False
                    seller_info_p = card.select_one("p.wt-text-caption.wt-mb-xs-1") # Paragraph containing seller/ad info
                    if seller_info_p:
                        full_text = seller_info_p.get_text(separator=' ', strip=True)
                        words = [word for word in re.split(r'\s+', full_text) if word]
                        print(f"Seller info text: {words}") # Debugging line

                        if "ad" in words and "by" in words:
                            is_ad = True
                            try:
                                by_index = words.index("by")
                                if by_index < len(words) - 1:
                                    store_name = words[-1]
                            except ValueError:
                                pass # Handle case where "by" might be missing (unlikely if "ad" is present)
                        elif words:
                            store_name = words[-1] # Last word in the paragraph is likely the store name        
                    store_url = f"https://www.etsy.com/uk/shop/{store_name}" if store_name else None
                    star_seller = True if "Star Seller" in str(card) else False

                    products.append({
                        "product_name": product_name,
                        "product_url": product_url,
                        "product_id": product_id,
                        "store_review_score": store_review_score,
                        "store_reviews_number": store_reviews_number,
                        "star_seller": star_seller,
                        "store_name": store_name,
                        "store_url": store_url,
                        "is_ad": is_ad
                    })
                except Exception:
                    continue

            return {
                "category_tree": category_tree,
                "category_name": category_name,
                "products": products,
                "search_url": self.url
            }

        except Exception as e:
            raise RuntimeError(f"Scraping failed: {str(e)}")

if __name__ == "__main__":
    # Example usage
    url = "https://www.etsy.com/uk/c/jewelry?explicit=1&instant_download=true&ship_to=GB&order=highest_reviews&page=8"
    scraper = EtsyCategoryScraper(url, proxy=None, timeout=10)
    result = asyncio.run(scraper.etsy_category_scraper())
    print(result)
    with open("category.json", "w", encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
    print("Data saved to category.json")