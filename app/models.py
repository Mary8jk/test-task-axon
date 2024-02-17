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
    __tablename__ = 'СтатусЗакрытия'
    status = Column(Boolean, info={'alias_name': 'СтатусЗакрытия'})
    task = Column(String, info={'alias_name': 'ПредставлениеЗаданияНаСмену'})
    line = Column(String, info={'alias_name': 'Линия'})
    working_shift = Column(String, info={'alias_name': 'Смена'})
    team = Column(String, info={'alias_name': 'Бригада'})
    batch_number = Column(Integer, primary_key=True,
                          info={'alias_name': 'НомерПартии'})
    batch_date = Column(Date, info={'alias_name': 'ДатаПартии'})
    nomenclature = Column(String, info={'alias_name': 'Номенклатура'})
    code_ekn = Column(String, info={'alias_name': 'КодЕКН'})
    id_rc = Column(String, info={'alias_name': 'ИдентификаторРЦ'})
    start_data = Column(DateTime, info={'alias_name': 'ДатаВремяНачалаСмены'})
    end_data = Column(DateTime, info={'alias_name': 'ДатаВремяОкончанияСмены'})
