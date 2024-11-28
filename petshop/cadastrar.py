import mysql
import mysql.connector
from tkinter import messagebox

#FAZENDO A CENXÃO DO BANCO
conexao_banco = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'clinica_petshop'
)

cursor = conexao_banco.cursor()

#UMA FUNÇÃO PARA VERIFICAR SE O ID EXISTE, MAS PODE SER USADO PARA PEGAR TODAS AS INFORMAÇÕES DE UMA TABELA DE ACORDO COM UMA OU MAIS CONDIÇÕES
def verificar(tabela, codigo):
    select= f'select* from {tabela} where codigo = {codigo}'
    cursor.execute(select)
    dados = cursor.fetchall()
    return dados

#LISTAS PARA O SISTEMA SABER QUAIS SÃO AS COLUNAS DE ACORDO COM A TABELA SELECIONADA
colunas_funcionario = ['id', 'telefone', 'cargo', 'salario', 'cep']
colunas_proprietario= ['id', 'telefone', 'cep']
colunas_animal = ['id', 'peso', 'altura', 'idade', 'idproprietario']
colunas_banho = ['id', 'horario', 'data', 'tipo', 'valor', 'idanimal', 'idfuncionario']

#FUNÇÃO PARA CADASTRAR
def cadastrar(tabela, info):
    index = 0 #é utilizado para mostrar qual é o campo vazio ao usuário
    campo = True #é utilizado para não cadastrar caso haja um campo vazio

    #CONDICIONAIS PARA ASSOCIAR AS COLUNAS CERTAS DE ACORDO COM A TABELA A TER CADASTRO
    if tabela == 'funcionario':
        colunas = colunas_funcionario
    elif tabela == 'proprietario':
        colunas = colunas_proprietario
    elif tabela == 'animal':
        colunas = colunas_animal
    elif tabela == 'banho':
        colunas = colunas_banho
    
    #CASO HAJA ALGUM CAMPO VAZIO O TKINTER DEVE MOSTRAR UMA MENSAGEM NA TELA DE CAMPO VAZIO, ele faz isso:
    for i in info: #Ao inteirar sobre a lista
        if len(i.strip()) <= 0: #verificar se a variável está vazia
            messagebox.showinfo("Campo vazio!", f"Há um campo vazio ({colunas[info.index(i)]}), preencha-o para continuar!") #se estiver vazia ele irá mostrar a mensagem na tela
            campo = False #e alterará a variável para verificação do campo para false
        index += 1 #contador do index para a coluna seguir as informações

    #VERIFICANDO SE NÃO HÁ NENHUM CAMPO VAZIO
    if campo == True:
        dados = verificar(tabela, info[0]) #pegando os dados para verificar se já não tem o id cadastrado

        if len(dados) <= 0:
            insert = f'insert into {tabela}({colunas}) values({info})'
            cursor.execute(insert)
            conexao_banco.commit()
        else:
            messagebox.showinfo("ID já cadastrado!", f"O ID ({info[0]}) já foi cadastrado!")



