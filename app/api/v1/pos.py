from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.core.security import get_current_active_user, role_required
from app.schemas.user import UserRole
from app.schemas.pos import SaleInDB, SaleCreate
from app.crud.pos import get_sales, get_sale, create_sale

router = APIRouter()

@router.get("/", response_model=List[SaleInDB])
def read_sales(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user)
):
    if current_user.role not in [UserRole.admin, UserRole.manager]:
        # Cashiers can only see their own sales
        sales = db.query(Sale).filter(Sale.cashier_id == current_user.id).offset(skip).limit(limit).all()
    else:
        sales = get_sales(db, skip=skip, limit=limit)
    return sales

@router.get("/{sale_id}", response_model=SaleInDB)
def read_sale(
    sale_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user)
):
    sale = get_sale(db, sale_id=sale_id)
    if sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    if current_user.role not in [UserRole.admin, UserRole.manager] and sale.cashier_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to view this sale")
    return sale

@router.post("/", response_model=SaleInDB)
def create_new_sale(
    sale: SaleCreate,
    db: Session = Depends(get_db),
    current_user=Depends(role_required(UserRole.cashier))
):
    try:
        return create_sale(db, sale=sale, cashier_id=current_user.id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))