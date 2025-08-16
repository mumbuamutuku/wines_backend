from sqlalchemy.orm import Session

from app.models.pos import Sale, SaleItem
from app.models.inventory import InventoryItem
from app.schemas.pos import SaleCreate

def get_sale(db: Session, sale_id: int):
    return db.query(Sale).filter(Sale.id == sale_id).first()

def get_sales(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Sale).offset(skip).limit(limit).all()

def create_sale(db: Session, sale: SaleCreate, cashier_id: int):
    # Calculate total amount
    total_amount = 0.0
    sale_items = []
    
    # Create sale items and update inventory
    for item in sale.items:
        inventory_item = db.query(InventoryItem).filter(InventoryItem.id == item.inventory_item_id).first()
        if not inventory_item:
            raise ValueError(f"Inventory item {item.inventory_item_id} not found")
        
        if inventory_item.stock < item.quantity:
            raise ValueError(f"Not enough quantity for item {inventory_item.name}")
        
        # Update inventory
        inventory_item.stock -= item.quantity
        
        # Calculate item total
        item_total = item.quantity * item.price_at_sale
        total_amount += item_total
        
        # Create sale item
        sale_item = SaleItem(
            inventory_item_id=item.inventory_item_id,
            quantity=item.quantity,
            price_at_sale=item.price_at_sale
        )
        sale_items.append(sale_item)
    
    # Create sale
    db_sale = Sale(
        total_amount=total_amount,
        cashier_id=cashier_id,
        items=sale_items
    )
    
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale