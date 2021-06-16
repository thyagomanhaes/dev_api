from flask import Flask, request
from flask_restful import Resource, Api
import json

from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)

developers = [
    {
        'id': 0,
        'nome': 'Rafael',
        'habilidades': ['Python', 'Flask']
     },
    {
        'id': 1,
        'nome': 'Thyago',
        'habilidades': ['Java', 'powerBI']
    }
]


class Developer(Resource):
    def get(self, id):
        try:
            response = developers[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o adm da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        data = json.loads(request.data)
        developers[id] = data
        return data

    def delete(self, id):
        developers.pop(id)
        return {'status': 'sucess', 'message': 'Register deleted'}


class ListDevelopers(Resource):
    def get(self):
        return developers


api.add_resource(Developer, '/dev/<int:id>/')
api.add_resource(ListDevelopers, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)
