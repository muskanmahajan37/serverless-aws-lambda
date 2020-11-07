from pydantic import BaseSettings


class Settings(BaseSettings):
    prefix: str = "/api/v1"
    secret_key: str = None
    db_user: str

    class Config:
        env_file = ".env"


settings = Settings()
