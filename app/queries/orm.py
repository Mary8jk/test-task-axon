# from database import engine, session_task
# from models import TaskModel, Base


# def create_tables():
#     Base.metadata.drop_all(engine)
#     Base.metadata.create_all(engine)


# тест бд
# def insert_data():
#     with session_task() as session:
#         t1 = TaskModel(name='Surok')
#         t2 = TaskModel(name='Kot')
#         session.add_all([t1, t2])
#         session.commit()

