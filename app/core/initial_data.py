from sqlalchemy.orm import Session

from app.crud.user import create_user
from app.schemas.user import UserCreate
from app.models.user import User

def init_superadmin(db: Session, email: str, password: str, full_name: str = "Super Admin"):
    """Create initial superadmin if no users exist"""
    if db.query(User).count() == 0:
        superadmin = UserCreate(
            email=email,
            password=password,
            full_name=full_name,
            role="admin"
        )
        create_user(db, superadmin)
        print(f"Superadmin created: {email}")
    else:
        print("Superadmin already exists")
        