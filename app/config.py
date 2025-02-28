# app/config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./assist.db")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
DEBUG = os.getenv("DEBUG", "True") == "True"

# JWT Configuration for authentication
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
