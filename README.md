# 07-Web-HW

## Run PostgresDB locally in Docker

```bash
docker pull postgres
```

```bash
docker run --name postgress -p 5432:5432 -e POSTGRES_PASSWORD=123456 -d postgres
```

## Install dependencies 

```bash
poetry install --no-root 
```

## Activate virtual environment
in the terminal
```bash
poetry shell 
```
or/and in the Pycharm IDE activate manually

## Create databases via alembic migration
```bash
alembic upgrade head
```
this will create tables according to the schemas