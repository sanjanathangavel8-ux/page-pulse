import time
import httpx
from bs4 import BeautifulSoup
from app.cache import cache
from app.concurrency import semaphore

async def analyze_url(url: str):
    async with semaphore:
        async def analyze_url(url: str):
            if url in cache:
                return cache[url]

    try:
        start = time.perf_counter()

        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url)

        response_time = round((time.perf_counter() - start) * 1000, 2)

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string.strip() if soup.title else "No title"

        description = ""
        meta = soup.find("meta", attrs={"name": "description"})
        if meta:
            description = meta.get("content", "")

        result = {
            "success": True,
            "url": url,
            "status_code": response.status_code,
            "response_time_ms": response_time,
            "title": title,
            "meta_description": description
        }

        # Store in cache
        cache[url] = result

        return result

    except httpx.TimeoutException:
        return {
            "success": False,
            "error": "Request timed out"
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }