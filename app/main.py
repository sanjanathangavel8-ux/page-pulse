from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import httpx
from bs4 import BeautifulSoup
import time


app = FastAPI(
    title="Page Pulse API",
    version="1.0.0",
)


# ==========================
# CORS CONFIGURATION
# ==========================

app.add_middleware(
    CORSMiddleware,

    # Frontend URLs
    allow_origins=[
        "http://localhost:3000",
        "https://page-pulse.vercel.app",
    ],

    allow_credentials=True,

    allow_methods=[
        "GET",
        "POST",
        "PUT",
        "DELETE",
        "OPTIONS",
    ],

    allow_headers=["*"],
)


# ==========================
# REQUEST MODEL
# ==========================

class AuditRequest(BaseModel):
    url: str



# ==========================
# ROOT
# ==========================

@app.get("/")
def root():
    return {
        "message": "Page Pulse API running"
    }



# ==========================
# HEALTH CHECK
# ==========================

@app.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "Page Pulse API"
    }



# ==========================
# AUDIT ENDPOINT
# ==========================

@app.post("/audit")
async def audit(
    request: AuditRequest
):

    url = request.url


    start = time.time()


    async with httpx.AsyncClient(
        follow_redirects=True,
        timeout=20
    ) as client:

        response = await client.get(url)


    response_time = (
        time.time() - start
    )


    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )


    title = (
        soup.title.text
        if soup.title
        else "No title"
    )


    meta = soup.find(
        "meta",
        attrs={
            "name": "description"
        }
    )


    description = (
        meta["content"]
        if meta
        else "No description"
    )


    return {

        "health_score": 90,

        "performance": {

            "status": "Good",

            "response_time":
                f"{response_time:.2f}s"

        },


        "seo": {

            "title": title,

            "meta_description":
                description

        },


        "security": {

            "https":
                url.startswith("https")

        },


        "technical": {

            "status_code":
                response.status_code

        },


        "recommendations": [

            "Optimize images",

            "Improve page loading speed"

        ]

    }