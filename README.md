# 07-Web-HW

## Run PostgresDB locally in Docker

```bash
docker pull postgres
```

```bash
docker run --name postgress -p 5432:5432 -e POSTGRES_PASSWORD=123456 -d postgres
```