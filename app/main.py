from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from slowapi import Limiter
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address

from app.models import URLRequest
from app.services import analyze_url
from app.middleware import RequestIDMiddleware


app = FastAPI(
    title="Page Pulse API",
    version="1.0.0",
    description="Production-grade URL Audit API"
)

# ----------------------------
# CORS
# ----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://page-pulse-frontend.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------
# Templates
# ----------------------------
templates = Jinja2Templates(directory="templates")

# ----------------------------
# Rate Limiter
# ----------------------------
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

# ----------------------------
# Middlewares
# ----------------------------
app.add_middleware(RequestIDMiddleware)
app.add_middleware(SlowAPIMiddleware)

# ----------------------------
# Home
# ----------------------------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

# ----------------------------
# Health
# ----------------------------
@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "Page Pulse API"
    }

# ----------------------------
# Audit
# ----------------------------
@app.post("/audit")
@limiter.limit("10/minute")
async def audit(request: Request, body: URLRequest):
    return await analyze_url(str(body.url))