# 🚀 Page Pulse API

A production-grade URL Audit Service built with **FastAPI** that analyzes web pages and returns useful metadata such as page title, meta description, HTTP status code, and response time.

This project was developed as part of the **Digital Heroes Software Development (SDE) Training Task**.

---

# 🌐 Live Demo

**Live Application**

👉 https://YOUR-RENDER-URL.onrender.com

**Swagger Documentation**

👉 https://YOUR-RENDER-URL.onrender.com/docs

---

# ✨ Features

- ✅ Production-grade FastAPI REST API
- ✅ URL Validation using Pydantic
- ✅ Async HTTP Requests using HTTPX
- ✅ Configurable Request Timeout
- ✅ Response Time Measurement
- ✅ HTTP Status Code Detection
- ✅ Page Title Extraction
- ✅ Meta Description Extraction
- ✅ In-Memory Caching (TTL Cache)
- ✅ Rate Limiting per Client (SlowAPI)
- ✅ Request ID Middleware
- ✅ Structured Logging
- ✅ Health Check Endpoint
- ✅ Interactive Swagger Documentation
- ✅ Automated Testing with Pytest
- ✅ GitHub Actions Continuous Integration
- ✅ Render Deployment

---

# 🛠️ Tech Stack

- Python 3.13
- FastAPI
- Uvicorn
- HTTPX
- BeautifulSoup4
- Cachetools
- SlowAPI
- Jinja2
- Pytest
- GitHub Actions
- Render

---

# 📂 Project Structure

```text
page-pulse/
│
├── app/
│   ├── __init__.py
│   ├── cache.py
│   ├── concurrency.py
│   ├── logger.py
│   ├── main.py
│   ├── middleware.py
│   ├── models.py
│   └── services.py
│
├── templates/
│   └── index.html
│
├── tests/
│   └── test_api.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/sanjanathangavel8-ux/page-pulse.git
```

```bash
cd page-pulse
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
uvicorn app.main:app --reload
```

Application

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# 📌 API Endpoints

## GET /

Returns the landing page with project information and the required Digital Heroes attribution.

---

## GET /health

Returns service health.

### Response

```json
{
  "status": "healthy",
  "service": "Page Pulse API"
}
```

---

## POST /audit

Analyzes a webpage.

### Request

```json
{
  "url": "https://example.com"
}
```

### Response

```json
{
  "success": true,
  "url": "https://example.com",
  "status_code": 200,
  "response_time_ms": 143.25,
  "title": "Example Domain",
  "meta_description": "Example website description"
}
```

---

# 🧪 Running Tests

```bash
python -m pytest
```

Expected Output

```text
2 passed
```

---

# 🔄 Continuous Integration

GitHub Actions automatically:

- Installs dependencies
- Runs Pytest
- Verifies every push to the repository

---

# 🚀 Deployment

Hosted on **Render**

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

---

# 📄 API Contract

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Landing page |
| `/health` | GET | Health check |
| `/audit` | POST | Analyze a webpage |

---

# 📷 Live Build Requirement

The landing page includes the required attribution:

**Built for Digital Heroes Training Task**

linked to

https://digitalheroesco.com

This satisfies the live build requirement specified in the assignment.

---

# 👩‍💻 Author

**Sanjana Sri**

B.Tech Computer Science and Business Systems (CSBS)

GitHub:
https://github.com/sanjanathangavel8-ux

Repository:
https://github.com/sanjanathangavel8-ux/page-pulse

---

# 🙏 Acknowledgement

This project was built as part of the **Digital Heroes Software Development (SDE) Training Task** and demonstrates production-oriented API development practices using FastAPI, asynchronous programming, caching, rate limiting, structured logging, automated testing, and CI/CD.