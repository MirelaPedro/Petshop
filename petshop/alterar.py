import mysql
import mysql.connector

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

colunas_funcionario = ['telefone', 'cargo', 'salario', 'cep']
colunas_proprietario= ['telefone', 'cep']
colunas_animal = ['peso', 'altura', 'idade', 'idproprietario']
colunas_banho = ['horario', 'data', 'tipo', 'valor', 'idanimal', 'idfuncionario']

def alterar(tabela, id,  modificacoes):
    index = 0

    if tabela == 'funcionario':
        colunas = colunas_funcionario
    elif tabela == 'proprietario':
        colunas = colunas_proprietario

    elif tabela == 'animal':
        colunas = colunas_animal

    elif tabela == 'banho':
        colunas = colunas_banho
        
    for i in modificacoes:
        if len(i) <= 0:
            colunas.pop(index)
            modificacoes.pop(index)
        index += 1
        
    for i in colunas:
        modificacao += f'{i} = {modificacoes[colunas.index(i)]}'

    update = f'update {tabela} set {modificacao} where id = {id}'
    cursor.execute(update)
    conexao_banco.commit()


    



