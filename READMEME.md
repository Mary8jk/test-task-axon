для запуска бд
pg_ctl -D /opt/homebrew/var/postgresql@14 start

создаем роль в бд:
createuser --interactive --pwprompt postgres

запускаем psql:
psql -h localhost -p 5432 -U postgres

для миграций 

в файле env.py добавляем
from config import settings
from models import TaskModel
from database import Base
config = context.config


if config.config_file_name is not None:
    fileConfig(config.config_file_name)

config.set_main_option('sqlalchemy.url', str(settings.DATABASE_URL_psycopg))

target_metadata = Base.metadata

инициализируем миграции
alembic init mugrations

alembic revision --autogenerate

запускаем
alembic upgrade head