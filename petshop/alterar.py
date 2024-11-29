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

colunas_funcionario = ['telefone', 'cargo', 'salario', 'cep'] #str: index(1), float: index(2), int: index(0,3)
colunas_proprietario= ['telefone', 'cep'] #int: index(0,1)
colunas_animal = ['peso', 'altura', 'idade', 'idproprietario'] #float: index(0,1), int: index(2,3)
colunas_banho = ['horario', 'data', 'tipo', 'valor', 'idanimal', 'idfuncionario'] #str: index(0, 1, 2), float: index(3), int: index(4,5)

def alterando(tabela, id,  modifica):

    #Colocando a tabela correta na lista
    if tabela == 'funcionario':
        colunas = colunas_funcionario
    elif tabela == 'proprietario':
        colunas = colunas_proprietario
    elif tabela == 'animal':
        colunas = colunas_animal
    elif tabela == 'banho':
        colunas = colunas_banho

    dados = verificar(tabela,id) #pegando os dados para verificar se já não tem o id cadastrado
    print(dados)

    modificacao = ""  # Inicializa a variável 'modificacao' como uma string vazia

    for index, i in enumerate(modifica):
        print(i)  # Imprime o valor da lista 'modifica' para depuração

        if i is None:
            # Se o valor for None, não adiciona a coluna na atualização
            continue  # Pula o valor e não faz nada para esse índice

        else:
            if isinstance(i, str):
                # Para valores de texto, usar aspas simples
                value = f"'{i}'"
            else:
                # Para outros tipos de valores (como números), não usar aspas
                value = str(i)  # Converte o valor para string sem aspas
            
            # Verificando se a 'modificacao' já contém alguma coisa (não está vazia)
            if modificacao:
                modificacao += ', '  # Se não estiver vazia, adiciona uma vírgula e espaço para separar as colunas

            # Adiciona a coluna e seu novo valor à string 'modificacao'
            modificacao += f"{colunas[index]} = {value}"
            
            print(modificacao)

    update = f'update {tabela} set {modificacao} where id = {id}'
    print(update)
    cursor.execute(update)
    conexao_banco.commit()


    



