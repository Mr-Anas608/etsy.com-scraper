from fastapi import FastAPI, Request
from scrapers.category_scraper import EtsyCategoryScraper  # Import your real scraper
from scrapers.product_scraper import EtsyProductScraper
from scrapers.store_scraper import EtsyStoreScraper

app = FastAPI()

@app.post("/category")
async def category_scraper(request: Request):
    try:
        data = await request.json()
        url = data.get("url")
        proxy = data.get("proxy", None)
        timeout = data.get("timeout", 10)

        if not url:
            return {"error": "Missing 'url' field"}

        # Create scraper instance
        scraper = EtsyCategoryScraper(url=url, proxy=proxy, timeout=timeout)

        # Await the actual async scraping method
        result = await scraper.etsy_category_scraper()
        return result

    except Exception as e:
        return {"error": f"Server error: {str(e)}"}
    
@app.post("/store")
async def store_scraper(request: Request):
    try:
        data = await request.json()
        url = data.get("url")
        proxy = data.get("proxy", None)
        timeout = data.get("timeout", 10)

        if not url:
            return {"error": "Missing 'url' field"}

        # Create scraper instance
        scraper = EtsyStoreScraper(url=url, proxy=proxy, timeout=timeout)

        # Await the actual async scraping method
        result = await scraper.etsy_store_scraper()
        return result

    except Exception as e:
        return {"error": f"Server error: {str(e)}"}
    
@app.post("/product")
async def product_scraper(request: Request):
    try:
        data = await request.json()
        url = data.get("url")
        proxy = data.get("proxy", None)
        timeout = data.get("timeout", 10)

        if not url:
            return {"error": "Missing 'url' field"}

        # Create scraper instance
        scraper = EtsyProductScraper(url=url, proxy=proxy, timeout=timeout)

        # Await the actual async scraping method
        result = await scraper.etsy_product_scraper()
        return result

    except Exception as e:
        return {"error": f"Server error: {str(e)}"}
    
@app.get("/sb-test")
async def sb_test():
    try:
        scraper = EtsyProductScraper()
        result = await scraper.sb_test()
        return {"result": result}
    except Exception as e:
        return {"error": f"Server error: {str(e)}"}
    
@app.get("/")
def root():
    return {"message": "Welcome to the Etsy Scraper API!"}


# Payload example for future

payload = {
            "url": False, # If you want to scrape on url at a time. 
            "batches" : {
                "urls" : [],  # if you want to scrape in batches, with different url,
                "min_time" : 1, # Minimum time you want to set per url request, By default 1
                "max_time" : 5, # Maximum time you want to set per url request, By default 5
                "max_concurrent" : False, # Maximum concurrent request you want to set, By default 5
            },
            "headers" : False, # if you want to use your custom headers otherwise default will be used.
            "Cookie" : False, # if you want to use your custom cookies otherwise will be scraped without cookie
            "timeout": 30, # Max Timeout if you want to set.
            'proxy': "http://germanproxy42de:tyF8SSTx27jg@168.119.244.147:13864"
}