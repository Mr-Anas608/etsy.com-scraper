
# Etsy Scraper API Documentation

## Base URL
https://e.privatebrowser.dev

## Endpoints

### 1. Scrape Product Data
**Endpoint:** `/product`  
**Method:** POST  
#### Request Body
```json
{
    "url": "string",       // Required: Full Etsy product URL
    "proxy": boolean,      // Optional: Use proxy (default: false)
    "timeout": integer     // Optional: Timeout in seconds (default: 5, range: 1-300)
}
```

#### Response
```json
{
  "category_tree": "Homepage > Paper & Party Supplies > Paper > Stationery > Design & Templates > Templates",
  "sale_price_usd": 7.9,
  "star_seller": true,
  "price_usd": 19.75,
  "product_title": "Family And Couple Annual Budget Google Sheets Excel Spreadsheet Monthly Biweekly Budget Tracker Bill Calendar Debt Tracker 50/30/20 Tracker",
  "number_in_basket": "20+ views in the last 24 hours",
  "category_name": "Templates",
  "category_url": "https://www.etsy.com/uk/c/paper-and-party-supplies/paper/stationery/design-and-templates/templates?click_key=cac5e902bc9a84971f59bffc3fd67c092b91d3ce%3A1583875617&click_sum=8962503b&ref=catnav_breadcrumb-4&pro=1&sts=1&listing_id=1583875617&listing_slug=family-and-couple-annual-budget-google&explicit=1",
  "product_reviews": 1360,
  "ratingValue": 4.8166,
  "store_reviews": 1360,
  "date_of_latest_review": "19 Feb, 2025",
  "store_name": "TheSheetCode",
  "store_url": "https://www.etsy.com/uk/shop/TheSheetCode?ref=l2-about-shopname&from_page=listing",
  "brand": "TheSheetCode",
  "more_from_this_shop_names": [
    "Family And Couple Monthly Budget Google Sheets Excel Spreadsheet Weekly Biweekly Budget Tracker Bill Calendar Debt Tracker 50 30 20 Budget",
    "Annual Budget Google Sheets Excel Spreadsheet Monthly Biweekly Budget Tracker Bill Calendar Debt Tracker 50/30/20 Budget Spreadsheet Tracker",
    "Biweekly Paycheck Budget Spreadsheet Excel Google Sheets Fortnightly Budget Planner Debt Tracker Personal Tracker Savings Income Template",
    "Family Budget Planner Couples Budget Spreadsheet Excel Google Sheets Budget Bill Calendar Debt Tracker 50/30/20 Tracker Finance Budget Excel",
    "Family And Couple Simple Budget Google Sheets Excel Spreadsheet Weekly Biweekly Budget Tracker 50 30 20 Budget Paycheck Budget Tracker"
  ],
  "more_from_this_shop_urls": [
    "https://www.etsy.com/uk/listing/1583886759/family-and-couple-monthly-budget-google?click_key=7859f54f1a1538b978756cbdef01c509eddc8c8f%3A1583886759&click_sum=300daaf8&ref=related-1&pro=1&sts=1",
    "https://www.etsy.com/uk/listing/1583852219/annual-budget-google-sheets-excel?click_key=1ad120ead08eecb4b9ab9398893b540ce0de065f%3A1583852219&click_sum=e1ed456c&ref=related-2&pro=1&sts=1",
    "https://www.etsy.com/uk/listing/1797861917/biweekly-paycheck-budget-spreadsheet?click_key=44d1e24c6c41336258603065cd68c7feacb09a3b%3A1797861917&click_sum=79798d3f&ref=related-3&pro=1&sts=1",
    "https://www.etsy.com/uk/listing/1656342572/family-budget-planner-couples-budget?click_key=27562a0753cab832aac25c218a06fd7cd53a6d5a%3A1656342572&click_sum=9615435a&ref=related-4&pro=1&sts=1",
    "https://www.etsy.com/uk/listing/1583900575/family-and-couple-simple-budget-google?click_key=da4806df470d6196ff7ce810b888dad228b69a5c%3A1583900575&click_sum=e6906a7e&ref=related-5&pro=1&sts=1"
  ],
  "similar_products_names": [
    "Family And Couple Annual Budget Google Sheets Spreadsheet Monthly Biweekly Budget Tracker Financial Planner Bill Calendar Debt Tracker 50/30",
    "Family Annual Budget Spreadsheet Google Sheets Monthly Biweekly Budget Tracker Couple Financial Planner Bill Calendar Debt Tracker Yearly",
    "Family Annual Budget Excel Spreadsheet Google Sheets Monthly Biweekly Budget Tracker Couple Financial Planner Bill Calendar Debt Tracker",
    "Family Annual Budget Excel Spreadsheet Google Sheets Monthly Biweekly Budget Tracker Couple Financial Planner Bill Calendar Debt Tracker",
    "Family Annual Budget Monthly Budget Biweekly Tracker Excel Spreadsheet Google Sheets Couple Financial Planner Bill Calendar Debt Tracker",
    "Family Annual Budget Dark Mode Monthly Budget Tracker Excel Spreadsheet Google Sheets Couple Financial Planner Bill Calendar Debt Tracker",
    "Ultimate Annual Budget Planner Google Sheets Spreadsheet Dark Mode Yearly Monthly Weekly Biweekly Tracker Bill Calendar Savings Debt Tracker",
    "Ultimate Annual Budget Template Excel Google Sheets Budget Spreadsheet Organization Planner Life Planner Template Habit Tracker Task Tracker",
    "Ultimate Annual Budget Spreadsheet Google Sheets Budget Template Monthly Budget Spending Tracker Yearly Weekly Paycheck Budget Bill Tracker",
    "Annual Budget Planner & Monthly Budget Template for Google Sheets | Financial Planner | Bill Tracker and Debt Tracker",
    "Ultimate Annual Budget Spreadsheet Google Sheets Excel Budget Template Monthly Budget Planner Family Weekly Yearly Budget Tracker Dark Mode",
    "Monthly & Annual Budget Google Sheets, Budget Spreadsheet, Budget Planner, Budget Template, Expense Tracker, Finance Planner, Budget Tracker"
  ],
  "similar_products_urls": [
    "https://www.etsy.com/uk/listing/1768614476/family-and-couple-annual-budget-google?click_key=77077a8d3820b844694ba03cfd70844c926c1f5e%3A1768614476&click_sum=e75168f9&ref=landingpage-recs-811809-1&pro=1",
    "https://www.etsy.com/uk/listing/1782314239/family-annual-budget-spreadsheet-google?click_key=bce58ffa9ef768cf223c7a19341d3a26532bfef6%3A1782314239&click_sum=678c43e5&ref=landingpage-recs-811809-2&pro=1",
    "https://www.etsy.com/uk/listing/1528583605/family-annual-budget-excel-spreadsheet?click_key=f429f0c8a006f8a352a642b45edd5f8f464699f6%3A1528583605&click_sum=e68a2b15&ref=landingpage-recs-811809-3&pro=1&sts=1",
    "https://www.etsy.com/uk/listing/1539779389/family-annual-budget-excel-spreadsheet?click_key=63cf92062a6c13fd806f51211f37448b8c4a7b96%3A1539779389&click_sum=b4ebf0ae&ref=landingpage-recs-811809-4&pro=1&sts=1",
    "https://www.etsy.com/uk/listing/1583456949/family-annual-budget-monthly-budget?click_key=32316d78d7fcf3002c5396470747d4fd483d6910%3A1583456949&click_sum=af5dbf25&ref=landingpage-recs-811809-5&pro=1&sts=1",
    "https://www.etsy.com/uk/listing/1697048389/family-annual-budget-dark-mode-monthly?click_key=8486079bc87e9083131fccd8510fb723ff131168%3A1697048389&click_sum=f1931193&ref=landingpage-recs-811809-6&pro=1&sts=1",
    "https://www.etsy.com/uk/listing/1825101255/ultimate-annual-budget-planner-google?click_key=0e3f6bcd00f05607b585904f016bdfeeec2234de%3A1825101255&click_sum=b23a33d0&ref=internal-recs-811808-1&pro=1&sts=1",
    "https://www.etsy.com/uk/listing/1818452852/ultimate-annual-budget-template-excel?click_key=54b2b7a862b4506c2e2c56b02b85f83e5cd90825%3A1818452852&click_sum=4fbba41e&ref=internal-recs-811808-2&pro=1&sts=1",
    "https://www.etsy.com/uk/listing/1835246802/ultimate-annual-budget-spreadsheet?click_key=adfebe6c7fd1cfecd9fa6c751d7efb2943535d70%3A1835246802&click_sum=73308e1b&ref=internal-recs-811808-3&pro=1&sts=1",
    "https://www.etsy.com/uk/listing/1474373129/annual-budget-planner-monthly-budget?click_key=f6fd69831ab1be14862e166b780e04b81c92dfd8%3A1474373129&click_sum=19911ac2&ref=internal-recs-811808-4&pro=1&sts=1",
    "https://www.etsy.com/uk/listing/1826328945/ultimate-annual-budget-spreadsheet?click_key=655e4daaddcf2cc756b903fbc5591aa581aaadb1%3A1826328945&click_sum=506b1b2a&ref=internal-recs-811808-5&pro=1&sts=1",
    "https://www.etsy.com/uk/listing/1693529944/monthly-annual-budget-google-sheets?click_key=1cbf4f5b50dad4c8838f73f40f5c32bf96dab8c9%3A1693529944&click_sum=018a7ec1&ref=internal-recs-811808-6&pro=1&sts=1"
  ],
  "digital_download": true,
  "image": "https://i.etsystatic.com/46964289/r/il/3469ac/5844127337/il_794xN.5844127337_6n76.jpg",
  "related_searches": [
    "Budget Spreadsheet",
    "Thesheetcode",
    "Speardsheet",
    "Couples Budget",
    "Family Budget",
    "70/20/10 Budget Excel",
    "Spreadsheetable",
    "Budget Template",
    "Google Sheets Budget Planning",
    "Family and Couples Budget",
    "Google Docs Couples Budget",
    "Google Sheets Budget Dashboard",
    "Couples Budget Tracking",
    "Budget Tracker Google Sheet Abby",
    "Budget Spreadsheet for Multiple Accounts",
    "Goodnotes Spread Sheets",
    "50/30/10 Budget",
    "Couple Financial Plan Excel",
    "Couples Budget Planners",
    "Birthday Budget Spread Sheet",
    "Excel Budget Planner Couples",
    "Weekly Budget Excel Men",
    "Couple Life Planner Google Sheets"
  ],
  "date_listed": "23 Feb 2025",
  "number_of_favourties": 1559,
  "main_image": "https://i.etsystatic.com/46964289/r/il/3469ac/5844127337/il_794xN.5844127337_6n76.jpg",
  "last_24_hours": 20,
  "product_url": "https://www.etsy.com/uk/listing/1583875617/family-and-couple-annual-budget-google?click_key=cac5e902bc9a84971f59bffc3fd67c092b91d3ce%3A1583875617&click_sum=8962503b&ref=landingpage_similar_listing_bot-1&pro=1&sts=1&listing_id=1583875617&listing_slug=family-and-couple-annual-budget-google",
  "product_id": "1583875617"
}
```

### 2. Scrape Store Data
**Endpoint:** `/store`  
**Method:** POST  


#### Request Body
```json
{
    "url": "string",       // Required: Full Etsy store URL
    "proxy": boolean,      // Optional: Use proxy (default: false)
    "timeout": integer     // Optional: Timeout in seconds (default: 5, range: 1-300)
}
```

#### Response
```json
{
  "store_name": "PrioriDigitalStudio",
  "store_id": "PrioriDigitalStudio",
  "store_logo_url": "https://i.etsystatic.com/isla/3f6378/62555471/isla_180x180.62555471_iztpbgv2.jpg?version=0",
  "most_recent_product_urls": [
    "https://www.etsy.com/uk/listing/1807934295/ultimate-annual-budget-spreadsheet-excel?click_key=5a32e308f41c0ed868b1f77cd6aa7dfd71d0e714%3A1807934295&click_sum=f8cd2f20&ref=shop_home_feat_1&pro=1&sts=1",
    "https://www.etsy.com/uk/listing/1818452852/ultimate-annual-budget-template-excel?click_key=f4a4c1ce5887c976e234e5874dd30f4579fc2f9d%3A1818452852&click_sum=7ec42b97&ref=shop_home_feat_2&pro=1&sts=1",
    "https://www.etsy.com/uk/listing/1702251197/wedding-planner-spreadsheet-wedding?click_key=cf7bd4ca34ac918b9608cca9a3bc268593ee9764%3A1702251197&click_sum=4d3ede31&ref=shop_home_feat_3&pro=1&sts=1",
    "https://www.etsy.com/uk/listing/1631477863/small-business-bundle-bookkeeping?click_key=e9918e5c849e1d9f5cc5a4c4287a55518a439011%3A1631477863&click_sum=748e2b28&ref=shop_home_feat_4&pro=1&sts=1"
  ],
  "store_description": "50% on EVERYTHING!! Limited time only!!\n\nMore templates are under way, so make sure to stay on the loop by favoriting the shop!💻\nIf you have any questions, please contact us. We're more than happy to help✨\n\nNeed a custom order?\nFill in our simple form and get a quote within 24h : https://forms.gle/SE9cGGuKY7D5WjEW9\n\nJoin our thriving community on social media, where we share tips, behind the scene, exclusive promo code and captivating content to streamline your life and elevate your productivity.\n📱 Tiktok: https://www.tiktok.com/@prioridigitalstudio\n📱 Instagram: https://www.instagram.com/prioridigitalstudio/\nIn-depth YouTube Tutorial on how to efficiently use our spreadsheets: \n🎥 https://www.youtube.com/@Prioridigitalstudio",
  "store_sub_title": "Budget & Business Spreadsheets to empower your life!",
  "store_country": "Canada",
  "star_seller": true,
  "store_review_score": 4.8189,
  "store_last_updated": "11 Dec, 2024",
  "store_reviews": 5606,
  "store_admirers": 3738,
  "store_sales": 66358,
  "number_of_store_products": 126,
  "on_etsy_since": "2023",
  "facebook_url": "https://www.facebook.com/people/Priori-Digital-Studio/100092079784125/",
  "instagram_url": "https://www.instagram.com/prioridigitalstudio/",
  "pinterest_url": "https://www.pinterest.ca/prioridigitalstudio/",
  "tiktok_url": null,
  "welcome_to_our_shop_text": "Hey there! \nMy name is Anne-Lyse, I specialize in providing templates that cater to the needs of individuals and small business owners who are looking to enhance their lives, get organized, and grow their businesses. Our spreadsheet are designed to simplify your day-to-day tasks and help you achieve your goals. Whether you're looking to improve your productivity, streamline your workflow, or just get a better handle on your to-do list, we've got you covered. Follow us to stay up-to-date on our latest templates!\n\nThank you for supporting our small business!\nAnne-Lyse",
  "looking_for_more_urls": [
    "https://www.etsy.com/uk/market/cozy_bear",
    "https://www.etsy.com/uk/market/dead_can_dance_tee",
    "https://www.etsy.com/uk/listing/903824987/ashley-merwin-pink-latex-dress-a4-signed",
    "https://www.etsy.com/uk/market/plane_heart_png",
    "https://www.etsy.com/uk/market/toy_spaniel",
    "https://www.etsy.com/uk/market/sheffield_street",
    "https://www.etsy.com/uk/market/paraffin_free_tea_lights"
  ],
  "store_url": "https://www.etsy.com/uk/shop/PrioriDigitalStudio?ref=l2-about-shopname&from_page=listing"
}
```

### 3. Scrape Category Data
**Endpoint:** `/category`  
**Method:** POST  


#### Request Body
```json
{
    "url": "string",       // Required: Full Etsy category URL
    "proxy": boolean,      // Optional: Use proxy (default: false)
    "timeout": integer     // Optional: Timeout in seconds (default: 5, range: 1-300)
}
```

#### Response
```json
{
  "category_tree": "Paper & Party Supplies > Paper > Stationery > Design & Templates",
  "category_name": "Design & Templates",
  "products": [
    {
      "product_name": "Monthly & Annual Budget Google Sheets, Budget Spreadsheet, Budget Planner, Budget Template, Expense Tracker, Finance Planner, Budget Tracker",
      "product_url": "https://www.etsy.com/listing/1693529944/monthly-annual-budget-google-sheets?click_key=494b3da4d7c0b8a8a5cfdcf6659a650556ab2d6b%3A1693529944&click_sum=216d617a&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49635-1-1&pro=1&sts=1&dd=1",
      "product_id": "1693529944",
      "store_review_score": 4.9528,
      "store_reviews_number": 128,
      "star_seller": true,
      "store_name": "OneStopSpreadsheets",
      "store_url": "https://www.etsy.com/shop/OneStopSpreadsheets",
      "is_ad": true
    },
    {
      "product_name": "12 Month Journal Cover Page Printable | US Letter, A4 and A5 Size | Digital Download | Planner Covers | Bujo Title Coloring Page Printable",
      "product_url": "https://www.etsy.com/listing/1811159563/12-month-journal-cover-page-printable-us?click_key=dbd7bdf8b8d0c8b31619737e035316b789294781%3A1811159563&click_sum=55be4608&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49635-1-2&sts=1&dd=1",
      "product_id": "1811159563",
      "store_review_score": 4.9477,
      "store_reviews_number": 2242,
      "star_seller": true,
      "store_name": "ByBindi",
      "store_url": "https://www.etsy.com/shop/ByBindi",
      "is_ad": true
    },
    {
      "product_name": "Canva Pricing Guide for Wedding Photographers, Customizable Photography Package Pricing List Sheet Template, Editable Price Sheet Flyer",
      "product_url": "https://www.etsy.com/listing/1215839750/canva-pricing-guide-for-wedding?click_key=f3bec648a92d50b90481dced3fe919bd8743d336%3A1215839750&click_sum=52e41d19&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49635-1-3&dd=1",
      "product_id": "1215839750",
      "store_review_score": 2.6,
      "store_reviews_number": 38,
      "star_seller": false,
      "store_name": "ShaeelizabethDesigns",
      "store_url": "https://www.etsy.com/shop/ShaeelizabethDesigns",
      "is_ad": true
    },
    {
      "product_name": "Digital Planner, Goodnotes Planner, iPad Planner, Notability Planner, Dated Digital Planner, 2025 2026 Undated Planner",
      "product_url": "https://www.etsy.com/listing/1123882489/digital-planner-goodnotes-planner-ipad?click_key=a19921ff656b3b79189191ea81b3d96db1976ccd%3A1123882489&click_sum=f01b78c3&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49635-1-4&pro=1&sts=1&dd=1",
      "product_id": "1123882489",
      "store_review_score": 4.8135,
      "store_reviews_number": 11687,
      "star_seller": true,
      "store_name": "Plannerscollective",
      "store_url": "https://www.etsy.com/shop/Plannerscollective",
      "is_ad": true
    },
    {
      "product_name": "Canva Pro Lifetime Subscription | Canva Pro Lifetime Access | Canva Upgrade and Template Design | Instant Access | One-time payment",
      "product_url": "https://www.etsy.com/listing/1834608536/canva-pro-lifetime-subscription-o-canva?click_key=7f3efb8d66aea892499a9c4a2aeb628f38be9462%3A1834608536&click_sum=669a02d2&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-1&pro=1&dd=1&content_source=7f3efb8d66aea892499a9c4a2aeb628f38be9462%253A1834608536",
      "product_id": "1834608536",
      "store_review_score": 4.4337,
      "store_reviews_number": 83,
      "star_seller": false,
      "store_name": "mynoorr",
      "store_url": "https://www.etsy.com/shop/mynoorr",
      "is_ad": true
    },
    {
      "product_name": "Digital Products Bundle Ideal for Passive Income, Millions of DFY Content, Featuring Private Label Rights & Master Resell Rights (MRR) (PLR)",
      "product_url": "https://www.etsy.com/listing/1803456145/digital-products-bundle-ideal-for?click_key=d21bce50cfdb312460c883e48fc25fe64de67985%3A1803456145&click_sum=d53aa3d8&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-2&pro=1&dd=1&content_source=d21bce50cfdb312460c883e48fc25fe64de67985%253A1803456145",
      "product_id": "1803456145",
      "store_review_score": 4.6682,
      "store_reviews_number": 1061,
      "star_seller": false,
      "store_name": "SocialCeo",
      "store_url": "https://www.etsy.com/shop/SocialCeo",
      "is_ad": true
    },
    {
      "product_name": "All-in-One Digital Planner 2025, 2026, 2027, Digital Planner, Digital Journal, Digital Goodnotes Template, Weekly, Daily Planner, Notability",
      "product_url": "https://www.etsy.com/listing/1784469516/all-in-one-digital-planner-2025-2026?click_key=484683d5ab1b15c573c112b4e8312a68d39353db%3A1784469516&click_sum=80789bd3&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-3&pro=1&sts=1&dd=1&content_source=484683d5ab1b15c573c112b4e8312a68d39353db%253A1784469516",
      "product_id": "1784469516",
      "store_review_score": 4.7528,
      "store_reviews_number": 6073,
      "star_seller": true,
      "store_name": "phenixdigital",
      "store_url": "https://www.etsy.com/shop/phenixdigital",
      "is_ad": true
    },
    {
      "product_name": "Budget Planner Google Sheet Monthly Budget Spreadsheet Paycheck Budget Template Simple Weekly Financial Planner Beginners Biweekly Budgeting",
      "product_url": "https://www.etsy.com/listing/1619225413/budget-planner-google-sheet-monthly?click_key=e45ba31d6d1862e13840ade8ddac03748fd7a395%3A1619225413&click_sum=32552d36&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-4&pro=1&sts=1&dd=1&content_source=e45ba31d6d1862e13840ade8ddac03748fd7a395%253A1619225413",
      "product_id": "1619225413",
      "store_review_score": 4.8277,
      "store_reviews_number": 4910,
      "star_seller": true,
      "store_name": "ExclusiveDesignLab",
      "store_url": "https://www.etsy.com/shop/ExclusiveDesignLab",
      "is_ad": true
    },
    {
      "product_name": "Digital Planner Undated, iPad & Android Planner, GoodNotes Planner, Digital Calendar, Daily, Weekly, Monthly Journal, 2024 2025 iPad Planner",
      "product_url": "https://www.etsy.com/listing/1756165829/digital-planner-undated-ipad-android?click_key=a046d20133900a924fc698bdb39a16b01cfdd401%3A1756165829&click_sum=780891a8&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-5&pro=1&sts=1&dd=1&content_source=a046d20133900a924fc698bdb39a16b01cfdd401%253A1756165829",
      "product_id": "1756165829",
      "store_review_score": 4.7738,
      "store_reviews_number": 4895,
      "star_seller": true,
      "store_name": "BrighterPlans",
      "store_url": "https://www.etsy.com/shop/BrighterPlans",
      "is_ad": true
    },
    {
      "product_name": "20X Rug Mockup Bundle for Canva | Interior Design Templates for Rug Sellers | Customizable Rug Display | Digital Download",
      "product_url": "https://www.etsy.com/listing/1828324132/20x-rug-mockup-bundle-for-canva-interior?click_key=28cf58a71f31f675e8fea9a313d5a46626fbec2c%3A1828324132&click_sum=b3f4db4a&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-6&pro=1&sts=1&dd=1&content_source=28cf58a71f31f675e8fea9a313d5a46626fbec2c%253A1828324132",
      "product_id": "1828324132",
      "store_review_score": 4.8198,
      "store_reviews_number": 344,
      "star_seller": true,
      "store_name": "AzureSkyMockups",
      "store_url": "https://www.etsy.com/shop/AzureSkyMockups",
      "is_ad": true
    },
    {
      "product_name": "Project Management Template Multi Project Tracker Google Sheets Excel Gantt Chart Kanban Board Task Tracker Planner Small Business Dashboard",
      "product_url": "https://www.etsy.com/listing/1762779362/project-management-template-multi?click_key=b8506f955488f86ef0611621cbd754459961e525%3A1762779362&click_sum=40c2b6ce&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-7&pro=1&sts=1&dd=1&content_source=b8506f955488f86ef0611621cbd754459961e525%253A1762779362",
      "product_id": "1762779362",
      "store_review_score": 4.9026,
      "store_reviews_number": 161,
      "star_seller": true,
      "store_name": "StandardOperator",
      "store_url": "https://www.etsy.com/shop/StandardOperator",
      "is_ad": true
    },
    {
      "product_name": "Customizable Envelope Liner Templates: 18 Designs for Any Occasion 739",
      "product_url": "https://www.etsy.com/listing/1803175222/customizable-envelope-liner-templates-18?click_key=3a1fddc74ac9cc6532741be9ed5aeea85a137f5a%3A1803175222&click_sum=f4ba5a0a&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-8&pro=1&sts=1&dd=1&content_source=3a1fddc74ac9cc6532741be9ed5aeea85a137f5a%253A1803175222",
      "product_id": "1803175222",
      "store_review_score": 4.7479,
      "store_reviews_number": 1447,
      "star_seller": true,
      "store_name": "AtacanDesignStore",
      "store_url": "https://www.etsy.com/shop/AtacanDesignStore",
      "is_ad": true
    },
    {
      "product_name": "Gantt Chart Spreadsheet Small Business Project Planner Task Tracker Project AutomatedManagement Project Timeline Business Template Project",
      "product_url": "https://www.etsy.com/listing/1783987550/gantt-chart-spreadsheet-small-business?click_key=9d27ac8b3577abdf9f16bdfdb95835fe78f26c0a%3A1783987550&click_sum=aab071ca&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-9&pro=1&dd=1&content_source=9d27ac8b3577abdf9f16bdfdb95835fe78f26c0a%253A1783987550",
      "product_id": "1783987550",
      "store_review_score": 4.7189,
      "store_reviews_number": 1932,
      "star_seller": false,
      "store_name": "TheProductivePlans",
      "store_url": "https://www.etsy.com/shop/TheProductivePlans",
      "is_ad": true
    },
    {
      "product_name": "All In One Digital Planner 2025, 2026, 2027 Digital Planner, Digital Journal, Digital Goodnotes Template, Weekly, Daily Planner, Notability",
      "product_url": "https://www.etsy.com/listing/1845320608/all-in-one-digital-planner-2025-2026?click_key=6096ca38c117faa44cc4b8f02de0b8ecf777a43b%3A1845320608&click_sum=8011d64d&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-10&pro=1&dd=1&content_source=6096ca38c117faa44cc4b8f02de0b8ecf777a43b%253A1845320608",
      "product_id": "1845320608",
      "store_review_score": 4.7913,
      "store_reviews_number": 3169,
      "star_seller": false,
      "store_name": "BandGCollection",
      "store_url": "https://www.etsy.com/shop/BandGCollection",
      "is_ad": true
    },
    {
      "product_name": "7500+ Templates, Planners, Trackers, Journals And Calendars For Personal Use Or To Re-Brand And Resell With Master Label Rights MRR + PLR",
      "product_url": "https://www.etsy.com/listing/1760689760/7500-templates-planners-trackers?click_key=d0dc43fdf05721b67ec44f3d6eccbb4f2ec3e871%3A1760689760&click_sum=fc4d05b6&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-11&pro=1&dd=1&content_source=d0dc43fdf05721b67ec44f3d6eccbb4f2ec3e871%253A1760689760",
      "product_id": "1760689760",
      "store_review_score": 4.6682,
      "store_reviews_number": 1061,
      "star_seller": false,
      "store_name": "SocialCeo",
      "store_url": "https://www.etsy.com/shop/SocialCeo",
      "is_ad": true
    },
    {
      "product_name": "Budget Planner Excel Monthly Budget Spreadsheet Paycheck Budget Tracker Excel Weekly Budget Template BiWeekly Budget Debt",
      "product_url": "https://www.etsy.com/listing/1681362279/budget-planner-excel-monthly-budget?click_key=28d795bb2481e77a5ea2a5d1beffb71c8c45ab98%3A1681362279&click_sum=920a1113&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-12&pro=1&sts=1&dd=1&content_source=28d795bb2481e77a5ea2a5d1beffb71c8c45ab98%253A1681362279",
      "product_id": "1681362279",
      "store_review_score": 4.7694,
      "store_reviews_number": 689,
      "star_seller": true,
      "store_name": "Crafted2Plan",
      "store_url": "https://www.etsy.com/shop/Crafted2Plan",
      "is_ad": true
    },
    {
      "product_name": "Small Business Easy Bookkeeping Spreadsheet Profit And Loss Excel Google Sheets Sales Tax Tracker Accounting Template Profit Tracker Invoice",
      "product_url": "https://www.etsy.com/listing/1734053917/small-business-easy-bookkeeping?click_key=20a37bf6d9746f792a5c0379f3606fc1f3fa39f6%3A1734053917&click_sum=634c37bd&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49635-1-5&pro=1&sts=1&dd=1",
      "product_id": "1734053917",
      "store_review_score": 4.8166,
      "store_reviews_number": 1360,
      "star_seller": true,
      "store_name": "TheSheetCode",
      "store_url": "https://www.etsy.com/shop/TheSheetCode",
      "is_ad": true
    },
    {
      "product_name": "reMarkable 2 / Paper Pro - Digital Planner Bundle 2025 + 2026 Ultimate Collection Pack, reMarkable Templates, Planners, Journals",
      "product_url": "https://www.etsy.com/listing/1415127322/remarkable-2-paper-pro-digital-planner?click_key=95153766efdff37dccae84c8603978b55d7713bc%3A1415127322&click_sum=9f50132f&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49635-1-6&pro=1&dd=1",
      "product_id": "1415127322",
      "store_review_score": 4.6424,
      "store_reviews_number": 5732,
      "star_seller": false,
      "store_name": "EvoPrintables",
      "store_url": "https://www.etsy.com/shop/EvoPrintables",
      "is_ad": true
    },
    {
      "product_name": "Coloring Book Bundle for reMarkable Paper Pro, Eink Adult Coloring Book, Calming Coloring Book for reMarkable Paper Pro,  eInk Coloring Book",
      "product_url": "https://www.etsy.com/listing/1834169651/coloring-book-bundle-for-remarkable?click_key=3b46620657087b03eb36319028eb57c9c389bd15%3A1834169651&click_sum=db82722f&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49635-1-7&pro=1&sts=1&dd=1",
      "product_id": "1834169651",
      "store_review_score": 4.8781,
      "store_reviews_number": 361,
      "star_seller": true,
      "store_name": "StudioPiksels",
      "store_url": "https://www.etsy.com/shop/StudioPiksels",
      "is_ad": true
    },
    {
      "product_name": "300 pcs - Transparent Business Card, Clear Boutique Card, Acrylic Frosty plastic, Translucent Plastic Cards,  Special Business Card",
      "product_url": "https://www.etsy.com/listing/1778380580/300-pcs-transparent-business-card-clear?click_key=9d4f3483d0be36b8f9d5a0b511dcfa802a1402e1%3A1778380580&click_sum=405af777&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49635-1-8",
      "product_id": "1778380580",
      "store_review_score": 4.7586,
      "store_reviews_number": 62,
      "star_seller": false,
      "store_name": "YalcinPrintingHouse",
      "store_url": "https://www.etsy.com/shop/YalcinPrintingHouse",
      "is_ad": true
    },
    {
      "product_name": "6000+ Aesthetic Faceless Videos, MMR & PLR Resell - Faceless Reels, Faceless Marketing",
      "product_url": "https://www.etsy.com/listing/1807112297/6000-aesthetic-faceless-videos-mmr-plr?click_key=d8e2fe5b86abd41b0406a9be632db98649638a6d%3A1807112297&click_sum=5002f591&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-13&bes=1&dd=1&content_source=d8e2fe5b86abd41b0406a9be632db98649638a6d%253A1807112297",
      "product_id": "1807112297",
      "store_review_score": 4.4828,
      "store_reviews_number": 36,
      "star_seller": false,
      "store_name": "MussaStudios",
      "store_url": "https://www.etsy.com/shop/MussaStudios",
      "is_ad": true
    },
    {
      "product_name": "40-Template Bundle Pack Editable in Canva: Custom Rap Tee Bootleg Designs | DIY Bootleg Templates, 90s Shirt, Face Photo Birthday Tee",
      "product_url": "https://www.etsy.com/listing/1847438866/40-template-bundle-pack-editable-in?click_key=88327d6b5b9429976573a59d265f14760dc80339%3A1847438866&click_sum=24068809&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-14&bes=1&dd=1&content_source=88327d6b5b9429976573a59d265f14760dc80339%253A1847438866",
      "product_id": "1847438866",
      "store_review_score": 3.8571,
      "store_reviews_number": 14,
      "star_seller": false,
      "store_name": "JusMystic",
      "store_url": "https://www.etsy.com/shop/JusMystic",
      "is_ad": true
    },
    {
      "product_name": "All-in-One Digital Planner Undated, iPad & Android Planner, Digital Calendar, GoodNotes Template, Daily Weekly Monthly Journal for 2025 2026",
      "product_url": "https://www.etsy.com/listing/1834109154/all-in-one-digital-planner-undated-ipad?click_key=c27e871fa07cf3bd5d8b0c9f106826295953e307%3A1834109154&click_sum=919d160f&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-15&pro=1&sts=1&dd=1&content_source=c27e871fa07cf3bd5d8b0c9f106826295953e307%253A1834109154",
      "product_id": "1834109154",
      "store_review_score": 4.7738,
      "store_reviews_number": 4895,
      "star_seller": true,
      "store_name": "BrighterPlans",
      "store_url": "https://www.etsy.com/shop/BrighterPlans",
      "is_ad": true
    },
    {
      "product_name": "Pricing Calculator Spreadsheet | Small Business Template | Product Pricing Calculator | Pricing Worksheet | Price Guide | Profit Calculator",
      "product_url": "https://www.etsy.com/listing/1670480275/pricing-calculator-spreadsheet-small?click_key=a27415b0de9408d3518733064fbaf561973208e9%3A1670480275&click_sum=b4680282&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-16&pro=1&sts=1&dd=1&content_source=a27415b0de9408d3518733064fbaf561973208e9%253A1670480275",
      "product_id": "1670480275",
      "store_review_score": 4.7814,
      "store_reviews_number": 7163,
      "star_seller": true,
      "store_name": "SimplyOrganizedPro",
      "store_url": "https://www.etsy.com/shop/SimplyOrganizedPro",
      "is_ad": true
    },
    {
      "product_name": "University Planner Spreadsheet Student Template Google Sheets Student Planner College Assignment Tracker Task Class Timetable Study Planner",
      "product_url": "https://www.etsy.com/listing/1794733998/university-planner-spreadsheet-student?click_key=71c57c4a86d28fa23362bc1ebbfcf13d4e32e1a5%3A1794733998&click_sum=b9badc12&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-17&pro=1&dd=1&content_source=71c57c4a86d28fa23362bc1ebbfcf13d4e32e1a5%253A1794733998",
      "product_id": "1794733998",
      "store_review_score": 4.7189,
      "store_reviews_number": 1932,
      "star_seller": false,
      "store_name": "TheProductivePlans",
      "store_url": "https://www.etsy.com/shop/TheProductivePlans",
      "is_ad": true
    },
    {
      "product_name": "600+ Sublimation Design Template |Jersey TShirt Premium Design For Adobe Illustrator | Ai",
      "product_url": "https://www.etsy.com/listing/1574355257/600-sublimation-design-template-jersey?click_key=d301ea3bbdafe43ea75a9effb3319bbc33bd76de%3A1574355257&click_sum=93fbd9b6&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-18&bes=1&dd=1&content_source=d301ea3bbdafe43ea75a9effb3319bbc33bd76de%253A1574355257",
      "product_id": "1574355257",
      "store_review_score": 4.2121,
      "store_reviews_number": 100,
      "star_seller": false,
      "store_name": "BusinesTemplate",
      "store_url": "https://www.etsy.com/shop/BusinesTemplate",
      "is_ad": true
    },
    {
      "product_name": "Notion Template - ALL IN ONE | Life Notion Planner Dashboard | Dark Mode Notion Ultimate Life Planner | Personal | Digital Planner Aesthetic",
      "product_url": "https://www.etsy.com/listing/1707999067/notion-template-all-in-one-life-notion?click_key=506d7cc07d2865cfc87bbc02ba15521b1445ead3%3A1707999067&click_sum=7128b113&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-19&pro=1&dd=1&content_source=506d7cc07d2865cfc87bbc02ba15521b1445ead3%253A1707999067",
      "product_id": "1707999067",
      "store_review_score": 4.7544,
      "store_reviews_number": 705,
      "star_seller": false,
      "store_name": "PIanifest",
      "store_url": "https://www.etsy.com/shop/PIanifest",
      "is_ad": true
    },
    {
      "product_name": "Flower print 10",
      "product_url": "https://www.etsy.com/listing/1615118676/flower-print-10?click_key=bd9c6996d9ea61167219c759db27f70e3732e37a%3A1615118676&click_sum=f05bfd92&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-20&bes=1&sts=1&dd=1&content_source=bd9c6996d9ea61167219c759db27f70e3732e37a%253A1615118676",
      "product_id": "1615118676",
      "store_review_score": 4.755,
      "store_reviews_number": 544,
      "star_seller": true,
      "store_name": "PrintaciousCo",
      "store_url": "https://www.etsy.com/shop/PrintaciousCo",
      "is_ad": true
    },
    {
      "product_name": "7 Size Wax Crayon Box Template Canva Crayon Box Template Wax Box Template Color Box Template Pencil Color Box Template Wax Crayon Box SVG",
      "product_url": "https://www.etsy.com/listing/1852678206/7-size-wax-crayon-box-template-canva?click_key=c3d21d308eca611040410e8b396e02f0f89a06b5%3A1852678206&click_sum=fbab27fe&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-21&pro=1&dd=1&content_source=c3d21d308eca611040410e8b396e02f0f89a06b5%253A1852678206",
      "product_id": "1852678206",
      "store_review_score": 4.7512,
      "store_reviews_number": 2678,
      "star_seller": false,
      "store_name": "OrispotMockups",
      "store_url": "https://www.etsy.com/shop/OrispotMockups",
      "is_ad": true
    },
    {
      "product_name": "50+ Project Management Templates in Excel and PowerPoint",
      "product_url": "https://www.etsy.com/listing/1199800561/50-project-management-templates-in-excel?click_key=e7fc9a5765e75eedf3158f6d6adb9996234d74b7%3A1199800561&click_sum=77204353&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-22&bes=1&sts=1&dd=1&content_source=e7fc9a5765e75eedf3158f6d6adb9996234d74b7%253A1199800561",
      "product_id": "1199800561",
      "store_review_score": 4.7637,
      "store_reviews_number": 427,
      "star_seller": true,
      "store_name": "ProjectHelper",
      "store_url": "https://www.etsy.com/shop/ProjectHelper",
      "is_ad": true
    },
    {
      "product_name": "Digital Notebook with Tabs, GoodNotes Notebook, Digital Journal, Student Notebook, Note Templates, Digital Note Paper, Note Taking Template",
      "product_url": "https://www.etsy.com/listing/1832761891/digital-notebook-with-tabs-goodnotes?click_key=1542f2ec77d066f800c1dd58dbce8686a2cec486%3A1832761891&click_sum=d76194fd&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-23&pro=1&sts=1&dd=1&content_source=1542f2ec77d066f800c1dd58dbce8686a2cec486%253A1832761891",
      "product_id": "1832761891",
      "store_review_score": 4.7738,
      "store_reviews_number": 4895,
      "star_seller": true,
      "store_name": "BrighterPlans",
      "store_url": "https://www.etsy.com/shop/BrighterPlans",
      "is_ad": true
    },
    {
      "product_name": "Elementor Pro 3.27.4 - Latest Version | Elementor Page Builder | Premium Wordpress Plugin | GPL License | Lifetime Updates | Free Support",
      "product_url": "https://www.etsy.com/listing/1833445203/elementor-pro-3274-latest-version?click_key=ad44d3bd6b430b2c5c261e28d9e61a2125817227%3A1833445203&click_sum=e15caf46&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-24&bes=1&dd=1&content_source=ad44d3bd6b430b2c5c261e28d9e61a2125817227%253A1833445203",
      "product_id": "1833445203",
      "store_review_score": 5,
      "store_reviews_number": 23,
      "star_seller": false,
      "store_name": "WPMakersMarket",
      "store_url": "https://www.etsy.com/shop/WPMakersMarket",
      "is_ad": true
    },
    {
      "product_name": "I Will Create Custom Logo Design for your Business, Logo Creation, Logo Design Custom For Business, Professional Logo Maker Photography Logo",
      "product_url": "https://www.etsy.com/listing/1840326712/i-will-create-custom-logo-design-for?click_key=569bcf9f498bcd46aef2216c24e43b732f4693ea%3A1840326712&click_sum=b53fa257&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49635-1-9&pro=1&frs=1",
      "product_id": "1840326712",
      "store_review_score": 5,
      "store_reviews_number": 1,
      "star_seller": false,
      "store_name": "PureGraphicsStudio",
      "store_url": "https://www.etsy.com/shop/PureGraphicsStudio",
      "is_ad": true
    },
    {
      "product_name": "Editable Minnie Birthday Invitation Inspired Invite Any Age Digital 5x7 Mouse Pink Black Polka Dot Kids Girls Minnie Party Minnie Invite",
      "product_url": "https://www.etsy.com/listing/1810518952/editable-minnie-birthday-invitation?click_key=84c572035c4bad63a28fd2b2f8c0f3281090fc5a%3A1810518952&click_sum=0027fac1&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49635-1-10&pro=1&sts=1&dd=1",
      "product_id": "1810518952",
      "store_review_score": 4.9056,
      "store_reviews_number": 1703,
      "star_seller": true,
      "store_name": "luzdesignsStoree",
      "store_url": "https://www.etsy.com/shop/luzdesignsStoree",
      "is_ad": true
    },
    {
      "product_name": "Wedding Coffee Table Photo Book Template Editable In Canva, Modern Editorial Magazine Album, Couples Story Scrapbook, Anniversary Gift | 01",
      "product_url": "https://www.etsy.com/listing/1681434815/wedding-coffee-table-photo-book-template?click_key=9178274ee57aafd278d3cee85025f0b0de10b379%3A1681434815&click_sum=148617f2&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49635-1-11&pro=1&sts=1&dd=1",
      "product_id": "1681434815",
      "store_review_score": 4.978,
      "store_reviews_number": 250,
      "star_seller": true,
      "store_name": "WhiteTint",
      "store_url": "https://www.etsy.com/shop/WhiteTint",
      "is_ad": true
    },
    {
      "product_name": "April Real Estate Spring Social Media Spring Real Estate Marketing Social Media Spring Real Estate Social Media Templates",
      "product_url": "https://www.etsy.com/listing/1873289319/april-real-estate-spring-social-media?click_key=aa9103ceaa3542538c56050843d922f3804cf9bf%3A1873289319&click_sum=ced86c25&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49635-1-12&pro=1&sts=1&dd=1",
      "product_id": "1873289319",
      "store_review_score": 4.9504,
      "store_reviews_number": 141,
      "star_seller": true,
      "store_name": "RealtyEssentialsCo",
      "store_url": "https://www.etsy.com/shop/RealtyEssentialsCo",
      "is_ad": true
    },
    {
      "product_name": "Budget Planner Google Sheets, Monthly Budget Spreadsheet, Paycheck Budget, Expense Tracker, Weekly Biweekly Annual Financial Planner",
      "product_url": "https://www.etsy.com/listing/1850948376/budget-planner-google-sheets-monthly?click_key=6c0e4d0fe072cb37f763a1d9c747e2c87e58ad02%3A1850948376&click_sum=64eea916&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-25&pro=1&dd=1&content_source=6c0e4d0fe072cb37f763a1d9c747e2c87e58ad02%253A1850948376",
      "product_id": "1850948376",
      "store_review_score": 5,
      "store_reviews_number": 5,
      "star_seller": false,
      "store_name": "MarethicDigital",
      "store_url": "https://www.etsy.com/shop/MarethicDigital",
      "is_ad": true
    },
    {
      "product_name": "Editable Ebook Template, Small Business Canva Ebook Template, A4 and US Letter Size, Digital Lead Magnet, Mini Training Guide Book",
      "product_url": "https://www.etsy.com/listing/1520815521/editable-ebook-template-small-business?click_key=044a8e783ff8105d64acf25b5b448037d5a6204a%3A1520815521&click_sum=f7641c6b&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-26&bes=1&sts=1&dd=1&content_source=044a8e783ff8105d64acf25b5b448037d5a6204a%253A1520815521",
      "product_id": "1520815521",
      "store_review_score": 4.9554,
      "store_reviews_number": 1821,
      "star_seller": true,
      "store_name": "DigiTemplatables",
      "store_url": "https://www.etsy.com/shop/DigiTemplatables",
      "is_ad": true
    },
    {
      "product_name": "Resume Template Canva with Cover Letter, 1 Page Cv Template Canva + 2 page resume for Canva, Minimalist Resume Professional Cv with photo",
      "product_url": "https://www.etsy.com/listing/1464435354/resume-template-canva-with-cover-letter?click_key=9a8c5fba99958a9cabc05a119098afb0ddc97621%3A1464435354&click_sum=afae4ed6&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-27&pro=1&sts=1&dd=1&content_source=9a8c5fba99958a9cabc05a119098afb0ddc97621%253A1464435354",
      "product_id": "1464435354",
      "store_review_score": 4.7856,
      "store_reviews_number": 2676,
      "star_seller": true,
      "store_name": "WinkyWin",
      "store_url": "https://www.etsy.com/shop/WinkyWin",
      "is_ad": true
    },
    {
      "product_name": "Excel Client Tracker | CRM Dashboard, Small Business Template, Excel Business Tracker, Business Planner Business Spreadsheet, Lead Tracker",
      "product_url": "https://www.etsy.com/listing/1787290835/excel-client-tracker-crm-dashboard-small?click_key=65f8283ab7a2ad8e37d045e8097c96352e2e8e6d%3A1787290835&click_sum=d0d18318&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-28&bes=1&sts=1&dd=1&content_source=65f8283ab7a2ad8e37d045e8097c96352e2e8e6d%253A1787290835",
      "product_id": "1787290835",
      "store_review_score": 4.7993,
      "store_reviews_number": 2604,
      "star_seller": true,
      "store_name": "JeeraDigitalDesigns",
      "store_url": "https://www.etsy.com/shop/JeeraDigitalDesigns",
      "is_ad": true
    },
    {
      "product_name": "50 Retro Frame Mockups Bundle Mid Century Modern Templates Vintage Art Pack PSD Files Collection for Prints & Posters Photoshop Art Display",
      "product_url": "https://www.etsy.com/listing/1799682501/50-retro-frame-mockups-bundle-mid?click_key=293b5a0a5c9185d803e4ecab111a02a8b65f0397%3A1799682501&click_sum=5ad8208c&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-29&pro=1&sts=1&dd=1&content_source=293b5a0a5c9185d803e4ecab111a02a8b65f0397%253A1799682501",
      "product_id": "1799682501",
      "store_review_score": 4.9456,
      "store_reviews_number": 386,
      "star_seller": true,
      "store_name": "SunnyMockupStore",
      "store_url": "https://www.etsy.com/shop/SunnyMockupStore",
      "is_ad": true
    },
    {
      "product_name": "Bookkeeping Spreadsheet Income, Expense, Profit and Loss Tracker Easy Google Sheets Accounting Financial Planner Template",
      "product_url": "https://www.etsy.com/listing/1806121814/bookkeeping-spreadsheet-income-expense?click_key=390f963ea9f4d34d45a5525769fa36f6aab29d5c%3A1806121814&click_sum=1b8a7b20&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-30&pro=1&dd=1&content_source=390f963ea9f4d34d45a5525769fa36f6aab29d5c%253A1806121814",
      "product_id": "1806121814",
      "store_review_score": 5,
      "store_reviews_number": 5,
      "star_seller": false,
      "store_name": "MarethicDigital",
      "store_url": "https://www.etsy.com/shop/MarethicDigital",
      "is_ad": true
    },
    {
      "product_name": "TOEFL ITP Complete Study Guide | Notion Template for Efficient Study",
      "product_url": "https://www.etsy.com/listing/1819887224/toefl-itp-complete-study-guide-notion?click_key=599d1dc9258ffaf710e639efbd6c13c3461b14ac%3A1819887224&click_sum=72dcf767&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-31&pro=1&dd=1&content_source=599d1dc9258ffaf710e639efbd6c13c3461b14ac%253A1819887224",
      "product_id": "1819887224",
      "store_review_score": 4.8333,
      "store_reviews_number": 6,
      "star_seller": false,
      "store_name": "MrsNotion",
      "store_url": "https://www.etsy.com/shop/MrsNotion",
      "is_ad": true
    },
    {
      "product_name": "Ultimate Annual Budget Spreadsheet Excel Google Sheets Budget Template Monthly Budget Tracker Financial Planner Bill Tracker Debt Tracker",
      "product_url": "https://www.etsy.com/listing/1807934295/ultimate-annual-budget-spreadsheet-excel?click_key=3c32735a3a54802b415670338e22c6b2e64a6150%3A1807934295&click_sum=81ee41e7&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-32&pro=1&sts=1&dd=1&content_source=3c32735a3a54802b415670338e22c6b2e64a6150%253A1807934295",
      "product_id": "1807934295",
      "store_review_score": 4.8189,
      "store_reviews_number": 5606,
      "star_seller": true,
      "store_name": "PrioriDigitalStudio",
      "store_url": "https://www.etsy.com/shop/PrioriDigitalStudio",
      "is_ad": true
    },
    {
      "product_name": "900+ Faceless Men Reels, Dark Aesthetic Videos for Men, Faceless Video Clips, MRR & PLR Included, Trendy Aesthetic Content",
      "product_url": "https://www.etsy.com/listing/1844020161/900-faceless-men-reels-dark-aesthetic?click_key=69d270a0a5a371b250edfa155bb21ebc690215d1%3A1844020161&click_sum=710ffc99&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-33&pro=1&dd=1&content_source=69d270a0a5a371b250edfa155bb21ebc690215d1%253A1844020161",
      "product_id": "1844020161",
      "store_review_score": 4.5455,
      "store_reviews_number": 231,
      "star_seller": false,
      "store_name": "PixelNectar",
      "store_url": "https://www.etsy.com/shop/PixelNectar",
      "is_ad": true
    },
    {
      "product_name": "50 Sets Dashboard Excel Template All In One Ultimate Collection | Fully Excel Editable | Various Categories",
      "product_url": "https://www.etsy.com/listing/1810076151/50-sets-dashboard-excel-template-all-in?click_key=e17111340bf991c2b378cb81c7017f4192752a58%3A1810076151&click_sum=96451f41&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-34&pro=1&sts=1&dd=1&content_source=e17111340bf991c2b378cb81c7017f4192752a58%253A1810076151",
      "product_id": "1810076151",
      "store_review_score": 5,
      "store_reviews_number": 5,
      "star_seller": true,
      "store_name": "ExcelEaseTemplates",
      "store_url": "https://www.etsy.com/shop/ExcelEaseTemplates",
      "is_ad": true
    },
    {
      "product_name": "OneNote Planner 2025 2026 Digital OneNote Templates Hyperlinked Planner Daily Weekly Planner Organization Planner Professional OneNote 2025",
      "product_url": "https://www.etsy.com/listing/1864489467/onenote-planner-2025-2026-digital?click_key=babc56f2a96299d28f241929c5cd214bd3ce4d1e%3A1864489467&click_sum=f437ee98&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-35&pro=1&sts=1&dd=1&content_source=babc56f2a96299d28f241929c5cd214bd3ce4d1e%253A1864489467",
      "product_id": "1864489467",
      "store_review_score": 4.8189,
      "store_reviews_number": 5606,
      "star_seller": true,
      "store_name": "PrioriDigitalStudio",
      "store_url": "https://www.etsy.com/shop/PrioriDigitalStudio",
      "is_ad": true
    },
    {
      "product_name": "Descriptive grade kindergarten",
      "product_url": "https://www.etsy.com/listing/1843331860/descriptive-grade-kindergarten?click_key=79523d89cd824466d04792c6354a51576f4520cc%3A1843331860&click_sum=920249cc&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-36&dd=1&content_source=79523d89cd824466d04792c6354a51576f4520cc%253A1843331860",
      "product_id": "1843331860",
      "store_review_score": 4,
      "store_reviews_number": 8,
      "star_seller": false,
      "store_name": "MartaMurawska",
      "store_url": "https://www.etsy.com/shop/MartaMurawska",
      "is_ad": true
    },
    {
      "product_name": "Digital Planner 2025 2026 Undated Digital Planners Goodnotes Planner iPad Planner Daily Planner Weekly Planner Digital Journal ADHD Planner",
      "product_url": "https://www.etsy.com/listing/661944197/digital-planner-2025-2026-undated?click_key=ce903d81dc98edb016fd81bb4799e300e58b8b64%3A661944197&click_sum=b23efb61&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49635-1-13&pro=1&sts=1&dd=1",
      "product_id": "661944197",
      "store_review_score": 4.8694,
      "store_reviews_number": 28294,
      "star_seller": true,
      "store_name": "HappyDownloads",
      "store_url": "https://www.etsy.com/shop/HappyDownloads",
      "is_ad": true
    },
    {
      "product_name": "Custom Branding Kit| Brand kit| Business Logo | Business Branding Kit| Custom Logo | Business Card Design | Brand Design",
      "product_url": "https://www.etsy.com/listing/1749858217/custom-branding-kit-brand-kit-business?click_key=d07399b50ef25cccf466cf52d2af4d2d36df2caa%3A1749858217&click_sum=2e56e5c8&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49635-1-14&dd=1",
      "product_id": "1749858217",
      "store_review_score": 4.6923,
      "store_reviews_number": 60,
      "star_seller": false,
      "store_name": "BeSeenBranding",
      "store_url": "https://www.etsy.com/shop/BeSeenBranding",
      "is_ad": true
    },
    {
      "product_name": "A5/A6/B6/5x7 Five greeting cards mockup",
      "product_url": "https://www.etsy.com/listing/1545244582/a5a6b65x7-five-greeting-cards-mockup?click_key=520347f022e1ab45a87b49a24fce67d9f481fb28%3A1545244582&click_sum=e47365cd&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49635-1-15&sts=1&dd=1",
      "product_id": "1545244582",
      "store_review_score": 4.958,
      "store_reviews_number": 263,
      "star_seller": true,
      "store_name": "MCKPME",
      "store_url": "https://www.etsy.com/shop/MCKPME",
      "is_ad": true
    },
    {
      "product_name": "Airbnb Welcome Book Template, Editable Canva Guidebook for Vacation Rental, Cabin, Cottage, Lake House, or Mountain Stay, Digital guest book",
      "product_url": "https://www.etsy.com/listing/1859324729/airbnb-welcome-book-template-editable?click_key=568f93b71d10924f9e978ecd5d7fcf48a05197b9%3A1859324729&click_sum=c4ab7329&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49635-1-16&pro=1&sts=1&dd=1",
      "product_id": "1859324729",
      "store_review_score": 4.8772,
      "store_reviews_number": 57,
      "star_seller": true,
      "store_name": "TheRightTemplateShop",
      "store_url": "https://www.etsy.com/shop/TheRightTemplateShop",
      "is_ad": true
    },
    {
      "product_name": "Gold Nikkah Contract Template, Digital Nikkah Certificate, Editable Nikkah Contract, Muslim Wedding Certificate, Islamic Nikah Nama, A3, A4",
      "product_url": "https://www.etsy.com/listing/1858006091/gold-nikkah-contract-template-digital?click_key=0429196d1077f8b05d224233c46e255cedc69cd0%3A1858006091&click_sum=1df1d1c8&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-37&bes=1&sts=1&dd=1&content_source=0429196d1077f8b05d224233c46e255cedc69cd0%253A1858006091",
      "product_id": "1858006091",
      "store_review_score": 4.8476,
      "store_reviews_number": 223,
      "star_seller": true,
      "store_name": "SheenPrintablesShop",
      "store_url": "https://www.etsy.com/shop/SheenPrintablesShop",
      "is_ad": true
    },
    {
      "product_name": "Boox Note Air4 C 2025 2026 Planner, Premier Designs and Minimalistic Layouts, Offering Excellent Templates for Your Digital Planning Needs",
      "product_url": "https://www.etsy.com/listing/1848233327/boox-note-air4-c-2025-2026-planner?click_key=385eaa9e032fc181222d81fd6be94dcf456c54ab%3A1848233327&click_sum=09a823c8&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-38&pro=1&dd=1&content_source=385eaa9e032fc181222d81fd6be94dcf456c54ab%253A1848233327",
      "product_id": "1848233327",
      "store_review_score": 4.5563,
      "store_reviews_number": 405,
      "star_seller": false,
      "store_name": "FocusFinesse",
      "store_url": "https://www.etsy.com/shop/FocusFinesse",
      "is_ad": true
    },
    {
      "product_name": "Modern apartment application couple Canva template beige short profile cover letter professional application template house purchase German template mint",
      "product_url": "https://www.etsy.com/listing/1760275238/modern-apartment-application-couple?click_key=765d045defc624406a0e98968ca76cd3dd0f4e12%3A1760275238&click_sum=2e20ca01&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-39&pro=1&dd=1&content_source=765d045defc624406a0e98968ca76cd3dd0f4e12%253A1760275238",
      "product_id": "1760275238",
      "store_review_score": 4.5625,
      "store_reviews_number": 108,
      "star_seller": false,
      "store_name": "DigitalAestheticCD",
      "store_url": "https://www.etsy.com/shop/DigitalAestheticCD",
      "is_ad": true
    },
    {
      "product_name": "I will create custom logo design, logo, photography logo, personalized gift, professional logo design, custom logo for your business",
      "product_url": "https://www.etsy.com/listing/1768219317/i-will-create-custom-logo-design-logo?click_key=036840708f9d05f595e0baee3df3ce28ef424a3c%3A1768219317&click_sum=26a63486&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-40&pro=1&frs=1&content_source=036840708f9d05f595e0baee3df3ce28ef424a3c%253A1768219317",
      "product_id": "1768219317",
      "store_review_score": 4.7,
      "store_reviews_number": 50,
      "star_seller": false,
      "store_name": "TulipDigi",
      "store_url": "https://www.etsy.com/shop/TulipDigi",
      "is_ad": true
    },
    {
      "product_name": "All In One Digital Planner 2025 2026 2027, Digital Planner, Digital Journal, Digital Goodnotes Template, Weekly, Daily Planner, Monthly plan",
      "product_url": "https://www.etsy.com/listing/1796209780/all-in-one-digital-planner-2025-2026?click_key=9d196200183fd90f501b86dccdfefc16b2e1594d%3A1796209780&click_sum=dd3ab55e&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-41&pro=1&dd=1&content_source=9d196200183fd90f501b86dccdfefc16b2e1594d%253A1796209780",
      "product_id": "1796209780",
      "store_review_score": 4.7261,
      "store_reviews_number": 1933,
      "star_seller": false,
      "store_name": "PrintMagicStudioX",
      "store_url": "https://www.etsy.com/shop/PrintMagicStudioX",
      "is_ad": true
    },
    {
      "product_name": "Budget Planner for Google Sheets, Monthly Budget Spreadsheet, Paycheck Budget Tracker, Weekly Budget Template, Biweekly Budget, Budgeting",
      "product_url": "https://www.etsy.com/listing/1473595073/budget-planner-for-google-sheets-monthly?click_key=18b3646823192df1a0dbb3491b27ddfc253df7c9%3A1473595073&click_sum=00aa3c19&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-42&pro=1&sts=1&dd=1&content_source=18b3646823192df1a0dbb3491b27ddfc253df7c9%253A1473595073",
      "product_id": "1473595073",
      "store_review_score": 4.8787,
      "store_reviews_number": 9281,
      "star_seller": true,
      "store_name": "HayeCreativesCo",
      "store_url": "https://www.etsy.com/shop/HayeCreativesCo",
      "is_ad": true
    },
    {
      "product_name": "Easy Bookkeeping Template | Small Business Finance Spreadsheet | Income and Expense Tracker | Profit and Loss | Accounting Google Sheets",
      "product_url": "https://www.etsy.com/listing/1463262520/easy-bookkeeping-template-small-business?click_key=377679988e1cc56187b6a296ea51d49720cdb90f%3A1463262520&click_sum=aee7d200&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-43&pro=1&sts=1&dd=1&content_source=377679988e1cc56187b6a296ea51d49720cdb90f%253A1463262520",
      "product_id": "1463262520",
      "store_review_score": 4.7814,
      "store_reviews_number": 7163,
      "star_seller": true,
      "store_name": "SimplyOrganizedPro",
      "store_url": "https://www.etsy.com/shop/SimplyOrganizedPro",
      "is_ad": true
    },
    {
      "product_name": "Budget Planner Excel Google Sheets Budget Spreadsheet Monthly Paycheck Budget Tracker Weekly Expense Budgeting Finance Spreadsheet Dark Mode",
      "product_url": "https://www.etsy.com/listing/1807214506/budget-planner-excel-google-sheets?click_key=aa27264b64bda01077c2b87d894718c54c342cb2%3A1807214506&click_sum=547b4425&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-44&pro=1&sts=1&dd=1&content_source=aa27264b64bda01077c2b87d894718c54c342cb2%253A1807214506",
      "product_id": "1807214506",
      "store_review_score": 4.8337,
      "store_reviews_number": 9566,
      "star_seller": true,
      "store_name": "TheWeeklyCrew",
      "store_url": "https://www.etsy.com/shop/TheWeeklyCrew",
      "is_ad": true
    },
    {
      "product_name": "Editable Planner Google Sheets Excel Digital Planner Spreadsheet Daily Weekly Agenda Daily Weekly Calendar Digital Daily Schedule Template",
      "product_url": "https://www.etsy.com/listing/1797037228/editable-planner-google-sheets-excel?click_key=af0ac4eb96d2077212f64aeddc72b0161426a5d7%3A1797037228&click_sum=e78af2d3&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-45&pro=1&dd=1&content_source=af0ac4eb96d2077212f64aeddc72b0161426a5d7%253A1797037228",
      "product_id": "1797037228",
      "store_review_score": 4.787,
      "store_reviews_number": 766,
      "star_seller": false,
      "store_name": "OneWayPrintables",
      "store_url": "https://www.etsy.com/shop/OneWayPrintables",
      "is_ad": true
    },
    {
      "product_name": "Winter booklet for preschoolers, preschool booklet, preschool book",
      "product_url": "https://www.etsy.com/listing/1858749443/winter-booklet-for-preschoolers?click_key=0f471cbf33960755693c7695591a9be686df61aa%3A1858749443&click_sum=5f401d85&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-46&bes=1&sts=1&dd=1&content_source=0f471cbf33960755693c7695591a9be686df61aa%253A1858749443",
      "product_id": "1858749443",
      "store_review_score": 4.9877,
      "store_reviews_number": 81,
      "star_seller": true,
      "store_name": "kitaimpulse",
      "store_url": "https://www.etsy.com/shop/kitaimpulse",
      "is_ad": true
    },
    {
      "product_name": "Monthly Budget Spreadsheet | Blush Pink Palette | Simple Annual Budget | Personal Finances | Easy Google Sheets | Financial Planner Easy",
      "product_url": "https://www.etsy.com/listing/1344426956/monthly-budget-spreadsheet-blush-pink?click_key=b3531ea8ce652aa73db69bbaa9f17da842b0a88d%3A1344426956&click_sum=7dc4ccdf&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-47&pro=1&sts=1&dd=1&content_source=b3531ea8ce652aa73db69bbaa9f17da842b0a88d%253A1344426956",
      "product_id": "1344426956",
      "store_review_score": 4.7814,
      "store_reviews_number": 7163,
      "star_seller": true,
      "store_name": "SimplyOrganizedPro",
      "store_url": "https://www.etsy.com/shop/SimplyOrganizedPro",
      "is_ad": true
    },
    {
      "product_name": "Valid for 1 Month",
      "product_url": "https://www.etsy.com/listing/1794461750/valid-for-1-month?click_key=33dd57dd8516c999b4d74f1c5686a6139104b159%3A1794461750&click_sum=68039318&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=search_grid-49636-1-48&dd=1&content_source=33dd57dd8516c999b4d74f1c5686a6139104b159%253A1794461750",
      "product_id": "1794461750",
      "store_review_score": null,
      "store_reviews_number": null,
      "star_seller": false,
      "store_name": "HandmadeYemeni",
      "store_url": "https://www.etsy.com/shop/HandmadeYemeni",
      "is_ad": true
    }
  ],
  "search_url": "https://www.etsy.com/c/paper-and-party-supplies/paper/stationery/design-and-templates?click_key=35fec8efd5281ff1a266cccd173e3872ba67acf3%3A1807934295&click_sum=a68dc1f1&ref=catnav_breadcrumb-3&pro=1&sts=1&explicit=1"
}
```

## Error Handling

The API returns standard HTTP status codes:
- `400`: Bad Request (invalid URL or timeout value)
- `500`: Internal Server Error (scraping or processing error)

Error responses include a detail message explaining the error:
```json
{
    "detail": "Error message"
}
```
