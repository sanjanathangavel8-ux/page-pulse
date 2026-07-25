from fastapi import FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware

from app.models import URLRequest
from app.services import analyze_url
from app.middleware import RequestIDMiddleware

# Create FastAPI app FIRST
app = FastAPI(
    title="Page Pulse API",
    version="1.0.0",
    description="Production-grade URL Audit API"
)

# Configure rate limiter
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

# Add middleware
app.add_middleware(SlowAPIMiddleware)
app.add_middleware(RequestIDMiddleware)

# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Page Pulse API Running"
    }

# Health endpoint
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

# Audit endpoint
@app.post("/audit")
@limiter.limit("10/minute")
async def audit(request: Request, body: URLRequest):
    return await analyze_url(str(body.url))