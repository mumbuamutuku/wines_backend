from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1 import auth, user, inventory, pos, expense, category
from app.core.database import Base, engine

import sys
import os

print("Starting application...")
print("Python executable:", sys.executable)
print("Current directory:", os.getcwd())
print("Environment variables:")
for key in ['DATABASE_URL', 'SECRET_KEY', 'ALGORITHM']:
    print(f"  {key}: {os.getenv(key)}")

app = FastAPI(title="Inventory and POS System")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create all tables
Base.metadata.create_all(bind=engine)
# Include routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(user.router, prefix="/api/v1/users", tags=["users"])
app.include_router(inventory.router, prefix="/api/v1/inventory", tags=["inventory"])
app.include_router(pos.router, prefix="/api/v1/pos", tags=["pos"])
app.include_router(expense.router, prefix="/api/v1/expense", tags=["expense"])
app.include_router(category.router, prefix="/api/v1/category", tags=["category"])

@app.get("/")
def read_root():
    return {"message": "Inventory and POS System"}

if __name__ == "__main__":
    import uvicorn
    print("Starting Uvicorn server on http://0.0.0.0:8000")
    print("Press Ctrl+C to stop the server")
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")