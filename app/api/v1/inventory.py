from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.core.security import get_current_active_user, role_required
from app.schemas.user import UserRole
from app.schemas.inventory import InventoryItemInDB, InventoryItemCreate, InventoryItemUpdate
from app.crud.inventory import (
    get_inventory_items,
    get_inventory_item,
    create_inventory_item,
    update_inventory_item,
    delete_inventory_item
)

router = APIRouter()

@router.get("/", response_model=List[InventoryItemInDB])
def read_inventory_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user)
):
    items = get_inventory_items(db, skip=skip, limit=limit)
    return items

@router.post("/", response_model=InventoryItemInDB)
def create_item(
    item: InventoryItemCreate,
    db: Session = Depends(get_db),
    current_user=Depends(role_required(UserRole.inventory_staff))
):
    return create_inventory_item(db, item=item, user_id=current_user.id)

@router.put("/{item_id}", response_model=InventoryItemInDB)
def update_item(
    item_id: int,
    item: InventoryItemUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user)
):
    if current_user.role not in [UserRole.inventory_staff, UserRole.admin]:
       raise HTTPException(status_code=403, detail="Not enough permissions")
    db_item = get_inventory_item(db, item_id=item_id)
    print(db_item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return update_inventory_item(db, item_id=item_id, item=item, updated_by_id=current_user.id)

@router.delete("/{item_id}")
def delete_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(role_required(UserRole.inventory_staff))
):
    db_item = get_inventory_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    delete_inventory_item(db, item_id=item_id)
    return {"ok": True}