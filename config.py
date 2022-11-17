from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_NAME: str
    HOST: str
    PORT: str

    class Config:
        env_file = ".env"


settings = Settings(_env_file=".env")
