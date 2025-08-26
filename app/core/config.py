from pydantic_settings import BaseSettings
import os
import sys

from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str  = os.getenv("DATABASE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY") 
    ALGORITHM: str = os.getenv("ALGORITHM") 
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

    class Config:
        env_file = ".env"
settings = Settings()

# from pydantic_settings import BaseSettings
# from pydantic import Field, ValidationError
# import os
# import sys
# from typing import Optional

# class Settings(BaseSettings):
#     DATABASE_URL: str = Field(
#         default="postgresql://postgres:admin@localhost/wines",
#         description="Database connection URL"
#     )
#     SECRET_KEY: str = Field(
#         default="change-me-in-production-075d2a0566cf70b3496438a5b00dc041643f984f1072beca4d1bf984f2422779",
#         min_length=32,
#         description="Secret key for cryptographic operations"
#     )
#     ALGORITHM: str = Field(
#         default="HS256",
#         description="JWT signing algorithm"
#     )
#     ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(
#         default=30,
#         description="Token expiration time in minutes"
#     )

#     class Config:
#         env_file = ".env"  # Explicitly disable .env file loading
#         env_file_encoding = 'utf-8'
#         extra = 'ignore'

# # Initialize settings
# try:
#     settings = Settings()
# except ValidationError as e:
#     print("Configuration error:", e)
#     print("\nPlease set the required environment variables:")
#     print("- DATABASE_URL: Database connection string")
#     print("- SECRET_KEY: Cryptographic secret (min 32 chars)")
#     print("- ALGORITHM: JWT algorithm (default: HS256)")
#     print("- ACCESS_TOKEN_EXPIRE_MINUTES: Token expiry (default: 30)")
#     sys.exit(1)
