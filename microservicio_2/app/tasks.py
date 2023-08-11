from app import app, db, celery
from app.models import Cancion
from celery.signals import task_postrun


@celery.task(name="tabla.registrar", bind=True)
def registrar_puntaje(self, cancion_json):
    with app.app_context():
        cancion = Cancion.query.get(cancion_json["id"])
        if cancion is None:
            cancion = Cancion(
                titulo=cancion_json["titulo"],
                minutos=cancion_json["minutos"],
                segundos=cancion_json["segundos"],
                interprete=cancion_json["interprete"],
                puntajes=[cancion_json["puntaje"]],
            )
            db.session.add(cancion)
        else:
            cancion.puntajes = cancion.puntajes + [cancion_json["puntaje"]]
        db.session.commit()


@task_postrun.connect
def close_session(*args, **kwargs):
    with app.app_context():
        db.session.remove()
