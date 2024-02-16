from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class TasksDTO(BaseModel):
    status: bool
    task: str
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
