from flask import Flask, render_template
import jinja2

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

@app.route('/')
def index():
    return render_template('index.html',
        titulo = 'minha pagina',
        teste = False,
        links = links,
        user = user,
        media = 26
        )






if __name__ == '__main__':
    app.run(debug=True)
    