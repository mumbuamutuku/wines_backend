from sqlalchemy import Boolean, Column, Integer, String, Enum, create_engine
from sqlalchemy.orm import relationship

from app.core.config import settings
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(Enum('admin', 'manager', 'cashier', 'inventory_staff', name='user_roles'), default='cashier')
    
    # Relationships
    inventory_items = relationship("InventoryItem", back_populates="created_by", foreign_keys="InventoryItem.created_by_id")
    sales = relationship("Sale", back_populates="cashier")
    expense_items = relationship("ExpenseItem", back_populates="created_by")
    category_items = relationship("CategoryItem", back_populates="created_by")
    updated_inventory_items = relationship("InventoryItem", back_populates="updated_by", foreign_keys="InventoryItem.updated_by_id")

    customers = relationship("Customer", back_populates="created_by", foreign_keys="Customer.created_by_id")
    updated_customers = relationship("Customer", back_populates="updated_by", foreign_keys="Customer.updated_by_id")
    deleted_customers = relationship("Customer", back_populates="deleted_by", foreign_keys="Customer.deleted_by_id")