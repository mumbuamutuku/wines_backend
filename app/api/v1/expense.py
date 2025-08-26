from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.core.security import get_current_active_user, role_required
from app.schemas.user import UserRole
from app.schemas.expense import expenseItemInDB, expenseItemCreate, expenseItemUpdate
from app.crud.expenses import (
    get_expense_items,
    get_expense_item,
    create_expense_item,
    update_expense_item,
    delete_expense_item
)

router = APIRouter()

@router.get("/", response_model=List[expenseItemInDB])
def read_expense_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user)
):
    items = get_expense_items(db, skip=skip, limit=limit)
    return items

@router.post("/", response_model=expenseItemInDB)
def create_item(
    item: expenseItemCreate,
    db: Session = Depends(get_db),
    current_user=Depends(role_required(UserRole.manager))
):
    return create_expense_item(db, item=item, user_id=current_user.id)

@router.put("/{expense_id}", response_model=expenseItemInDB)
def update_item(
    item_id: int,
    item: expenseItemUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(role_required(UserRole.admin))
):
    db_item = get_expense_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return update_expense_item(db, item_id=item_id, item=item)

@router.delete("/{expense_id}")
def delete_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(role_required(UserRole.admin))
):
    db_item = get_expense_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    delete_expense_item(db, item_id=item_id)
    return {"ok": True}