from celery import Celery
import time

celery_app = Celery(__name__, broker="redis://localhost:6379/0")


@celery_app.task()
def registrar_log(usuario, fecha):
    with open("log_signin.txt", "a+") as file:
        file.write("{} - inicio de sesion: {}\n".format(usuario, fecha))
    time.sleep(10)
