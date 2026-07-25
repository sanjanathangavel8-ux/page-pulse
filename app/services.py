import time
import httpx
from bs4 import BeautifulSoup

from app.cache import cache
from app.concurrency import semaphore


async def analyze_url(url: str):

    # Check cache first
    if url in cache:
        return cache[url]

    try:
        async with semaphore:

            start = time.perf_counter()

            async with httpx.AsyncClient(timeout=10) as client:
                response = await client.get(
                    url,
                    follow_redirects=True
                )

            response_time = round(
                (time.perf_counter() - start) * 1000,
                2
            )

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )


            # Extract title
            title = (
                soup.title.string.strip()
                if soup.title and soup.title.string
                else None
            )


            # Extract meta description
            description = ""

            meta = soup.find(
                "meta",
                attrs={"name": "description"}
            )

            if meta:
                description = meta.get(
                    "content",
                    ""
                )


            # Security check
            https_status = (
                "Enabled"
                if url.startswith("https")
                else "Disabled"
            )


            # SEO analysis
            seo_title = (
                "Present"
                if title
                else "Missing"
            )

            seo_description = (
                "Present"
                if description
                else "Missing"
            )


            # Performance rating
            if response_time < 500:
                performance_status = "Excellent"
            elif response_time < 1000:
                performance_status = "Good"
            else:
                performance_status = "Slow"


            # Health score calculation
            score = 100

            if response.status_code != 200:
                score -= 30

            if not title:
                score -= 10

            if not description:
                score -= 10

            if response_time > 1000:
                score -= 10


            recommendations = []

            if not title:
                recommendations.append(
                    "Add a proper page title"
                )

            if not description:
                recommendations.append(
                    "Add meta description"
                )

            if response_time > 1000:
                recommendations.append(
                    "Improve page loading speed"
                )


            result = {

                "website": title or url,

                "health_score": score,

                "performance": {
                    "response_time": f"{response_time}ms",
                    "status": performance_status
                },

                "seo": {
                    "title": seo_title,
                    "meta_description": seo_description
                },

                "security": {
                    "https": https_status
                },

                "technical": {
                    "status_code": response.status_code
                },

                "recommendations": recommendations

            }


            # Cache result
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