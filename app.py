from flask import Flask, render_template


app = Flask(__name__)


links = [
    {'nome': 'joao gomes', 'url': 'https://www.youtube.com/watch?v=cvdpUHnr_tY&themeRefresh=1' }
]

user = [
    {'nome': 'pedro', 'idade': '17'},
    {'nome': 'maria', 'idade': '22'},
    {'nome': 'joao', 'idade': '35'},
    {'nome': 'ana', 'idade': '28'},
    {'nome': 'carlos', 'idade': '40'},
    {'nome': 'beatriz', 'idade': '19'},
    {'nome': 'marcos', 'idade': '31'},
    {'nome': 'juliana', 'idade': '25'},
    {'nome': 'roberto', 'idade': '45'},
    {'nome': 'alice', 'idade': '23'},
    {'nome': 'fernando', 'idade': '29'},
    {'nome': 'camila', 'idade': '21'},
    {'nome': 'ricardo', 'idade': '33'},
    {'nome': 'leticia', 'idade': '26'},
    {'nome': 'paulo', 'idade': '37'},
    {'nome': 'daniela', 'idade': '20'},
    {'nome': 'antonio', 'idade': '48'},
    {'nome': 'sara', 'idade': '24'},
    {'nome': 'renato', 'idade': '34'},
    {'nome': 'bruna', 'idade': '18'}
]

carro = [
    {'nome': 'hilux', 'marca': 'toyota', 'cor': 'red'},
    {'nome': 'mustang', 'marca': 'ford', 'cor': 'blue'},
    {'nome': 'civic', 'marca': 'honda', 'cor': 'black'},
    {'nome': 'corolla', 'marca': 'toyota', 'cor': 'yellow'},
    {'nome': 'camaro', 'marca': 'chevrolet', 'cor': 'green'}
]

@app.route('/')
def index():
    usuarios_ordenados = sorted(user, key=lambda x: int(x['idade']), reverse=True)
    return render_template('index.html',
        titulo = 'minha pagina',
        teste = False,
        links = links,
        user = user,
        media = 26,
        usuarios_ordenados = usuarios_ordenados,
        carro = carro 
        )

@app.route('/index02.html')
def index02():
    return render_template('index02.html',
        titulo = 'my pagina',
        teste = False,
        links = links,
        user = user,
        media = 26,
        carro = carro
        )

@app.route('/index03.html')
def index03():
    usuarios_ordenados = sorted(user, key=lambda x: int(x['idade']), reverse=True)
    return render_template('index03.html',
        titulo = 'minha pagina',
        teste = False,
        links = links,
        user = user,
        media = 26,
        usuarios_ordenados = usuarios_ordenados,
        carro = carro 
        )

@app.route('/index04.html')
def index04():
    return render_template('index04.html',
        titulo = 'minha pagina',
        teste = False,
        links = links,
        user = user,
        media = 26,
        carro = carro 
        )

     
#   <h1>oi {{nome}}</h1>

#    {% if teste %}
#    <h1>entrei na condicional</h1>

#    {% else %}
#    <h1>não entrei na condicional</h1>
#    {% endif %}

#    {% for row in links %}
#       <a href="{{row.url}}" target="_blank" >{{row.nome}}</a>
#    {% endfor %}




if __name__ == '__main__':
    app.run(debug=True)
    