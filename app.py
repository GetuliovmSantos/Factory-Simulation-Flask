from flask import Flask, redirect, render_template, request
from bd import bd
from datetime import datetime

aplication = Flask(__name__)
userInformation = {}
bd = bd()


@aplication.route("/")
def index():
    if "error" in f"{bd.connection}":
        return render_template("errorConnection.html", errorBD=bd.connection)
    else:
        return render_template("index.html", error=False)


@aplication.route("/logar", methods=["POST"])
def logar():
    global userInformation

    userID = request.form["id"]
    userPassword = request.form["password"]

    print(userID, userPassword)
    userInformation = bd.login(userID, userPassword)

    if "error" in userInformation:
        return render_template("login.html", error=True)
    else:
        return redirect("/storage")


@aplication.route("/storage")
def fabrica():
    return render_template("storage.html", user=userInformation)


@aplication.route("/logout")
def logout():
    global user
    user = {}
    return redirect("/")


@aplication.route("/area/<int:area>")
def areas(area):
    products = bd.searchProducts(area)
    return render_template(
        "area.html", products=products, area=area, date=datetime.now().date()
    )


@aplication.route("/sale/<int:productID>")
def venda(productID):
    product = bd.searchOneProduct(productID)

    return render_template("sale.html", product=product, date=datetime.now().date())


@aplication.route("/sale/<int:productID>/finish", methods=["POST"])
def finalizarVenda(productID):
    quantity = request.form["quantity"]
    destination = request.form["destination"]

    saleResult = bd.sellProduct(productID, quantity, destination)
    if saleResult is True:
        return render_template("popup.html", sale=True)
    else:
        return render_template("popup.html", sale=False)


"""
@aplication.route("/relatorio")
def relatorio():
    produtos = todosProdutos()
    return render_template(
        "relatorio.html", produtos=produtos, data=datetime.now().date()
    )


@aplication.route("/vendas")
def relatorioVendas():
    produtosVendidos = vendas()
    return render_template("vendas.html", produtos=produtosVendidos)
"""

if __name__ == "__main__":
    aplication.run(debug=True)
