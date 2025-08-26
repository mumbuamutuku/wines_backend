from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, create_engine
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.core.config import settings

class ExpenseItem(Base):
    __tablename__ = "expense_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String)
    amount = Column(Float, nullable=False)
    category = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    created_by_id = Column(Integer, ForeignKey("users.id"))
    
    # Relationships
    created_by = relationship("User", back_populates="expense_items")

    engine = create_engine(settings.DATABASE_URL)
    Base.metadata.create_all(bind=engine)