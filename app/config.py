from pydantic_settings import BaseSettings
from sqlalchemy.engine.url import URL

from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL_psycopg(self):
        # Строка подключения (DSN)
        return URL(
            drivername="postgresql+psycopg2",
            username=self.DB_USER,
            password=self.DB_PASS,
            host=self.DB_HOST,
            port=self.DB_PORT,
            database=self.DB_NAME,
            query={},
        )

    class Config:
        env_file = ".env"


settings = Settings()
