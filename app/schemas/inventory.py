from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class InventoryItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    stock: float
    price: float
    category: Optional[str] = None
    cost: float

class InventoryItemCreate(InventoryItemBase):
    pass

class InventoryItemUpdate(InventoryItemBase):
    pass

class InventoryItemInDB(InventoryItemBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    created_by_id: int

    class Config:
        from_attributes = True