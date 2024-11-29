import mysql
import mysql.connector
from tkinter import messagebox

conexao_banco = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'petshop'
)

cursor = conexao_banco.cursor()

def verificar(tabela, condicao):
    select= f'select* from {tabela} where {condicao}'
    cursor.execute(select)
    dados = cursor.fetchall()
    return dados


def deletar(tabela, id):

    dados = verificar(tabela, f'id = {id}')

    if len(dados) > 0:
        delete  = f'delete from {tabela} where id = {id}'
        cursor.execute(delete)
        conexao_banco.commit()
    else:
        messagebox.showinfo('ID inexistente!', "Esse id não existe!")


