from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.core.security import get_current_active_user, role_required
from app.schemas.user import UserInDB, UserCreate, UserRole
from app.crud.user import get_user, get_user_by_email, get_users, create_user

router = APIRouter()

@router.get("/", response_model=List[UserInDB])
def read_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user=Depends(role_required(UserRole.admin))
):
    """
    Retrieve all users (admin only)
    """
    users = get_users(db, skip=skip, limit=limit)
    return users

@router.post("/", response_model=UserInDB, status_code=status.HTTP_201_CREATED)
def create_new_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    current_user=Depends(role_required(UserRole.admin))
):
    """
    Create a new user (admin only)
    """
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user=user)

@router.get("/me", response_model=UserInDB)
def read_user_me(current_user: UserInDB = Depends(get_current_active_user)):
    """
    Get current user details
    """
    return current_user

@router.get("/{user_id}", response_model=UserInDB)
def read_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(role_required(UserRole.admin))
):
    """
    Get a specific user by ID (admin only)
    """
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user