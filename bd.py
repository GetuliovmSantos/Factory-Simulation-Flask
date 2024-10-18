# conecção banco de dados
import mysql.connector

# erro de conexão
import mysql.connector.errors

from password import password


def criarConexao():
    print("Conectando ao banco de dados...")
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            port="3307",
            user="jason",
            password=password,
            database="fabrica",
        )
        print("Conexão realizada com sucesso!")
        return conexao
    except mysql.connector.errors.InterfaceError as erro:
        print("Erro de conexão: ", erro)
        return None


print(criarConexao())


def login(usuario, senha):
    user = {}

    conexao = criarConexao()
    if conexao is None:
        return "Erro de conexão"
    else:
        cursor = conexao.cursor()
        cursor.execute(
            "select * from usuarios where idUsuarios = %s and senha = %s",
            (usuario, senha),
        )
        resultado = cursor.fetchall()
        if len(resultado) > 0:
            user = {
                "idUsuarios": resultado[0][0],
                "nome": resultado[0][1],
                "funcao": resultado[0][2],
                "senha": resultado[0][3],
            }
        else:
            user = {"error": True}
        cursor.close()
        conexao.close()

    return user


def buscarProdutos(area):
    conexao = criarConexao()
    if conexao is None:
        return "Erro de conexão"
    else:
        cursor = conexao.cursor()
        cursor.execute(f"select * from produtos where area = {area}")
        resultado = cursor.fetchall()
        produtos = {}

        if len(resultado) > 0:
            for i in range(len(resultado)):
                produtos[resultado[i][0]] = {
                    "nome": resultado[i][1],
                    "quantidade": resultado[i][2],
                    "lote": resultado[i][3],
                    "data": resultado[i][4],
                }
        else:
            produtos = {"error": True}

        cursor.close()
        conexao.close()

    return produtos


def buscarProduto(idProduto):
    conexao = criarConexao()
    if conexao is None:
        return "Erro de conexão"
    else:
        cursor = conexao.cursor()
        cursor.execute(f"select * from produtos where idProdutos = {idProduto}")
        resultado = cursor.fetchall()
        produto = {}

        if len(resultado) > 0:
            produto = {
                "idProduto": resultado[0][0],
                "nome": resultado[0][1],
                "quantidade": resultado[0][2],
                "lote": resultado[0][3],
                "data": resultado[0][4],
                "area": resultado[0][5],
            }
        else:
            produto = {"error": True}

        cursor.close()
        conexao.close()

        print(produto)

    return produto


def venderProduto(idProduto, quantidade, destino):
    conexao = criarConexao()
    if conexao is None:
        return "Erro de conexão"
    else:
        cursor = conexao.cursor()

        cursor.execute(
            f"select quantidade from produtos where idProdutos = {idProduto}"
        )
        resultado = cursor.fetchall()
        # verificar se a quantidade de produtos é suficiente
        if int(quantidade) > resultado[0][0]:
            print("Quantidade insuficiente!")
            return False

        cursor.execute(
            f"insert into vendas (quantidadeVenda, dataHora, destino, idProdutos) values ({quantidade}, now(), '{destino}', {idProduto})"
        )
        cursor.execute(
            f"update produtos set quantidade = quantidade - {quantidade} where idProdutos = {idProduto}"
        )
        print("Venda realizada com sucesso!")
        conexao.commit()
        cursor.close()
        conexao.close()

        return True
