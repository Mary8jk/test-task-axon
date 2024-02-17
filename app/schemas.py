from datetime import datetime, date
from typing import Optional, List
from pydantic import BaseModel, Field


class TasksDTO(BaseModel):
    status: bool = Field(alias='СтатусЗакрытия')
    task: str = Field(alias='ПредставлениеЗаданияНаСмену')
    line: str
    working_shift: str
    team: str
    batch_number: int
    batch_date: date
    nomenclature: str
    code_ekn: str
    id_rc: str
    start_data: datetime
    end_data: datetime


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
