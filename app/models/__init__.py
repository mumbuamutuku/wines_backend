# Import all models here to ensure they're loaded
from .user import User
from .inventory import InventoryItem
from .pos import Sale, SaleItem

__all__ = ["User", "InventoryItem", "Sale", "SaleItem"]