#conecção banco de dados
import mysql.connector
# erro de conexão
import mysql.connector.errors

def criarConexao():
    print("Conectando ao banco de dados...")
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            port="3307",
            user="jason",
            password="derf120@",
            database="fabrica"
            )
        print("Conexão realizada com sucesso!")
        return conexao
    except mysql.connector.errors.InterfaceError as erro:
        print("Erro de conexão: ", erro)
        return None

def login(usuario, senha):
    conexao = criarConexao()
    if conexao == None:
        return "Erro de conexão"
    else:
        cursor = conexao.cursor()
        cursor.execute("select * from usuarios where idUsuarios = %s and senha = %s", (usuario, senha))
        resultado = cursor.fetchall()
        if len(resultado) > 0:
            return {
                "idUsuarios": resultado[0][0],
                "nome": resultado[0][1],
                "funcao": resultado[0][2],
                "senha": resultado[0][3]
            }
        else:
            return {
                "error": True
            }


    