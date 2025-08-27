from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class InventoryItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    stock: float
    price: float
    category_id: Optional[int] = None
    category: Optional[str] = None
    cost: float

class InventoryItemCreate(InventoryItemBase):
    pass

class InventoryItemUpdate(InventoryItemBase):
    name: Optional[str] = None
    description: Optional[str] = None
    stock: Optional[float] = None
    price: Optional[float] = None
    cost: Optional[float] = None
    category_id: Optional[int] = None
    category: Optional[str] = None

class InventoryItemInDB(InventoryItemBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    created_by_id: int
    updated_by_id: Optional[int]

    class Config:
        from_attributes = True