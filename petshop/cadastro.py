import mysql
import mysql.connector

conexao_banco = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'clinica_petshop'
)

cursor = conexao_banco.cursor()

def verificar(tabela, codigo):
    select= f'select* from {tabela} where codigo = {codigo}'
    cursor.execute(select)
    dados = cursor.fetchall()
    return dados


