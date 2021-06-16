from flask_restful import Resource

lista_habilidades = ['Python', 'Flask', 'Django', 'PowerBI']


class Habilidades(Resource):
    def get(self):
        return lista_habilidades
