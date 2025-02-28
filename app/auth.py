# app/auth.py
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
import jwt
from datetime import datetime, timedelta
from app.config import SECRET_KEY, ALGORITHM
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

router = APIRouter(prefix="/auth", tags=["Authentication"])
security = HTTPBearer()

# For demonstration, using an in-memory user store.
fake_users_db = {}

class User(BaseModel):
    username: str
    password: str
    role: str = "user"          # Default role: "user" or "admin"
    custom_ai_config: dict = {}  # User-specific AI settings

class Token(BaseModel):
    access_token: str
    token_type: str

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=30))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@router.post("/register", response_model=User)
def register(user: User):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    fake_users_db[user.username] = user
    return user

@router.post("/login", response_model=Token)
def login(user: User):
    db_user = fake_users_db.get(user.username)
    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.username, "role": db_user.role})
    return {"access_token": access_token, "token_type": "bearer"}

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None or username not in fake_users_db:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        return fake_users_db[username]
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
