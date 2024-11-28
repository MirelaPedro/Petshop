import mysql
import mysql.connector
from tkinter import messagebox

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

colunas_funcionario = ['id', 'telefone', 'cargo', 'salario', 'cep']
colunas_proprietario= ['id', 'telefone', 'cep']
colunas_animal = ['id', 'peso', 'altura', 'idade', 'idproprietario']
colunas_banho = ['id', 'horario', 'data', 'tipo', 'valor', 'idanimal', 'idfuncionario']

def cadastrar(tabela, info):
    index = 0
    campo = True

    if tabela == 'funcionario':
        colunas = colunas_funcionario
    elif tabela == 'proprietario':
        colunas = colunas_proprietario

    elif tabela == 'animal':
        colunas = colunas_animal

    elif tabela == 'banho':
        colunas = colunas_banho
        
    for i in info:
        if len(i) <= 0:
            messagebox.showinfo('Campo vazio!', "Há um campo vazio, preencha-o para continuar!")
            campo = False
        index += 1
        
    insert = f'insert into {tabela}({colunas}) values({info})'
    cursor.execute(insert)
    conexao_banco.commit()



