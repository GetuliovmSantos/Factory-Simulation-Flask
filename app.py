from flask import Flask, redirect, render_template, request
from bd import login

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html', erro=False)

@app.route('/logar', methods=['POST'])
def logar():
    usuario = request.form['id']
    senha = request.form['senha']
    print(usuario, senha)
    resultado = login(usuario, senha)

    if "error" in resultado:
        return render_template('login.html', erro=True)
    else:
        return redirect('/fabrica')
    

if __name__ == '__main__':
    app.run(debug=True)