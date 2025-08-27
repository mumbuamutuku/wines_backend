from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, create_engine
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.core.config import settings
from app.core.database import Base

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    total_amount = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    cashier_id = Column(Integer, ForeignKey("users.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    sales_notes = Column(String)
    total_discount = Column(Float, nullable=False)

    # Relationships
    cashier = relationship("User", back_populates="sales")
    items = relationship("SaleItem", back_populates="sale")
    customer = relationship("Customer", back_populates="sales")

class SaleItem(Base):
    __tablename__ = "sale_items"

    id = Column(Integer, primary_key=True, index=True)
    sale_id = Column(Integer, ForeignKey("sales.id"))
    inventory_item_id = Column(Integer, ForeignKey("inventory_items.id"))
    quantity = Column(Float, nullable=False)
    price_at_sale = Column(Float, nullable=False)
    
    # Relationships
    sale = relationship("Sale", back_populates="items")
    inventory_item = relationship("InventoryItem", back_populates="sale_items")
    