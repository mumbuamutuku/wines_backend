from sqlalchemy.orm import Session

from app.models.category import CategoryItem
from app.schemas.category import CategoryItemCreate, CategoryItemUpdate

def get_category_item(db: Session, item_id: int):
    return db.query(CategoryItem).filter(CategoryItem.id == item_id).first()

def get_category_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CategoryItem).offset(skip).limit(limit).all()

def create_category_item(db: Session, item: CategoryItemCreate, user_id: int):
    db_item = CategoryItem(**item.dict(), created_by_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_category_item(db: Session, item_id: int, item: CategoryItemUpdate):
    db_item = get_category_item(db, item_id)
    if not db_item:
        return None
    for key, value in item.dict().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_category_item(db: Session, item_id: int):
    db_item = get_category_item(db, item_id)
    if not db_item:
        return None
    db.delete(db_item)
    db.commit()
    return db_item
