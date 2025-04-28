# Basic General header

{
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



# Copied from chrome, after some interection
{
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'downlink': '6.05',
    'dpr': '1.25',
    'ect': '4g',
    'priority': 'u=0, i',
    'rtt': '150',
    'sec-ch-dpr': '1.25',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="135.0.7049.96", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    # 'cookie': 'uaid=bM1MOjrxpaa0JTGhrCGIExZ1UFtjZACCDPaaqTC6Wqk0MTNFyUrJvKwkJdHdO9HHxdCrLDXV26kiqyzHxMkwPTHTTamWAQA.; user_prefs=ZSfgQYve7dwVLivN2nY1siRNkMxjZACCDPaaqTA6Wsk1NEhJJ680J0dHKTVPNzRYSUfJDSZiBKFwEbEMAA..; fve=1745321109.0; exp_ebid=m=b90BAShSV4PKdft%2BYoaNTSpE%2BrChMYR65s7mV7sb4M0%3D,v=Tvhr-HuXP0Rr5OqsYdbgz6KBHiWuqEhv; ua=531227642bc86f3b5fd7103a0c0b4fd6; datadome=4A40VCdVWSI2PvEtOnLZPS1Hq4lU8piVautSyr_bSChdlSICA0OA8zfFZrNIuKaFGnBMERtk3uPmYgwqOu2QC5sNnmHrIlI1Tdfu1YUu6DMGCvyAvInGUOVSu6DxkDie; p=eyJnZHByX3RwIjoyLCJnZHByX3AiOjJ9',
}

# copy from firefox after some scrolling

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'DNT': '1',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    # 'Cookie': 'uaid=LJwanV3CuabW1BDzWWLxGkiNmYtjZACCDI5Td2B0tVJpYmaKkpWSsb9xQaKlhXl6WpGfYUh5WrpueGBAZUhKipm5mVItAwA.; user_prefs=VpAUqUj0sHdUh0-d3mFC83vvsr1jZACCDI5Td2B0tFJosIuSTl5pTo6OUmqerruTko5SgDdUxAhC4SJiGQA.; fve=1745406684.0; last_browse_page=https%3A%2F%2Fwww.etsy.com%2F; _fbp=fb.1.1745406684059.5620553994011474; exp_ebid=m=Zv%2FT3l9l3SSQiXXNWeg8N6ZSyoqvVeEgKyySrgvBjq4%3D,v=F3SWwRk0Rwqf6qlq2itXIw7xZkvAv7Ck; datadome=i8HwNHAiu8YEbdmLDN_POft8YtEChkl7rfrsnYlBv4XHIXLXRQYxQfxsTIgPKBC8SfoR65zjXsUdT~7ibLOuUQ2AiY3BIz0uQT84cwHLn5V6ATKA2xG4Lb3JVVC7o6ge; ua=531227642bc86f3b5fd7103a0c0b4fd6; _gcl_au=1.1.303135881.1745406687; _ga_KR3J610VYM=GS1.1.1745406687.1.1.1745406698.49.0.0; _ga=GA1.1.919017597.1745406688; _pin_unauth=dWlkPVlUazVNekpoT0dJdFltUmpaaTAwT0dVMkxUbGtNVFV0WkRObFpEZ3hNREUwTW1JMQ',
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

# after solving captcha on edge

{
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.etsy.com/',
    'sec-ch-device-memory': '8',
    'sec-ch-ua': '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-full-version-list': '"Microsoft Edge";v="135.0.3179.85", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
    # 'cookie': 'uaid=2-sZfJfkQsMUxw9JKycwk2UB-hRjZACCDI7T02F0tVJpYmaKkpVSZXBucYqFW5VLeGFWeEmUS3FUYHZ2QL6HR5VRiVItAwA.; user_prefs=qbSWHQJjpnmRee4NYcfbzLz6_YFjZACCDI7T02F0tFJosIuSTl5pTo6OUmqerruTko5SgDdUxAhC4SJiGQA.; fve=1745406871.0; last_browse_page=https%3A%2F%2Fwww.etsy.com%2F; _fbp=fb.1.1745406871610.7590141605708551; exp_ebid=m=JiNrz3duVj0PUsgWqYDOf2YeHvzKqNDTzrvCeonqoHg%3D,v=9OPLFpfPCWMs24ttPdF9bi7yxZzIPDAf; ua=531227642bc86f3b5fd7103a0c0b4fd6; _gcl_au=1.1.1056874315.1745406874; daily_deals_listings=1760772179,1439215482,1275026920,1691774789,1551811473,796253063,782328024,1876793582,1855258643,1772065342,1042867485,1737764030,1614338742,1882059656,1567160504; lantern=44f7c2ac-ba5c-443c-a623-373164d77d06; _ga=GA1.1.1824269325.1745406875; _uetsid=231b4ea0203411f0a7d7612fd570b7fc; _uetvid=231ba320203411f09347838307dd68d8; _pin_unauth=dWlkPU1qWmtZbU0zWW1NdE1EUTFOeTAwWlRCa0xXSmpORE10WkdKbE1UUmpaamt4TnpJMg; search_options={"prev_search_term":"","item_language":null,"language_carousel":null}; tsd=%7B%22gnav_search_focus%22%3A%7B%22event_name%22%3A%22gnav_search_focus%22%2C%22interaction_type%22%3A%22click%22%7D%2C%22gnav_perform_search%22%3A%7B%22event_name%22%3A%22gnav_perform_search%22%2C%22interaction_type%22%3A%22click%22%7D%7D; _ga_KR3J610VYM=GS1.1.1745406874.1.1.1745406907.27.0.0; datadome=KZcjvzcOpKyT5sDif4u64tBzVoGpATWloZNsOTyr8CM8fi8IGwLbM4Rn~zS1S0y4lO~yIitph6294bF98TE4qdIxnsAifd8tufP6izGJlp6VDeBHk~89bJmtER9WWoUE',
}
