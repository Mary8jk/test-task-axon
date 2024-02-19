from sqlalchemy import (Column, Integer, String,
                        Boolean, Date, DateTime)
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import UniqueConstraint

Base = declarative_base()

class TaskModel(Base):
    __tablename__ = 'ВыпускПродукции'
    id = Column(Integer, primary_key=True, autoincrement=True)
    closed_at = Column(DateTime, nullable=True, default=None)
    СтатусЗакрытия = Column(Boolean)
    ПредставлениеЗаданияНаСмену = Column(String)
    Линия = Column(String)
    Смена = Column(String)
    Бригада = Column(String)
    НомерПартии = Column(Integer, primary_key=True)
    ДатаПартии = Column(Date)
    Номенклатура = Column(String)
    КодЕКН = Column(String)
    ИдентификаторРЦ = Column(String)
    ДатаВремяНачалаСмены = Column(DateTime)
    ДатаВремяОкончанияСмены = Column(DateTime)

    __table_args__ = (
        UniqueConstraint(НомерПартии, ДатаПартии),
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.СтатусЗакрытия:
            self.closed_at = datetime.now()
        else:
            self.closed_at = None


class ProductModel(Base):
    __tablename__ = 'Продукция'
    id = Column(Integer, primary_key=True, autoincrement=True)
    УникальныйКодПродукта = Column(String, unique=True)
    НомерПартии = Column(Integer)
    ДатаПартии = Column(Date)
    is_aggregated = Column(Boolean, default=False)
    aggregated_at = Column(DateTime, nullable=True)
