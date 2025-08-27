from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.core.security import get_current_active_user, role_required
from app.schemas.user import UserRole
from app.schemas.customer import CustomerInDB, CustomerCreate, CustomerUpdate
from app.crud.customer import (
    get_customers,
    get_customer,
    create_customer,
    update_customer,
    delete_customer
)

router = APIRouter()

@router.get("/", response_model=List[CustomerInDB])
def read_customers(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user)
):
    items = get_customers(db, skip=skip, limit=limit)
    return items

@router.get("/{id}", response_model=CustomerInDB)
def read_customer(
    id: int,
    db: Session = Depends(get_db),
    current_user= Depends(get_current_active_user)
):
    cust = get_customer(db, item_id=id)
    if cust is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return cust

@router.post("/", response_model=CustomerInDB)
def create_item(
    item: CustomerCreate,
    db: Session = Depends(get_db),
    current_user=Depends(role_required(UserRole.inventory_staff))
):
    return create_customer(db, item=item, user_id=current_user.id)

@router.put("/{item_id}", response_model=CustomerInDB)
def update_item(
    item_id: int,
    item: CustomerUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user)
):
    if current_user.role not in [UserRole.inventory_staff, UserRole.admin]:
       raise HTTPException(status_code=403, detail="Not enough permissions")
    db_item = get_customer(db, item_id=item_id)
    print(db_item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return update_customer(db, item_id=item_id, item=item, updated_by_id=current_user.id)

@router.delete("/{customer_id}")
def delete_item(
    customer_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user)
):
    if current_user.role not in [UserRole.manager, UserRole.admin]:
       raise HTTPException(status_code=403, detail="Not enough permissions")
    db_item = get_customer(db, item_id=customer_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    delete_customer(db, item_id=customer_id)
    return {"ok": True}

