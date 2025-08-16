from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://mary:f9kZAFptt38lI4Fkkn7gX5jnmCcl1Oaj@dpg-d2g4nnfdiees73d2kd60-a.oregon-postgres.render.com/wines_kq0l"
    # "postgresql://eiouerxs_mary:OKc^dnEz1J2O@printcopysolution.co.ke:5432/eiouerxs_wines"
    # "postgresql://mary:SWMF8zdUqxvVEWYsR3MBPG7e4eMH5E0Y@dpg-d2g4g70dl3ps73errqug-a.ohio-postgres.render.com/wines_bftr"
    # "postgresql://mary:SWMF8zdUqxvVEWYsR3MBPG7e4eMH5E0Y@dpg-d2g4g70dl3ps73errqug-a/wines_bftr"
    # "postgresql+psycopg2://postgres:admin@localhost:5432/wines"
    SECRET_KEY: str = "075d2a0566cf70b3496438a5b00dc041643f984f1072beca4d1bf984f2422779"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()