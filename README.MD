# Factory Backend (v2)

## Environment

Install dependencies:
```bash
pip install -r requirements.txt
```

### Local Development 

If you have python dbg installed:
```
Just Press F5 
```

Run dev mode with hot reloading:
```bash
uvicorn app.main:app --reload
```

Alembic things:
```bash
alembic revision --autogenerate
alembic upgrade head
```

### Docker Development

Build and run backend service:
```bash
docker-compose up --build       (foreground)
docker-compose up -d --build    (background)
```
   
Shut down backend service (force or Ctrl+C):
```bash
docker-compose down
```

Alembic manual revision update:
```bash
docker-compose run server alembic revision --autogenerate
docker-compose run server alembic upgrade head
```


## API Testing 

### Postman

Open Postman and click **Import** with following address (OpenAPI option):
```
http://localhost:8000/openapi.json
```

### Swagger

Fast API provides Swagger by default 
```
http://localhost:8000/docs
```


## Problems

All problems with albemic can be resolved (data wipe) by requesting:
```
http://localhost:8000/dev/repool
```
