from flask import Flask, redirect, render_template, request
from bd import bd
from datetime import datetime

# Inicializa a aplicação Flask
aplication = Flask(__name__)
userInformation = {}
bd = bd()

# Rota principal(login)
@aplication.route("/")
def index():
    # Verifica se há erro na conexão com o banco de dados
    if "error" in f"{bd.connection}":
        return render_template("errorConnection.html", errorBD=bd.connection)
    else:
        return render_template("index.html", error=False)

# Rota para logar
@aplication.route("/logar", methods=["POST"])
def logar():
    global userInformation

    userID = request.form["id"]
    userPassword = request.form["password"]

    print(userID, userPassword)
    userInformation = bd.login(userID, userPassword)

    # Verifica se houve erro no login
    if "error" in userInformation:
        return render_template("login.html", error=True)
    else:
        return redirect("/storage")

# Rota para a página de armazenamento
@aplication.route("/storage")
def fabrica():
    return render_template("storage.html", user=userInformation)

# Rota para logout
@aplication.route("/logout")
def logout():
    global user
    user = {}
    return redirect("/")

# Rota para exibir produtos de uma área específica
@aplication.route("/area/<int:area>")
def areas(area):
    products = bd.searchProducts(area)
    return render_template(
        "area.html", products=products, area=area, date=datetime.now().date()
    )

# Rota para exibir detalhes para a compra de um produto
@aplication.route("/sale/<int:productID>")
def sale(productID):
    product = bd.searchOneProduct(productID)
    return render_template("sale.html", product=product, date=datetime.now().date())

# Rota para finalizar a venda de um produto
@aplication.route("/sale/<int:productID>/finish", methods=["POST"])
def finalizeSale(productID):
    quantity = request.form["quantity"]
    destination = request.form["destination"]

    saleResult = bd.sellProduct(productID, quantity, destination)
    # Verifica se a venda foi bem-sucedida
    if saleResult is True:
        return render_template("popup.html", sale=True)
    else:
        return render_template("popup.html", sale=False)

# Rota para exibir o estoque
@aplication.route("/stock")
def stock():
    allProducts = bd.allProducts()
    return render_template(
        "stock.html", allProducts=allProducts, date=datetime.now().date()
    )

# Rota para exibir o relatório de vendas
@aplication.route("/salesReport")
def salesReport():
    productsSale = bd.sales()
    return render_template("salesReport.html", productsSale=productsSale)

# Executa a aplicação Flask
if __name__ == "__main__":
    aplication.run(debug=True)
