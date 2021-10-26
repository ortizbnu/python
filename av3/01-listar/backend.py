from config import *
from modelo import Estagiario

@app.route("/")
def inicio():
    return 'Sistema de cadastro de Estagiarios. '+\
        '<a href="/listar_estagiarios">Operação listagem</a>'

@app.route("/listar_estagiarios")
def listar_estagiarios():
    # obter as estagiarios do cadastro
    estagiarios = db.session.query(Estagiario).all()
    # aplicar o método json que a classe Estagiario possui a cada elemento da lista
    estagiarios_em_json = [ x.json() for x in estagiarios ]
    # converter a lista do python para json
    resposta = jsonify(estagiarios_em_json)
    # PERMITIR resposta para pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # retornar...

# iniciar o servidor web
app.run(debug=True)    

# curl localhost:5000/listar_estagiarios
# 