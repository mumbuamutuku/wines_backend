from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Import models after Base is created
from app.models import *  # This ensures all models are registered

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()