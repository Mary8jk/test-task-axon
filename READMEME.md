# Система контроля заданий на выпуск продукции #

## Стек технологий ##
+ SQLAlchemy
+ fastapi

## Как запустить проект
Клонируйте репозиторий и перейдите в него в командной строке:
```
git@github.com:Mary8jk/test-task-axon.git
```

```
cd test-task-axon
```

Создайте env-file:
```python
touch .env
```

Добавьте в env-file данные:
```python
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASS=postgres
DB_NAME=postgres
```

Cоздайте и активируйте виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установите зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```


для запуска БД Posgres в отдельном окне терминала:
```
pg_ctl -D <путь_к_папке_с_базой_данных> start
```

создаем роль в бд:
```
createuser --interactive --pwprompt postgres
```

запускаем psql:
```
psql -h localhost -p 5432 -U postgres
```

(для миграций (в проекте они уже сформированы, эта информация для справки)

инициализируем миграции:
```
alembic init migrations
```

в файле env.py добавляем импорты и конфиг:
```
from config import settings
from models import TaskModel
from database import Base
```

```
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

config.set_main_option('sqlalchemy.url', str(settings.DATABASE_URL_psycopg))

target_metadata = Base.metadata
```

делаем ревизию миграций:
```
alembic revision --autogenerate
```

запускаем миграции:
```
alembic upgrade head
```
)

для запуска проекта из директории app /app:
```
uvicorn main:app --reload
```