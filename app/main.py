from typing import List

from fastapi import FastAPI, HTTPException, Depends
from fastapi import Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models import Base, TaskModel, ProductModel
from schemas import TaskCreate, TaskUpdate, TaskOut, ProductCreate, ProductOut
from filters import (apply_status_filter, apply_batch_number_filter,
                     apply_batch_date_filter, apply_pagination)
from database import SessionLocal, engine
from datetime import datetime, date

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/tasks/", response_model=TaskOut)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    try:
        db_task = TaskModel(**task.dict())
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Task creation failed")


@app.get("/tasks/{task_id}", response_model=TaskOut)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@app.put("/tasks/{task_id}", response_model=TaskOut)
def update_task(task_id: int, task: TaskUpdate,
                db: Session = Depends(get_db)):
    db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in task.dict().items():
        setattr(db_task, key, value)
    if db_task.СтатусЗакрытия:
        db_task.closed_at = datetime.now()
    else:
        db_task.closed_at = None
    db.commit()
    db.refresh(db_task)
    return db_task


@app.get("/tasks/", response_model=List[TaskOut])
def read_tasks(status: bool = Query(None),
               batch_number: int = Query(None),
               batch_date_from: date = Query(None),
               batch_date_to: date = Query(None),
               offset: int = Query(default=0, ge=0),
               limit: int = Query(default=10, le=100),
               db: Session = Depends(get_db)):
    query = db.query(TaskModel)
    if status is not None:
        query = apply_status_filter(query, status)
    if batch_number is not None:
        query = apply_batch_number_filter(query, batch_number)
    if batch_date_from is not None or batch_date_to is not None:
        query = apply_batch_date_filter(query, batch_date_from, batch_date_to)
    query = apply_pagination(query, offset, limit)
    tasks = query.all()
    return tasks


@app.post("/add_product/", response_model=List[ProductOut])
def add_products(products: List[ProductCreate], db: Session = Depends(get_db)):
    added_products = []
    existing_tasks = {}
    for product_req in products:
        existing_task = db.query(TaskModel).filter_by(
            НомерПартии=product_req.НомерПартии,
            ДатаПартии=product_req.ДатаПартии
        ).first()
        if existing_task:
            existing_tasks[product_req.УникальныйКодПродукта] = existing_task
    for product_req in products:
        if product_req.УникальныйКодПродукта in existing_tasks:
            existing_task = existing_tasks[product_req.УникальныйКодПродукта]
            existing_product = db.query(ProductModel).filter_by(
                УникальныйКодПродукта=product_req.УникальныйКодПродукта
            ).first()
            if existing_product is None:
                new_product = ProductModel(
                    УникальныйКодПродукта=product_req.УникальныйКодПродукта,
                    НомерПартии=existing_task.НомерПартии,
                    ДатаПартии=existing_task.ДатаПартии,
                    is_aggregated=False,
                    aggregated_at=None
                )
                db.add(new_product)
                added_products.append(new_product)
    db.commit()

    response_products = []
    for product in added_products:
        response_products.append(ProductOut(
            id=product.id,
            УникальныйКодПродукта=product.УникальныйКодПродукта,
            НомерПартии=product.НомерПартии,
            ДатаПартии=product.ДатаПартии,
            is_aggregated=product.is_aggregated,
            aggregated_at=product.aggregated_at
        ))
    return response_products


@app.post("/aggregate_product/{batch_id}/{unique_code}",
          response_model=ProductOut)
def aggregate_product(batch_id: int,
                      unique_code: str, db: Session = Depends(get_db)):
    product = db.query(ProductModel).filter_by(
        УникальныйКодПродукта=unique_code).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if product.НомерПартии != batch_id:
        raise HTTPException(status_code=400,
                            detail="Unique code is attached to another batch")
    if product.is_aggregated:
        raise HTTPException(
            status_code=400,
            detail=f"Unique code already used at {product.aggregated_at}")
    product.is_aggregated = True
    product.aggregated_at = datetime.now()
    db.commit()
    return product
