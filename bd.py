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

    '''
    def todosProdutos(self):
        conexao = criarConexao()

        if conexao is None:
            return "Erro de conexão"
        else:
            cursor = conexao.cursor()
            cursor.execute("select * from produtos")
            resultado = cursor.fetchall()
            produtos = {}

            if len(resultado) > 0:
                for i in range(len(resultado)):
                    produtos[resultado[i][0]] = {
                        "nome": resultado[i][1],
                        "quantidade": resultado[i][2],
                        "lote": resultado[i][3],
                        "data": resultado[i][4],
                        "area": resultado[i][5],
                    }
            else:
                produtos = {"error": True}

            cursor.close()
            conexao.close()

            return produtos


    def vendas(self):
        conexao = criarConexao()

        if conexao is None:
            return "Erro de conexão"
        else:
            cursor = conexao.cursor()
            cursor.execute("select * from vendas")
            resultado = cursor.fetchall()
            vendas = {}

            if len(resultado) > 0:
                for i in range(len(resultado)):
                    cursor.execute(
                        f"select nomeProduto from produtos where idProdutos = {resultado[i][4]}"
                    )
                    nomeProduto = cursor.fetchall()
                    vendas[resultado[i][0]] = {
                        "quantidade": resultado[i][1],
                        "dataHora": resultado[i][2],
                        "destino": resultado[i][3],
                        "nomeProduto": nomeProduto[0][0],
                    }
            else:
                vendas = {"error": True}

            cursor.close()
            conexao.close()

            return vendas
'''