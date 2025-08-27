from sqlalchemy.orm import Session

from app.models.customer import Customer
from app.schemas.customer import CustomerCreate, CustomerUpdate

def get_customer(db: Session, item_id: int):
    return db.query(Customer).filter(Customer.id == item_id).first()

def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Customer).offset(skip).limit(limit).all()

def create_customer(db: Session, item: CustomerCreate, user_id: int):
    db_item = Customer(**item.dict(), created_by_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_customer(db: Session, item_id: int, item: CustomerUpdate, updated_by_id: int):
    db_item = get_customer(db, item_id)
    if not db_item:
        return None
    
     # Only update fields that are provided
    update_data = item.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_item, key, value)
    
    # Set updated_by_id and trigger updated_at
    db_item.updated_by_id = updated_by_id
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_customer(db: Session, item_id: int):
    db_item = get_customer(db, item_id)
    if not db_item:
        return None
    db.delete(db_item)
    db.commit()
    return db_item
