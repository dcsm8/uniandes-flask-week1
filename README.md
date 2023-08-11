# UNIANDES FLASK WEEK 1

## Requirements
```sh
pip install gevent
```

## Start the app monolithic
```sh
cd flaskr
flask run -p 5000
```

## Start the microservice 1
```sh
cd microservicio_1
flask run -p 5001
```

## Start the microservice 2
```sh
cd microservicio_2
flask run -p 5002
```

## Start the microservice 2 worker
```sh
cd microservicio_2
celery -A app.tasks.celery worker -l info -P gevent
```

## Start the worker monolithic
```sh
celery -A tareas.tareas worker -l info -P gevent -Q logs
```

## Start flower dashboard
```sh
celery -A tareas.tareas flower
```