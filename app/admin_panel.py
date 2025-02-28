# app/admin_panel.py
from fastapi import APIRouter, Depends, HTTPException
from app.auth import fake_users_db, User, get_current_user

router = APIRouter(prefix="/admin", tags=["Admin Panel"])

def admin_required(user: User = Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return user

@router.get("/users")
def list_users(admin: User = Depends(admin_required)):
    # Return a list of all registered users
    return [user for user in fake_users_db.values()]

@router.put("/users/{username}")
def update_user(username: str, user_update: User, admin: User = Depends(admin_required)):
    if username not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    fake_users_db[username] = user_update
    return user_update

@router.delete("/users/{username}")
def delete_user(username: str, admin: User = Depends(admin_required)):
    if username not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del fake_users_db[username]
    return {"detail": "User deleted successfully"}
