# conecção banco de dados
import mysql.connector

# erro de conexão
import mysql.connector.errors

from password import password


class bd:
    def __init__(self):
        self.connection = self.createConnection()

    def createConnection(self):
        print("Conectando ao banco de dados...")
        try:
            connectionBD = mysql.connector.connect(
                host="localhost",
                port="3307",
                user="jason",
                password=password,
                database="fabrica",
            )
            print("Conexão realizada com sucesso!")
            return connectionBD
        except mysql.connector.errors.ProgrammingError as erro:
            print("Erro de conexão: ", erro)
            return {"error": erro}

    def login(self, userID, userPassword):
        user = {}

        cursor = self.connection.cursor()

        cursor.execute(
            f"select * from usuarios where idUsuarios = {userID} and senha = {userPassword};"
        )
        resultado = cursor.fetchall()

        if len(resultado) > 0:
            user = {
                "userId": resultado[0][0],
                "userName": resultado[0][1],
                "userFuction": resultado[0][2],
                "userPassword": resultado[0][3],
            }
        else:
            user = {"error": True}

        cursor.close()

        return user

    def searchProducts(self, area):
        cursor = self.connection.cursor()
        cursor.execute(f"select * from produtos where area = {area}")
        resultSelect = cursor.fetchall()
        products = {}

        if len(resultSelect) > 0:
            for i in range(len(resultSelect)):
                products[resultSelect[i][0]] = {
                    "productName": resultSelect[i][1],
                    "productQuantity": resultSelect[i][2],
                    "productBatch": resultSelect[i][3],
                    "productDate": resultSelect[i][4],
                }
        else:
            products = {"error": True}

        cursor.close()

        return products

    def searchOneProduct(self, productID):
        cursor = self.connection.cursor()
        cursor.execute(f"select * from produtos where idProdutos = {productID}")
        resultSelect = cursor.fetchall()
        product = {}

        if len(resultSelect) > 0:
            product = {
                "productID": resultSelect[0][0],
                "productName": resultSelect[0][1],
                "productQuantity": resultSelect[0][2],
                "productBatch": resultSelect[0][3],
                "productDate": resultSelect[0][4],
                "productArea": resultSelect[0][5],
            }
        else:
            product = {"error": True}

        cursor.close()

        return product

    def sellProduct(self, productID, quantitySold, productDestination):
        cursor = self.connection.cursor()

        cursor.execute(
            f"select quantidade from produtos where idProdutos = {productID}"
        )
        resultSelect = cursor.fetchall()
        if int(quantitySold) > resultSelect[0][0]:
            print("Quantidade insuficiente!")
            return False

        cursor.execute(
            f"insert into vendas (quantidadeVenda, dataHora, destino, idProdutos) values ({quantitySold}, now(), '{productDestination}', {productID})"
        )
        cursor.execute(
            f"update produtos set quantidade = quantidade - {quantitySold} where idProdutos = {productID}"
        )
        self.connection.commit()
        cursor.close()

        return True

    def allProducts(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from produtos")
        resultSelect = cursor.fetchall()
        allProducts = {}

        if len(resultSelect) > 0:
            for i in range(len(resultSelect)):
                allProducts[resultSelect[i][0]] = {
                    "productName": resultSelect[i][1],
                    "productQuantity": resultSelect[i][2],
                    "productBatch": resultSelect[i][3],
                    "productDate": resultSelect[i][4],
                    "productArea": resultSelect[i][5],
                }
        else:
            allProducts = {"error": True}

        cursor.close()

        return allProducts

    def sales(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from vendas")
        resultSelect = cursor.fetchall()
        sales = {}

        if len(resultSelect) > 0:
            for i in range(len(resultSelect)):
                cursor.execute(
                    f"select nomeProduto from produtos where idProdutos = {resultSelect[i][4]}"
                )
                productName = cursor.fetchall()
                sales[resultSelect[i][0]] = {
                    "saleQuantity": resultSelect[i][1],
                    "dateTime": resultSelect[i][2],
                    "productDestination": resultSelect[i][3],
                    "productName": productName[0][0],
                }
        else:
            sales = {"error": True}

        cursor.close()

        return sales
