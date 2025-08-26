from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.core.security import get_current_active_user, role_required
from app.schemas.user import UserRole
from app.schemas.category import CategoryItemInDB, CategoryItemCreate, CategoryItemUpdate
from app.crud.category import (
    get_category_items,
    get_category_item,
    create_category_item,
    update_category_item,
    delete_category_item
)

router = APIRouter()

@router.get("/", response_model=List[CategoryItemInDB])
def read_category_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user)
):
    items = get_category_items(db, skip=skip, limit=limit)
    return items

@router.post("/", response_model=CategoryItemInDB)
def create_item(
    item: CategoryItemCreate,
    db: Session = Depends(get_db),
    current_user=Depends(role_required(UserRole.inventory_staff))
):
    return create_category_item(db, item=item, user_id=current_user.id)

@router.put("/{item_id}", response_model=CategoryItemInDB)
def update_item(
    item_id: int,
    item: CategoryItemUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(role_required(UserRole.inventory_staff))
):
    db_item = get_category_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return update_category_item(db, item_id=item_id, item=item)

@router.delete("/{item_id}")
def delete_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(role_required(UserRole.inventory_staff))
):
    db_item = get_category_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    delete_category_item(db, item_id=item_id)
    return {"ok": True}