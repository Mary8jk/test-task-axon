from sqlalchemy import (Column, Integer, String,
                        Boolean, Date, DateTime)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# для теста бд
# class TaskModel(Base):
#     __tablename__ = 'Контроль заданий на выпуск продукции'
#     id = Column(Integer, primary_key=True)
#     name = Column(String, info={'alias_name': 'Имя'})


class TaskModel(Base):
    __tablename__ = 'ВыпускПродукции'
    id = Column(Integer, primary_key=True, autoincrement=True)
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
