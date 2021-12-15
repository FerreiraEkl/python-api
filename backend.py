from config import *
from models import Pessoa, EstudanteDaDisciplina, Disciplina

@app.route("/<string:classe>", methods=['post'])
def incluir(classe):
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    # RECEBIMENTO DE INFORMAÇÕES
    dados = request.get_json()
    Classe = None

    if classe == "EstudanteDaDisciplina":
        Classe = EstudanteDaDisciplina

    elif classe == "Pessoa":
        Classe = Pessoa

    elif classe == "Disciplina":
        Classe = Disciplina

    try:
        # CRIA O NOVO OBJETO
        nova = Classe(**dados)
        # INSERE NOVO OBJETO
        db.session.add(nova)
        # EFETIVA A TRANSAÇÃO
        db.session.commit()
    except Exception as e:
        # RETORNAR ERRO
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")

    # CONFIGURAÇÃO DE CORS
    return resposta

@app.route("/<string:classe>/<int:id>", methods=['DELETE'])
def excluir(classe, id):
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})

    # GENERALIZANDO A ENTRADA
    Classe = None
    
    if classe == "EstudanteDaDisciplina":
        Classe = EstudanteDaDisciplina

    elif classe == "Pessoa":
        Classe = Pessoa

    elif classe == "Disciplina":
        Classe = Disciplina

    try:
        # REMOVER OBJETO COM O ID LISTADO
        Classe.query.filter(Classe.id == id).delete()
        # EFETIVAR TRANSAÇÃO
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})

    # CONFIGURAÇÃO DE CORS
    resposta.headers.add("Access-Control-Allow-Origin", "*")

    return resposta

# APLICADO GENERALIZAÇÃO DE LISTAGEM COMO SUGERIDO EM EXEMPLOS ONLINE
@app.route("/<string:classe>")
def listar(classe):
    dados = None

    if classe == "EstudanteDaDisciplina":
        dados = db.session.query(EstudanteDaDisciplina).all()

    elif classe == "Pessoa":
        dados = db.session.query(Pessoa).all()

    elif classe == "Disciplina":
        dados = db.session.query(Disciplina).all()

    # PEGA OS DADOS EM FORMATO JSON
    lista_jsons = [x.json() for x in dados]

    # TRANSFORMA A LISTA EM JSON
    resposta = jsonify(lista_jsons)

    # CONFIGURAÇÃO DE CORS
    resposta.headers.add("Access-Control-Allow-Origin", "*")

    return resposta


app.run(debug=True)
