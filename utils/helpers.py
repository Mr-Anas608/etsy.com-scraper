import sys, os

# Ensure the project's root directory is in the Python path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logs.custom_logging import setup_logging 
import logging

from typing import Optional, List, Dict, Any
from aiohttp import ClientSession


class Helpers:
    def __init__(self, url: str, headers: Dict[str, str] = None, proxy: Optional[str] = None, timeout: int = 10):
        self.url = url
        self.proxy = proxy
        self.timeout = timeout
        self.logger = setup_logging(console_level=logging.DEBUG)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Cache-Control": "max-age=0",
        }

    async def fetch_page(self) -> Optional[str]:
        """Fetches HTML content from the stored URL."""
        try:
            self.logger.info(f"🌐 Fetching HTML content from: {self.url}")  # Use f-string
            async with ClientSession() as session:
                response = await session.get(self.url, proxy=self.proxy, headers=self.headers, timeout=self.timeout)
                response.raise_for_status()
                html_content = await response.text()
                self.logger.debug(f"✅ Page fetched successfully. Response len = {len(html_content)} char.")
                self.logger.info(
                    f"✅ Page fetched successfully with status: {response.status} and length: {len(html_content)}")  # Use f-string
                return html_content, None
        except Exception as exc:
            error_message = f"❌ Error during fetching: {exc}"  # Use f-string
            self.logger.error(error_message)
            return None, error_message
