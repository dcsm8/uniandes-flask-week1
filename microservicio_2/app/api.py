from flask_restful import Resource, Api
from app import app, models

api = Api(app)


class VistaTablaPuntaje(Resource):
    def get(self):
        return [models.CancionSchema().dump(ca) for ca in models.Cancion.query.all()]


api.add_resource(VistaTablaPuntaje, "/tablaPuntajes")
