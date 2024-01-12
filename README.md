 # Project Description

This project demonstrates the use of SQLAlchemy, an Object-Relational Mapper (ORM), for interacting with a PostgreSQL database in Python. It showcases various SQL query techniques, including aggregations, joins, subqueries, and filtering, while utilizing Alembic for database schema management.

This project showcases the power of SQLAlchemy as an ORM for manipulating a PostgreSQL database in Python. It demonstrates various SQL queries, from aggregations and joins to subqueries and filtering, effectively bridging the gap between Python code and database operations. Alembic integration ensures smooth schema management.

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



