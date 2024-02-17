# import os
# import sys
# from queries.orm import create_tables, insert_data

# import uvicorn
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from queries.core import AsyncCore, SyncCore
# from queries.orm import AsyncORM, SyncORM

# sys.path.insert(1, os.path.join(sys.path[0], '..'))

# create_tables()
# # insert_data()


from typing import List

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/tasks/", response_model=schemas.TaskOut)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    try:
        db_task = models.TaskModel(**task.dict())
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail="Task creation failed")


@app.get("/tasks/{task_id}", response_model=schemas.TaskOut)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(models.TaskModel).filter(models.TaskModel.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@app.put("/tasks/{task_id}", response_model=schemas.TaskOut)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    db_task = db.query(models.TaskModel).filter(models.TaskModel.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in task.dict().items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task


@app.get("/tasks/", response_model=List[schemas.TaskOut])
def read_tasks(status: bool = None, db: Session = Depends(get_db)):
    if status is not None:
        return db.query(models.TaskModel).filter(models.TaskModel.status == status).all()
    return db.query(models.TaskModel).all()
