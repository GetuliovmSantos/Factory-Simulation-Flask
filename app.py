from flask import Flask, redirect, render_template, request
from bd import login, buscarProdutos
from datetime import datetime

app = Flask(__name__)
user = {}

@app.route('/')
def index():
    return render_template('login.html', erro=False)

@app.route('/logar', methods=['POST'])
def logar():
    global user
    usuario = request.form['id']
    senha = request.form['senha']
    print(usuario, senha)
    user = login(usuario, senha)

    if "error" in user:
        return render_template('login.html', erro=True)
    else:
        return redirect('/armazem')

@app.route('/armazem')
def fabrica():
    return render_template('armazem.html', user=user)

@app.route('/logout')
def logout():
    global user
    user = {}
    return redirect('/')

@app.route('/area/<int:area>')
def areas(area):
    produtos = buscarProdutos(area)
    return render_template('area.html', produtos=produtos, area=area, data=datetime.now().date())

if __name__ == '__main__':
    app.run(debug=True)