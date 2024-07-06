#REVISÃO DE FLASK
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def primeira_pagina():
    return '<h1> minha primeira pagina </h1>'
#form
@app.route('/formulario')
def formulario():
    form ='''<h1> formulario </h1>
    <from>
        <lapel>primeiro nome:</lapel>
        <input type= "text" placeholder="digite seu primeiro nome:"> <br><br>
        <lapel>segundo nome</lapel>
        <input type="text" placeholder="digite seu segundo nome:"><br><br>
        <input type="submit" value="enviar">
    </from>'''
    return form



pessoas = [
        {
            'nome': 'pedro',
            'idade': 17,
            'email': 'pedro@gmail.com'
        },
        {
            'nome': 'ana',
            'idade': 18,
            'email': 'ana@gmail.com'
        },
        {
            'nome': 'joão',
            'idade': 16,
            'email': 'joao@gmail.com'
        },
        {
            'nome': 'mariana',
            'idade': 17,
            'email': 'mariana@gmail.com'
        },
        {
            'nome': 'carlos',
            'idade': 19,
            'email': 'carlos@gmail.com'
        },
        {
            'nome': 'fernanda',
            'idade': 20,
            'email': 'fernanda@gmail.com'
        },
        {
            'nome': 'lucas',
            'idade': 18,
            'email': 'lucas@gmail.com'
        },
        {
            'nome': 'beatriz',
            'idade': 21,
            'email': 'beatriz@gmail.com'
        },
        {
            'nome': 'gustavo',
            'idade': 22,
            'email': 'gustavo@gmail.com'
        },
        {
            'nome': 'larissa',
            'idade': 19,
            'email': 'larissa@gmail.com'
        },
        {
            'nome': 'rafael',
            'idade': 17,
            'email': 'rafael@gmail.com'
        },
        {
            'nome': 'camila',
            'idade': 18,
            'email': 'camila@gmail.com'
        },
        {
            'nome': 'thiago',
            'idade': 20,
            'email': 'thiago@gmail.com'
        },
        {
            'nome': 'isabela',
            'idade': 22,
            'email': 'isabela@gmail.com'
        },
        {
            'nome': 'felipe',
            'idade': 21,
            'email': 'felipe@gmail.com'
        }
    ]

@app.route('/v1/user/idade/<nome>', methods=['GET'])
def achar_idade(nome):
    for pessoa in pessoas:
        if  pessoa['nome'] == nome:
            return jsonify(idade= pessoa['idade'])
       
    return jsonify({'idade': 'pessoa não encontrada'}), 404


@app.route('/v1/user/consulta', methods=['GET'])
def achar_dados():
    nome = request.args.get('nome')
    email = request.args.get('email')
    for user in pessoas:
        if user['nome'] == nome or user['email'] == email:
            return jsonify(user)
        
    return jsonify({'dados não encontrada'}), 404























if __name__ == '__main__':
    app.run(debug=True)






