from fastapi import FastAPI, Request
from scrapers.category_scraper import EtsyCategoryScraper  # Import your real scraper
from scrapers.product_scraper import EtsyProductScraper

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
    
@app.get("/sb-test")
async def sb_test():
    try:
        scraper = EtsyProductScraper()
        result = await scraper.sb_test()
        return {"result": result}
    except Exception as e:
        return {"error": f"Server error: {str(e)}"}
    
@app.get("/chrome-version")
async def check_chrome():
    try:
        from seleniumbase import get_driver
        driver = get_driver()
        driver.get("chrome://version/")
        version_text = driver.find_element("tag name", "body").text
        driver.quit()
        return {"status": "success", "version": version_text}
    except Exception as e:
        return {"status": "error", "message": str(e)}