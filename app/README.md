# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]

# Assist2: AI Assistant Project

## Overview
Assist2 is an AI-powered personal assistant built with FastAPI. It includes:
- User authentication and admin panel
- Multiple specialized AI agents (Developer, Tester, Researcher, etc.)
- A simple LLM interface (stub for further integration)
- Background tasks via Celery
- Auto-deployment using GitHub Actions to AWS (or later, multi-server scaling)

## Repository Structure
(Include the repository structure as listed above.)

## Setup
1. **Clone the Repository**
   ```bash
   git clone git@github.com:ryaag01/Assist2.git
   cd Assist2
