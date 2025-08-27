from sqlalchemy.orm import Session

from app.models.inventory import InventoryItem
from app.schemas.inventory import InventoryItemCreate, InventoryItemUpdate

def get_inventory_item(db: Session, item_id: int):
    return db.query(InventoryItem).filter(InventoryItem.id == item_id).first()

def get_inventory_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(InventoryItem).offset(skip).limit(limit).all()

def create_inventory_item(db: Session, item: InventoryItemCreate, user_id: int):
    db_item = InventoryItem(**item.dict(), created_by_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_inventory_item(db: Session, item_id: int, item: InventoryItemUpdate, updated_by_id: int):
    db_item = get_inventory_item(db, item_id)
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

def delete_inventory_item(db: Session, item_id: int):
    db_item = get_inventory_item(db, item_id)
    if not db_item:
        return None
    db.delete(db_item)
    db.commit()
    return db_item
