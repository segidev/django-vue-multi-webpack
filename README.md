# Only for presentation purpose

1. `npm install --save ./modules/events/frontend ./modules/person/frontend`
2. `docker compose exec api python manage.py loaddata events persons`
3. docker-compose up -d

> The package.json controls which vue **module** will be used while the settings.py decides which django **app** will be used.

Visit [http://localhost:8000/myevents/](http://localhost:8000/myevents/)

Visit [http://localhost:8080/](http://localhost:8080/)
