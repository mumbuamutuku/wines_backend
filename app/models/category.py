from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base

class CategoryItem(Base):
    __tablename__ = "category_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    created_by_id = Column(Integer, ForeignKey("users.id"))
    
    # Relationships
    created_by = relationship("User", back_populates="category_items")
    inventory_items = relationship(
        "InventoryItem",
        back_populates="category_item",  # Point to the relationship on InventoryItem
        foreign_keys="[InventoryItem.category_id]"
    )