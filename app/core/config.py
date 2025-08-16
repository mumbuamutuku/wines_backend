from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://postgres:admin@localhost:5432/wines"
    SECRET_KEY: str = "075d2a0566cf70b3496438a5b00dc041643f984f1072beca4d1bf984f2422779"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()