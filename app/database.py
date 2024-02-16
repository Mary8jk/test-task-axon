from sqlalchemy.orm import Session, sessionmaker, DeclarativeMeta
from sqlalchemy import create_engine, text
from config import settings

engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    pool_size=5,
    max_overflow=10,
)

session_task = sessionmaker(engine)
