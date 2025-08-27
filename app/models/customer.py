from sqlalchemy import Boolean, Column, Float, DateTime, ForeignKey, Integer, String, Enum, create_engine, func
from sqlalchemy.orm import relationship

from app.core.config import settings
from app.core.database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    totalPurchases = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    created_by_id = Column(Integer, ForeignKey("users.id"))
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    updated_by_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True)
    deleted_by_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    
    # Relationships
    created_by = relationship("User", back_populates="customers", foreign_keys=[created_by_id])
    updated_by = relationship("User", back_populates="updated_customers", foreign_keys=[updated_by_id])
    deleted_by = relationship("User", back_populates="deleted_customers", foreign_keys=[deleted_by_id])
    sales = relationship("Sale", back_populates="customer")
    