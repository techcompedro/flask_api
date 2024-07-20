from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def modelofilho():
    return render_template(
        'modelofilho.html',
            
            )



if __name__ == '__main__':
    app.run(debug=True)
    