# FastAPI+Postgres Starter

## Building the project
The project runs using docker-compose and mounts the codebase in a volume inside the container. This allows for live reloading using uvicorn --reload.

## To get started:
1. `docker-compose build`
2. `docker-compose up`

## To migrate the database:
By default, the postgres db is created inside a container. The default credentials are set in local.env and are:
```
POSTGRES_PASSWORD=admin
POSTGRES_USER=development_user
POSTGRES_DB=development
```

To get started with a sample database, you can use the [northwind traders dataset](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/northwind-install), a popular test/demo database published by microsoft. Once the app is up, run:
```./seed_local_db```


## Project structure
The `src` dir contains all the code. app.py holds the main fastapi instance and config reads the env vars and exposes them in python. Each component or subservice should have its own directory inside src, including an apirouter to bind to fastapi, models, db access code, etc.

## Running in prod
The project is designed to get started locally on docker. To host in prod, you'll need a hosted, durable postgres instance. You can build the api container for use on kubernetes or something like fly.io.
