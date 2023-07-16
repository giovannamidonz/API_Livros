from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O Senhir dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'título': 'Intelegicia Emocional',
        'autor': 'Daniel Goleman'
    },
    {
        'id': 3,
        'título': 'Eclesiates',
        'autor': 'Salomão'
    }
]


# consultar(todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

#Consulta(id)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
#editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livros.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
#criar
@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get.json()
    livros.append(novo_livro)
    return jsonify(livros)
# deleltar
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro():
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)
app.run(port=5000, host='localhost', debug=True)
'''
API = É um lugar para disponibilizar recrsos e/ou funcionalidades
#1 Objetivo - criar um api que disponibiliza consulta, criação, edição e exclusão de livros.
#2 URL base - localhost
#3 Endpoints -
    localhost/livros (get)
    localhost/livros (pust)
    localhost/livros/id (get)
    localhost/livros/id (put)
    localhost/livros/id (delete)
#4 quais recursos - Livros funcionalidades ou recursos 
'''
