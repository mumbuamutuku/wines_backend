from sqlalchemy.orm import Session

from app.models.expense import ExpenseItem
from app.schemas.expense import expenseItemCreate, expenseItemUpdate

def get_expense_item(db: Session, item_id: int):
    return db.query(ExpenseItem).filter(ExpenseItem.id == item_id).first()

def get_expense_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ExpenseItem).offset(skip).limit(limit).all()

def create_expense_item(db: Session, item: expenseItemCreate, user_id: int):
    db_item = ExpenseItem(**item.dict(), created_by_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_expense_item(db: Session, item_id: int, item: expenseItemUpdate):
    db_item = get_expense_item(db, item_id)
    if not db_item:
        return None
    for key, value in item.dict().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_expense_item(db: Session, item_id: int):
    db_item = get_expense_item(db, item_id)
    if not db_item:
        return None
    db.delete(db_item)
    db.commit()
    return db_item
