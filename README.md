# Only for presentation purpose

1. `npm install`
2. `docker-compose up -d` (Wait for build)

## Add fixtures
1. `docker-compose exec api python manage.py makemigrations`
2. `docker-compose exec api python manage.py migrate`
3. `docker-compose exec api python manage.py loaddata events persons`

> The package.json controls which vue **module** will be used while the settings.py decides which django **app** will be used.

Visit [http://localhost:8000/myevents/](http://localhost:8000/myevents/)

Visit [http://localhost:8080/](http://localhost:8080/)
