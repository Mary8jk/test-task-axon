from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel, Field


class TasksDTO(BaseModel):
    СтатусЗакрытия: bool = Field
    closed_at: Optional[datetime] = Field(default=None)
    ПредставлениеЗаданияНаСмену: str = Field
    Линия: str = Field
    Смена: str = Field
    Бригада: str = Field
    НомерПартии: int = Field
    ДатаПартии: date = Field
    Номенклатура: str = Field
    КодЕКН: str = Field
    ИдентификаторРЦ: str = Field
    ДатаВремяНачалаСмены: datetime = Field
    ДатаВремяОкончанияСмены: datetime = Field


class TaskCreate(TasksDTO):
    pass


class TaskUpdate(TasksDTO):
    pass


class TaskOut(TasksDTO):
    id: int


class ProductCreate(BaseModel):
    УникальныйКодПродукта: str
    НомерПартии: int
    ДатаПартии: date


class ProductOut(BaseModel):
    id: int
    УникальныйКодПродукта: str
    НомерПартии: int
    ДатаПартии: date
    is_aggregated: bool = False
    aggregated_at: Optional[datetime] = None
