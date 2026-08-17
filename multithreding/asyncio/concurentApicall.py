# • Given a synchronous function making 
# 5 sequential API calls, refactor it to run 
# concurrently using asyncio.gather, and 
# explain what changes if one call must 
# retry on failure.

# import requests

# def fetch_data():
#     urls = [
#         "https://api.example.com/1",
#         "https://api.example.com/2",
#         "https://api.example.com/3",
#         "https://api.example.com/4",
#         "https://api.example.com/5",
#     ]

#     results = []
#     for url in urls:
#         response = requests.get(url)
#         response.raise_for_status()
#         results.append(response.json())

#     return results


import asyncio
import httpx

URLS = [
    "https://api.example.com/1",
    "https://api.example.com/2",
    "https://api.example.com/3",
    "https://api.example.com/4",
    "https://api.example.com/5",
]

async def fetch(client, url):
    response = await client.get(url)
    response.raise_for_status()
    return response.json()




# fetch with retry

async def fetch_with_retry(client, url, retries=3):
    for attempt in range(retries):
        try:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()

        except Exception as e:
            if attempt == retries - 1:
                raise
            await asyncio.sleep(2 ** attempt)   # exponential backoff

async def fetch_all():
    async with httpx.AsyncClient(timeout=10) as client:
        tasks = [fetch(client, url) for url in URLS]
        results = await asyncio.gather(*tasks)
        return results

if __name__ == "__main__":
    data = asyncio.run(fetch_all())
    print(data)