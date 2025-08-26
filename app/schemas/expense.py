from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class expenseItemBase(BaseModel):
    name: str
    category: Optional[str] = None
    amount: float
    description: Optional[str] = None
    

class expenseItemCreate(expenseItemBase):
    pass

class expenseItemUpdate(expenseItemBase):
    pass

class expenseItemInDB(expenseItemBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    created_by_id: int

    class Config:
        from_attributes = True