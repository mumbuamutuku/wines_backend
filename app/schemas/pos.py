from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

class SaleItemBase(BaseModel):
    inventory_item_id: int
    quantity: float
    price_at_sale: float

class SaleBase(BaseModel):
    items: List[SaleItemBase]

class SaleCreate(SaleBase):
    pass

class SaleInDB(SaleBase):
    id: int
    total_amount: float
    created_at: datetime
    cashier_id: int

    class Config:
        from_attributes = True