from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class CategoryItemBase(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryItemCreate(CategoryItemBase):
    pass

class CategoryItemUpdate(CategoryItemBase):
    pass

class CategoryItemInDB(CategoryItemBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    created_by_id: int

    class Config:
        from_attributes = True