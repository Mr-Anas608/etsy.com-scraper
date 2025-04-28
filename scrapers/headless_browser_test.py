from seleniumbase import BaseCase, SB
from seleniumwire import webdriver


class BaseTestCase(BaseCase):

    def get_new_driver(self, *args, **kwargs):
        self.driver = webdriver.Firefox()
        self._drivers_list = [self.driver]
        return self.driver

    def setUp(self):
        super(BaseTestCase, self).setUp()

    def sb_test(self) -> str:
        with SB(
            headless=True,
            headless2=True,
            browser="firefox",
            page_load_strategy="eager",
            uc=False,  # Ensure undetected-chromedriver is OFF
            undetectable=False, # Also ensure this is OFF
            binary_location=None,  # Set binary_location to None for Firefox
        ) as sb:
           
            sb.open("https://www.etsy.com/uk/listing/1583875617/family-and-couple-annual-budget-google?ref=landingpage_similar_listing_bot-1&pro=1&sts=1&listing_id=1583875617&listing_slug=family-and-couple-annual-budget-google&logging_key=cac5e902bc9a84971f59bffc3fd67c092b91d3ce%3A1583875617")

            sb.sleep(2)
            page_source = sb.get_page_source()

        return page_source
    
    def test_wire(self):
        driver2 = webdriver.Firefox()
        self._drivers_list.append(driver2)
        self.driver = driver2
        self.open("https://www.etsy.com/uk/listing/1583875617/family-and-couple-annual-budget-google?ref=landingpage_similar_listing_bot-1&pro=1&sts=1&listing_id=1583875617&listing_slug=family-and-couple-annual-budget-google&logging_key=cac5e902bc9a84971f59bffc3fd67c092b91d3ce%3A1583875617")
        self.sleep(2)
        page_source = self.get_page_source()
        return page_source
        
if __name__ == "__main__":
    # scraper = EtsyProductScraper()
    # print(asyncio.run(scraper.cr_test()))
    scraper = BaseTestCase()
    print(scraper.test_wire())