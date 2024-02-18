from datetime import datetime, date
from typing import Optional, List
from pydantic import BaseModel, Field
from typing import Optional


class TasksDTO(BaseModel):
    СтатусЗакрытия: bool = Field
    ПредставлениеЗаданияНаСмену: str = Field
    Линия: str = Field
    Смена: str = Field
    Бригада: str = Field
    НомерПартии: int = Field
    ДатаПартии: date = Field
    Номенклатура: str = Field
    КодЕКН: str = Field(alias='КодЕКН')
    ИдентификаторРЦ: str = Field
    ДатаВремяНачалаСмены: datetime = Field
    ДатаВремяОкончанияСмены: datetime = Field


class TaskCreate(TasksDTO):
    pass


class TaskUpdate(TasksDTO):
    pass


class TaskOut(TasksDTO):
    id: int


class AggregateFilter(BaseModel):
    pass


class AggregateOut(BaseModel):
    pass
