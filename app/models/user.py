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
    inventory_items = relationship("InventoryItem", back_populates="created_by")
    sales = relationship("Sale", back_populates="cashier")
    expense_items = relationship("ExpenseItem", back_populates="created_by")
    category_items = relationship("CategoryItem", back_populates="created_by")
