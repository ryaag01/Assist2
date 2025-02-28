# app/config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env file

# Database & Redis configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./assist.db")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
DEBUG = os.getenv("DEBUG", "True") == "True"

# JWT Configuration for authentication
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

# API Keys (store these in your .env file)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
