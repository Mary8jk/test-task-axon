# from sqlalchemy.orm import Session, sessionmaker, DeclarativeMeta
# from sqlalchemy import create_engine, text
# from config import settings

# engine = create_engine(
#     url=settings.DATABASE_URL_psycopg,
#     echo=True,
#     pool_size=5,
#     max_overflow=10,
# )

# session_task = sessionmaker(engine)

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

# Создание URL базы данных из конфигурации
DATABASE_URL = settings.DATABASE_URL_psycopg

# Создание объекта подключения к базе данных
engine = create_engine(DATABASE_URL)

# Создание базового класса для всех моделей
Base = declarative_base()

# Создание сессии базы данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
