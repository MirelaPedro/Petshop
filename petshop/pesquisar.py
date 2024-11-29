import tkinter as tk
from tkinter import *
import mysql
import mysql.connector

conexao_banco = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'petshop'
)

cursor = conexao_banco.cursor()

colunas_funcionario = ['id', 'nome', 'telefone', 'cargo', 'salario', 'cep']
colunas_proprietario= ['id', 'nome', 'telefone', 'cep']
colunas_animal = ['id', 'nome', 'especie', 'raca', 'peso', 'altura', 'idade', 'cor', 'idproprietario']
colunas_banho = ['id', 'horario', 'data', 'tipo', 'valor', 'idanimal', 'idfuncionario']

def pesquisar(tabela, frame, checkboxes, termo):

    if tabela == 'funcionario':
        colunas = colunas_funcionario
        info = 'funcionario.id, funcionario.nome, funcionario.telefone, funcionario.cargo, funcionario.salario, funcionario.cep, animal.nome, banho.tipo, banho.data, banho.horário  from funcionario, animal, banho where banho.idfuncionario = funcionario.id and banho.idanimal = animal.id '
        n = 7

    elif tabela == 'proprietario':
        colunas = colunas_proprietario
        info = 'proprietario.id, proprietario.nome, proprietario.telefone, proprietario.cep, animal.id, animal.nome, banho.idanimal, banho.tipo, banho.data, banho.horário from proprietario, animal, banho where animal.idproprietario = proprietario.id and banho.idanimal = animal.id '
        n = 5

    elif tabela == 'animal':
        colunas = colunas_animal
        info = 'animal.id, animal.nome, animal.especie, animal.raca, animal.peso, animal.altura, animal.idade, animal.cor, proprietario.id, proprietaio.nome, banho.tipo, banho.data, banho.horário  from animal, proprietario, banho where animal.idproprietario = proprietario.id and banho.idanimal = animal.id '
        n = 10

    elif tabela == 'banho':
        colunas = colunas_banho
        info = 'banho.id, banho.horário, banho.data, banho.tipo, banho.valor, banho.idanimal, banho.idfuncionario, animal.nome, funcionario.nome from banho, animal, funcionario where banho.idfuncionario = funionario.id and banho.idanimal = animal.id '
        n = 8
    

    print(checkboxes)
    condicao =''
    if checkboxes[len(checkboxes) - 1] == True:
        for coluna in colunas:
            condicao += f'and {tabela}.{coluna} like "%{termo}%" '
    else:
        for index, i in enumerate(checkboxes):
            if i == True:
                    condicao += f'and {tabela}.{colunas[index]} like "%{termo}%" '
        
    select = f'select {info} {condicao}'
    print(select)

    cursor.execute(select)
    dados = cursor.fetchall()

    print(dados)

    lb_dados = tk.Label(frame, text=dados)
    lb_dados.pack()