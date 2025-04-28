import asyncio
import time
import json
import os
from datetime import datetime
import sys
import random

import pandas as pd
import aiohttp
from fake_useragent import UserAgent

# Ensure the project's root directory is in the Python path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logs.custom_logging import setup_logging

# Setup
logger = setup_logging()
ua = UserAgent()

# Base URL for categories
base_url = "https://www.etsy.com/c/jewelry?explicit=1&instant_download=true&ship_to=GB&order=highest_reviews&page="
already_used = set()

# Create directories for storing HTML and results
os.makedirs("utils/debug", exist_ok=True)
os.makedirs("utils/debug/reports", exist_ok=True)

class ScraperTester:
    def __init__(self, api_base_url="https://etsy-com-scraper.onrender.com/", total_categories=250, max_stores=250):
        self.api_base_url = api_base_url
        self.total_categories = total_categories
        self.max_stores = max_stores
        self.category_results = []
        self.store_results = []
        self.store_urls = set()
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
    def get_headers(self, user_agent):
        """Generate request headers with given user agent."""
        # return {
        #         'User-Agent': f'{user_agent}',
        #         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        #         'Accept-Language': 'en-US,en;q=0.5',
        #         'DNT': '1',
        #         'Connection': 'keep-alive',
        #         'Upgrade-Insecure-Requests': '1',
        #         'Sec-Fetch-Dest': 'document',
        #         'Sec-Fetch-Mode': 'navigate',
        #         'Sec-Fetch-Site': 'none',
        #         'Sec-Fetch-User': '?1',
        #         'Pragma': 'no-cache',
        #         'Cache-Control': 'no-cache',
        #     }

    #     return {
  
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0',
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #     'Accept-Language': 'en-US,en;q=0.5',
    #     # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    #     'DNT': '1',
    #     'Sec-GPC': '1',
    #     'Connection': 'keep-alive',
    #     'Upgrade-Insecure-Requests': '1',
    #     'Sec-Fetch-Dest': 'document',
    #     'Sec-Fetch-Mode': 'navigate',
    #     'Sec-Fetch-Site': 'none',
    #     'Sec-Fetch-User': '?1',
    #     'Priority': 'u=0, i',
    #     'Pragma': 'no-cache',
    #     'Cache-Control': 'no-cache',
    # }
    

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Connection': 'keep-alive',
    'Cookie': 'uaid=bYLctygEEiT8-9zfqHMX5vQmeZ9jZACCDIbEABhdrVSamJmiZKUU6Rvm4ZgYbx6Q41uVnuJhYFSWmWoZlpuUX1BVrFTLAAA.; user_prefs=2-jl6r0xIZNjh60_WV8N6zxneoJjZACCDIbEABgdreTuFKCkk1eak6OjlJqn6-6kpKMEIsAiRhAKFxHLAAA.; fve=1744855377.0; _fbp=fb.1.1744855377039.3044595180781198; exp_ebid=m=UIJ%2BKW7tIYMoxxex1SeY8PmAaz6REUHanY1VRK2SfcI%3D,v=Kvus9PVFNfQPJcWnBTbnzjbsU_gyfEZt; datadome=fIPp_MqZPaxckAIEUWP5j7E1HTGxzTx2kWR5hVHOBlJ8IlVohAG8iq5OjDMFOCjj4CPaciYLYoaIx5p9OeGOYveS5MZl9L64fIF7inH_d_6dyi_gjWGsFnlK_CuPLhfv; ua=531227642bc86f3b5fd7103a0c0b4fd6; _gcl_au=1.1.241807951.1744855380; _ga_KR3J610VYM=GS1.1.1745236246.17.0.1745236246.60.0.0; _ga=GA1.1.1564093969.1744855382; lantern=dc0c732b-b507-44fa-ab0e-55bb98bd6153; _ga_WSQNWKVGKE=GS1.1.1744884186.1.0.1744884237.0.0.0; _ga_0X0TDCYXJK=GS1.1.1744983146.4.1.1744984914.0.0.0; _ga_4H5M4GDE3Q=GS1.1.1744979462.2.1.1744980932.0.0.0',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'DNT': '1',
    'Sec-GPC': '1',
    'Priority': 'u=0, i',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

    def generate_category_urls(self):
        """Generate category URLs for testing."""
        urls = []
        for i in range(1, self.total_categories + 1):
            urls.append(f"{base_url}{i}")
        return urls
    
    def get_random_user_agent(self):
        """Get a random user agent that hasn't been used before."""
        max_attempts = 100
        for _ in range(max_attempts):
            user_agent = ua.random
            if user_agent not in already_used:
                already_used.add(user_agent)
                return user_agent
        
        # If we've exhausted unique user agents, reset and start over
        already_used.clear()
        return ua.random
    
    async def fetch_category_page(self, session, url, page_num):
        """Fetch a single category page using the API endpoint."""
        start_time = time.time()
        user_agent = self.get_random_user_agent()
        print(f"Using user agent: {user_agent}")

        try:
            # First get the raw HTML
            headers = self.get_headers(user_agent)
            async with session.get(url, headers=headers) as response:
                html_content = await response.text()
                status_code = response.status
                
                # Save HTML content
                if len(html_content) < 2000:
                    logger.info(f"Page {page_num}: Possibly captcha, HTML length: {len(html_content)}")
                    with open(f"utils/debug/captcha_Page_{page_num}.html", "w", encoding="utf-8") as f:
                        f.write(html_content)
                else:
                    with open(f"utils/debug/Page_{page_num}.html", "w", encoding="utf-8") as f:
                        f.write(html_content)
                
                # Now call the API endpoint with the URL
                category_api_url = f"{self.api_base_url}/category"
                payload = {
                    "url": url,
                    "timeout": 30,
                    'proxy': "http://germanproxy42de:tyF8SSTx27jg@168.119.244.147:13864"
                }
                
                try:
                    api_start_time = time.time()
                    async with session.post(category_api_url, json=payload) as api_response:
                        category_data = await api_response.json()
                        api_end_time = time.time()
                        api_request_time = api_end_time - api_start_time
                except Exception as api_err:
                    logger.error(f"API error for page {page_num}: {str(api_err)}")
                    category_data = {"error": str(api_err)}
                    api_request_time = 0
                
                end_time = time.time()
                total_request_time = end_time - start_time
                
                return {
                    "page_num": page_num,
                    "url": url,
                    "user_agent": user_agent,
                    "status_code": status_code,
                    "html_length": len(html_content),
                    "request_time": total_request_time,
                    "api_request_time": api_request_time,
                    "is_captcha": len(html_content) < 2000,
                    "category_data": category_data
                }
        except Exception as e:
            logger.error(f"Error fetching page {page_num}: {str(e)}")
            end_time = time.time()
            return {
                "page_num": page_num,
                "url": url,
                "user_agent": user_agent,
                "status_code": 0,
                "html_length": 0,
                "request_time": end_time - start_time,
                "api_request_time": 0,
                "is_captcha": False,
                "category_data": {"error": str(e)},
                "error": str(e)
            }
    
    async def fetch_store_page(self, session, url, store_name):
        """Fetch a single store page using the API endpoint."""
        start_time = time.time()
        user_agent = self.get_random_user_agent()
        
        try:
            # First get the raw HTML
            headers = self.get_headers(user_agent)
            async with session.get(url, headers=headers) as response:
                html_content = await response.text()
                status_code = response.status
                
                # Save HTML content
                if len(html_content) < 2000:
                    logger.info(f"Store {store_name}: Possibly captcha, HTML length: {len(html_content)}")
                    with open(f"utils/debug/captcha_Store_{store_name}.html", "w", encoding="utf-8") as f:
                        f.write(html_content)
                
                with open(f"utils/debug/Store_{store_name}.html", "w", encoding="utf-8") as f:
                    f.write(html_content)
                
                # Now call the API endpoint with the URL
                store_api_url = f"{self.api_base_url}/store"
                payload = {
                    "url": url,
                    "timeout": 30,
                    'proxy': "http://germanproxy42de:tyF8SSTx27jg@168.119.244.147:13864"
                }
                
                try:
                    api_start_time = time.time()
                    async with session.post(store_api_url, json=payload) as api_response:
                        store_data = await api_response.json()
                        api_end_time = time.time()
                        api_request_time = api_end_time - api_start_time
                except Exception as api_err:
                    logger.error(f"API error for store {store_name}: {str(api_err)}")
                    store_data = {"error": str(api_err)}
                    api_request_time = 0
                
                end_time = time.time()
                total_request_time = end_time - start_time
                
                return {
                    "store_name": store_name,
                    "url": url,
                    "user_agent": user_agent,
                    "status_code": status_code,
                    "html_length": len(html_content),
                    "request_time": total_request_time,
                    "api_request_time": api_request_time,
                    "is_captcha": len(html_content) < 2000,
                    "store_data": store_data
                }
        except Exception as e:
            logger.error(f"Error fetching store {store_name}: {str(e)}")
            end_time = time.time()
            return {
                "store_name": store_name,
                "url": url,
                "user_agent": user_agent,
                "status_code": 0,
                "html_length": 0,
                "request_time": end_time - start_time,
                "api_request_time": 0,
                "is_captcha": False,
                "store_data": {"error": str(e)},
                "error": str(e)
            }
    
    def count_empty_fields(self, data):
        """Count empty fields in a dictionary recursively."""
        empty_count = 0
        
        if isinstance(data, dict):
            for key, value in data.items():
                if value is None or value == "" or (isinstance(value, list) and len(value) == 0):
                    empty_count += 1
                elif isinstance(value, dict) or isinstance(value, list):
                    empty_count += self.count_empty_fields(value)
        
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, dict) or isinstance(item, list):
                    empty_count += self.count_empty_fields(item)
        
        return empty_count
    
    def process_category_result(self, page_data):
        """Process category API result and extract metrics."""
        result = {
            "Page No": page_data["page_num"],
            "UserAgent Used": page_data["user_agent"],
            "Response Status Code": page_data["status_code"],
            "Length of html": page_data["html_length"],
            "Request time": round(page_data["request_time"], 3),
            "API Request time": round(page_data["api_request_time"], 3),
            "No. Of Empty fields": 0,
            "No. of store urls found": 0,
            "Is Captcha": page_data["is_captcha"]
        }
        
        # Handle errors or captcha
        if page_data.get("error") or page_data["is_captcha"]:
            if page_data.get("error"):
                result["Error"] = page_data["error"]
            return result
        
        category_data = page_data["category_data"]
        
        # Handle API errors
        if "error" in category_data:
            result["Error"] = category_data["error"]
            return result
        
        # Count empty fields
        result["No. Of Empty fields"] = self.count_empty_fields(category_data)
        
        # Extract store URLs
        store_urls_found = 0
        for product in category_data.get("products", []):
            if product.get("store_url") and product["store_url"] not in self.store_urls:
                self.store_urls.add(product["store_url"])
                store_urls_found += 1
        
        result["No. of store urls found"] = store_urls_found
        
        # Save the JSON result
        with open(f"utils/debug/reports/category_result_{page_data['page_num']}.json", "w", encoding="utf-8") as f:
            json.dump(category_data, f, indent=4, ensure_ascii=False)
        
        return result
    
    def process_store_result(self, store_data):
        """Process store API result and extract metrics."""
        result = {
            "Store Name": store_data["store_name"],
            "UserAgent Used": store_data["user_agent"],
            "Response Status Code": store_data["status_code"],
            "Length of html": store_data["html_length"],
            "Request time": round(store_data["request_time"], 3),
            "API Request time": round(store_data["api_request_time"], 3),
            "No. Of Empty fields": 0,
            "Is Captcha": store_data["is_captcha"]
        }
        
        # Handle errors or captcha
        if store_data.get("error") or store_data["is_captcha"]:
            if store_data.get("error"):
                result["Error"] = store_data["error"]
            return result
        
        api_result = store_data["store_data"]
        
        # Handle API errors
        if "error" in api_result:
            result["Error"] = api_result["error"]
            return result
        
        # Count empty fields
        result["No. Of Empty fields"] = self.count_empty_fields(api_result)
        
        # Save the JSON result
        with open(f"utils/debug/reports/store_result_{store_data['store_name']}.json", "w", encoding="utf-8") as f:
            json.dump(api_result, f, indent=4, ensure_ascii=False)
        
        return result
    
    async def run_category_test(self):
        """Run the category scraper test with all URLs in parallel."""
        logger.info(f"Starting category test with {self.total_categories} URLs")
        
        # Generate all category URLs
        category_urls = self.generate_category_urls()
        
        start_time = time.time()
        
        # Create a connection pool for concurrent requests
        connector = aiohttp.TCPConnector(limit=5)  # Limit concurrent connections
        async with aiohttp.ClientSession(connector=connector) as session:
            # Create tasks for all category URLs
            tasks = []
            for i, url in enumerate(category_urls, 1):
                tasks.append(self.fetch_category_page(session, url, i))
            
            # Run all fetch tasks concurrently
            fetch_results = await asyncio.gather(*tasks)
            
            # Process the results
            self.category_results = [self.process_category_result(result) for result in fetch_results]
        
        end_time = time.time()
        total_time = end_time - start_time
        
        logger.info(f"Category test completed in {total_time:.2f} seconds")
        return total_time
    
    async def run_store_test(self):
        """Run the store scraper test with store URLs in parallel."""
        # Limit to max_stores
        store_urls_list = list(self.store_urls)[:self.max_stores]
        
        if not store_urls_list:
            logger.warning("No store URLs found to test")
            return 0
        
        logger.info(f"Starting store test with {len(store_urls_list)} URLs")
        
        start_time = time.time()
        
        # Create a connection pool for concurrent requests
        connector = aiohttp.TCPConnector(limit=100)  # Limit concurrent connections
        async with aiohttp.ClientSession(connector=connector) as session:
            # Create tasks for all store URLs
            tasks = []
            for url in store_urls_list:
                store_name = url.split("/")[-1]
                tasks.append(self.fetch_store_page(session, url, store_name))
            
            # Run all fetch tasks concurrently
            fetch_results = await asyncio.gather(*tasks)
            
            # Process the results
            self.store_results = [self.process_store_result(result) for result in fetch_results]
        
        end_time = time.time()
        total_time = end_time - start_time
        
        logger.info(f"Store test completed in {total_time:.2f} seconds")
        return total_time
    
    def save_results_to_csv(self):
        """Save test results to CSV files."""
        # Save category results
        if self.category_results:
            df = pd.DataFrame(self.category_results)
            category_csv_path = f"utils/debug/reports/category_test_results_{self.timestamp}.csv"
            df.to_csv(category_csv_path, index=False)
            logger.info(f"Category results saved to {category_csv_path}")
        
        # Save store results
        if self.store_results:
            df = pd.DataFrame(self.store_results)
            store_csv_path = f"utils/debug/reports/store_test_results_{self.timestamp}.csv"
            df.to_csv(store_csv_path, index=False)
            logger.info(f"Store results saved to {store_csv_path}")
    
    def generate_summary_report(self, category_time, store_time):
        """Generate a summary markdown report."""
        # Calculate statistics
        category_df = pd.DataFrame(self.category_results)
        store_df = pd.DataFrame(self.store_results) if self.store_results else pd.DataFrame()
        
        report = []
        report.append("# Etsy Scraper Performance Test Summary")
        report.append(f"\nTest Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        report.append("\n## Overall Test Results")
        report.append(f"- Total Category URLs: {self.total_categories}")
        report.append(f"- Total Category Scraping Time: {category_time:.2f} seconds")
        report.append(f"- Total Store URLs Found: {len(self.store_urls)}")
        report.append(f"- Store URLs Tested: {len(self.store_results)}")
        report.append(f"- Total Store Scraping Time: {store_time:.2f} seconds")
        report.append(f"- Combined Total Time: {category_time + store_time:.2f} seconds")
        
        # Category statistics
        if not category_df.empty:
            report.append("\n## Category Test Statistics")
            report.append(f"- Average Request Time: {category_df['Request time'].mean():.3f} seconds")
            report.append(f"- Average API Processing Time: {category_df['API Request time'].mean():.3f} seconds")
            report.append(f"- Fastest Request: {category_df['Request time'].min():.3f} seconds")
            report.append(f"- Slowest Request: {category_df['Request time'].max():.3f} seconds")
            report.append(f"- Successful Responses (200): {(category_df['Response Status Code'] == 200).sum()}")
            report.append(f"- Failed Responses: {(category_df['Response Status Code'] != 200).sum()}")
            report.append(f"- Captcha Pages: {category_df['Is Captcha'].sum()}")
            report.append(f"- Total Empty Fields: {category_df['No. Of Empty fields'].sum()}")
            report.append(f"- Average Empty Fields per Page: {category_df['No. Of Empty fields'].mean():.2f}")
            report.append(f"- Total Store URLs Found: {category_df['No. of store urls found'].sum()}")
        
        # Store statistics
        if not store_df.empty:
            report.append("\n## Store Test Statistics")
            report.append(f"- Average Request Time: {store_df['Request time'].mean():.3f} seconds")
            report.append(f"- Average API Processing Time: {store_df['API Request time'].mean():.3f} seconds")
            report.append(f"- Fastest Request: {store_df['Request time'].min():.3f} seconds")
            report.append(f"- Slowest Request: {store_df['Request time'].max():.3f} seconds")
            report.append(f"- Successful Responses (200): {(store_df['Response Status Code'] == 200).sum()}")
            report.append(f"- Failed Responses: {(store_df['Response Status Code'] != 200).sum()}")
            report.append(f"- Captcha Pages: {store_df['Is Captcha'].sum()}")
            report.append(f"- Total Empty Fields: {store_df['No. Of Empty fields'].sum()}")
            report.append(f"- Average Empty Fields per Store: {store_df['No. Of Empty fields'].mean():.2f}")
        
        # Save the report
        report_path = f"utils/debug/reports/test_summary_{self.timestamp}.md"
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("\n".join(report))
        
        logger.info(f"Summary report saved to {report_path}")
        return "\n".join(report)

async def main():
    # Create tester instance - specify your FastAPI server URL here
    api_base_url = "http://65.109.59.224:8010"  # Change this if your API is on a different host/port
    tester = ScraperTester(api_base_url=api_base_url, total_categories=15, max_stores=0)
    
    # Run category test
    category_time = await tester.run_category_test()
    
    # Run store test
    store_time = await tester.run_store_test()
    
    # Save results to CSV
    tester.save_results_to_csv()
    
    # Generate summary report
    summary = tester.generate_summary_report(category_time, store_time)
    print("\nTest Summary:")
    print(summary)

if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())