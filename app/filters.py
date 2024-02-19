from sqlalchemy.orm import Query
from sqlalchemy import desc
from models import TaskModel
from datetime import date


def apply_status_filter(query: Query, status: bool = None) -> Query:
    if status is not None:
        query = query.filter(TaskModel.СтатусЗакрытия == status)
    return query


def apply_batch_number_filter(query: Query, batch_number: int = None) -> Query:
    if batch_number is not None:
        query = query.filter(TaskModel.НомерПартии == batch_number)
    return query


def apply_batch_date_filter(query: Query,
                            batch_date_from: date = None,
                            batch_date_to: date = None) -> Query:
    if batch_date_from is not None and batch_date_to is not None:
        query = query.filter(TaskModel.ДатаПартии >= batch_date_from,
                             TaskModel.ДатаПартии <= batch_date_to)
    elif batch_date_from is not None:
        query = query.filter(TaskModel.ДатаПартии >= batch_date_from)
    elif batch_date_to is not None:
        query = query.filter(TaskModel.ДатаПартии <= batch_date_to)
    return query


def apply_pagination(query: Query, offset: int = 0, limit: int = 10) -> Query:
    query = query.offset(offset).limit(limit)
    return query


def apply_sorting(query: Query, sort_by: str = None) -> Query:
    if sort_by == 'batch_number_asc':
        query = query.order_by(TaskModel.НомерПартии)
    elif sort_by == 'batch_date_desc':
        query = query.order_by(TaskModel.ДатаПартии.desc())
    return query
