# app/models/inventory_item.py
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base

class InventoryItem(Base):
    __tablename__ = "inventory_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    stock = Column(Float, nullable=False)
    cost = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    created_by_id = Column(Integer, ForeignKey("users.id"))
    updated_by_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    category = Column(String)  # Added ForeignKey
    category_id = Column(Integer, ForeignKey("category_items.id"))
    
    # Relationships
    created_by = relationship("User", back_populates="inventory_items", foreign_keys=[created_by_id])
    updated_by = relationship("User", back_populates="updated_inventory_items", foreign_keys=[updated_by_id])
    sale_items = relationship("SaleItem", back_populates="inventory_item")
    category_item = relationship(
        "CategoryItem",
        back_populates="inventory_items",
        foreign_keys=[category_id]
    )