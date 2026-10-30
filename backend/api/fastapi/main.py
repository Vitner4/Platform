from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException


# dev mode command: fastapi dev main.py
# Адрес localhost: http://127.0.0.1:8000/
# Проверка и тесты: http://127.0.0.1:8000/docs


app = FastAPI() # приложение FastAPI
tasks = [] # хранилище задач


"""
TaskCreate - это описание того, как должна выглядеть задача. 
А task - уже конкретная задача, созданная по этому описанию.
"""

# Структура данных, которая хранит наша программа (описание задачи)
class TaskCreate(BaseModel):
    title: str
    priority: int
    completed: bool = False


# Объект класса TaskCreate (конкретная задача)
task = TaskCreate(
    title="Изучить Python",
    priority=1
)


@app.get("/") # говорит FastAPI: «Когда кто-то отправит GET-запрос по адресу /, вызови эту функцию».
def home():
    return {"message": "Привет!"}


@app.get("/tasks") # получаем все задачи
def get_tasks():
    return tasks


@app.post("/tasks") # создаём новую задачу
def create_task(task: TaskCreate):
    tasks.append(task)
    return task
