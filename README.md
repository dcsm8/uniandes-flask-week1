# UNIANDES FLASK WEEK 1

## Requirements
```sh
pip install gevent
```

## Start the app
```sh
cd flaskr
flask run
```

## Start the worker
```sh
celery -A flaskr.tareas.tareas worker -l info -P gevent
```

## Start flower dashboard
```sh
celery -A flaskr.tareas.tareas flower
```