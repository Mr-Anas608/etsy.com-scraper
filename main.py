from fastapi import FastAPI, HTTPException, Body
import asyncio
from scrapers.category_scraper import EtsyCategoryScraper

app = FastAPI()

@app.post("/category")
async def handle_category(data: dict = Body(...)):
    try:
        url = data.get('url')
        proxy = data.get('proxy')
        timeout = data.get('timeout', 10)

        if not url:
            raise HTTPException(status_code=400, detail="Missing 'url' field")

        scraper = EtsyCategoryScraper(url=url, proxy=proxy, timeout=timeout)
        result = await scraper.etsy_category_scraper()  # Use 'await' here

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")