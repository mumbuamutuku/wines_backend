from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class CustomerBase(BaseModel):
    name: str
    email: str
    phone: str
    address: str
    totalPurchases: float
    
class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[int] = None
    address: Optional[str] = None
    totalPurchases: Optional[float] = None

class CustomerInDB(CustomerBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    created_by_id: int
    updated_by_id: Optional[int]

    class Config:
        from_attributes = True