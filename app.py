from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {
        'nome': 'Rafael',
        'habilidades': ['Python', 'Flask']
     },
    {
        'nome': 'Thyago',
        'habiliades': ['Java', 'powerBI']
    }
]


@app.route("/dev/<int:id_dev>/", methods=['GET', 'PUT'])
def desenvolvedor(id_dev):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id_dev]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o adm da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id_dev] = dados
        return jsonify(dados)


@app.route('/dev/', methods=['GET', 'POST'])
def lista_devs():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({'status':'sucesso', 'mensagem': 'Registro inserido'})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)
