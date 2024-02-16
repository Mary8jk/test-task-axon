для запуска бд
pg_ctl -D /opt/homebrew/var/postgresql@14 start

создаем роль в бд:
createuser --interactive --pwprompt postgres

запускаем psql:
psql -h localhost -p 5432 -U postgres