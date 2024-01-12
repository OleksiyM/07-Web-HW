 # Project Description

This project uses SQLAlchemy, an ORM, to work with a PostgreSQL database in Python. It shows how to do different SQL queries, such as aggregations, joins, subqueries, and filtering, and how to connect Python code and database actions. It also uses Alembic to manage the database schema.
## Features

* Interacts with a PostgreSQL database using SQLAlchemy.
* Executes diverse SQL queries, including:
    * Aggregations (e.g., GROUP BY, COUNT, SUM)
    * Joins (e.g., INNER JOIN, LEFT JOIN)
    * Subqueries
    * Filtering
* Manages database schema changes using Alembic.

## Installation

### Run PostgreSQL locally in the Docker

```bash
docker pull postgres
```

```bash
docker run --name postgress -p 5432:5432 -e POSTGRES_PASSWORD=123456 -d postgres
```

### Install dependencies 

```bash
poetry install --no-root 
```

### Activate virtual environment
in the terminal
```bash
poetry shell 
```
or/and in the Pycharm IDE activate manually

### Create databases via alembic migration
```bash
alembic upgrade head
```
this will create tables according to the schemas

## Usage
this command will run all queries from my_select.py
```bash
python main.py
```
You can modify main.py by adding from `print(select_1()` to `print(select_12()` at the bottom of the file

## Project Structure

* **models.py:** Defines SQLAlchemy models for entities.
* **db.py:** Establishes the database connection.
* **my_select.py:** Contains functions for executing queries.
* **main.py:** Runs the queries and prints results.
* **constants.py:** Stores constant values.
* **alembic.ini** and **alembic** folder: Manage database migrations.

## Technologies Used

* Python
* SQLAlchemy
* PostgreSQL
* Alembic
* Docker



