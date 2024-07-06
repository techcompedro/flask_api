from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return 'hello wordl'


@app.route('/curriculo')
def show_curriculo():
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)
    