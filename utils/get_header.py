from fake_useragent import UserAgent
import random
import requests
from httpx import AsyncClient
import sys, os

# Ensure the project's root directory is in the Python path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


ua = UserAgent()
    #----FireFox----


already_used = set()
for i in range(1, 2):
    user_agent = ua.firefox
    if user_agent in already_used:
        print(f"UserAgent {user_agent} has already been used. Skipping...")
        continue
    already_used.add(user_agent)
    # Category header for analysis
    header = {
                'User-Agent': f'{user_agent}',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                # 'Accept-Encoding': 'gzip, deflate, br, zstd',
                'DNT': '1',
                'Sec-GPC': '1',
                'Connection': 'keep-alive',
                'Cookie': 'datadome=7BGx1wHedSA3gAlIJFKZ7iTxjBnjoWamCWMNAM1JQD8COR_r8Q~aE~BLkDkGVJoMJtwajKIY8M418h4HGMCe0u_B8Mk3xjKVUoQLq0rikTl6wpl5I8M9FVMqwbBLK3ox; exp_ebid=m=QBjT03EiZGVcyHG5XE5ZIQzjpe6urrN92Xjk9tW7uhY%3D,v=jodar_ZH7cld3caXudhygNAWGakMczD-; uaid=sY5osjbQl9TWGFA2582FdAuwwhhjZACCDJa7GjC6Wqk0MTNFyUopI93JIsLcwL8qsyzFqNwkzd3T3C-g2NE_MN49QKmWAQA.; user_prefs=Rrg0tJ5QGTvcoGomJSUYSzsVZkNjZACCDJa7GjA6WsndKUBJJ680J0dHKTVP191JSUcJRIBFjCAULiKWAQA.; fve=1745149224.0; _fbp=fb.1.1745149224810.5743244604227888; ua=531227642bc86f3b5fd7103a0c0b4fd6; _gcl_au=1.1.348421385.1745149225; _ga_KR3J610VYM=GS1.1.1745149225.1.1.1745149379.60.0.0; _ga=GA1.1.1946022003.1745149225; __adal_ses=*; __adal_id=adf633bd-ee1f-4064-97ca-5d9bc06f8ac4.1745149226.1.1745149379.1745149226.b1169c51-0bd5-44fb-8b47-86df1def8cdd; __adal_ca=so%3Ddirect%26me%3Dnone%26ca%3Ddirect%26co%3D%28not%2520set%29%26ke%3D%28not%2520set%29; __adal_cw=1745149225510; _pin_unauth=dWlkPU5UYzVNbUZqTkRRdE1ERTNOQzAwTTJJd0xXSTJNVFl0TmprME56WmxNVEl4T1RCaw',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'Priority': 'u=0, i',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
                # Requests doesn't support trailers
                # 'TE': 'trailers',
            }
    
    url = f"https://www.etsy.com/uk/c/jewelry?explicit=1&instant_download=true&ship_to=GB&order=highest_reviews&page={i}"

    response = requests.get(url, headers=header)

    print(f"Response Code: {response.status_code}")
    print(f"Length of response html is {len(response.text)}")

    if len(response.text) < 2000:
        print(f"Failed to fetch complete html, Saving for debug...")
        with open(f"utils/debug/Page {i}.html", "w", encoding="utf-8") as f:
            f.write(str(response.text))

    with open(f"utils/debug/Page {i}.html", "w", encoding="utf-8") as f:
        f.write(str(response.text))