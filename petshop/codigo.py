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

####################################CADASTRO#####################################
def cadastro():
    op = int(input('1 - Cliente \n2 - Animal \n3 - Funcionário \n4 - Antendimento \n5 - Exame \n6 - Tratamento \n7 - Estoque \n8 - Venda \n9 - Despesa \n10 - Calcular lucro do mês'))

    ########CLIENTE
    if op == 1:
        codigo = int(input('Código do cliente:'))

        dados = verificar('cliente', codigo)

        if len(dados) <= 0:
            nome = input('Nome: ')
            cpf = int(input('CPF: '))
            estado = input('Estado: ')
            cidade = input('Cidade: ')
            bairro = input('Bairro: ')
            endereco = input('Endereço: ')
            telefone = int(input('Telefone (sem caracteres e espaço): '))

            insert = f'insert into cliente(codigo, cpf, nome, estado, cidade, bairro, endereco, telefone) values({codigo}, {cpf}, "{nome}", "{estado}", "{cidade}", "{bairro}", "{endereco}", {telefone})'
            cursor.execute(insert)
            conexao_banco.commit()
            print('Cadastro realizado com sucesso!')
        else:
            print('Já existe um cliente cadastrado com esse código e suas informações são:')
            print(f'Nome: {dados[0][2]}     Cpf: {dados[0][1]}     Estado: {dados[0][3]}    Cidade: {dados[0][4]}     Bairro: {dados[0][5]}     Endereço: {dados[0][6]}    Telefone: {dados[0][7]}')

    ########ANIMAL
    elif op == 2:
        codigo = int(input('Código do animal:'))

        dados = verificar('animal', codigo)

        if len(dados) <= 0:
            nome = input('Nome: ')
            especie = int(input('Espécie: '))
            raca = input('Raça: ')
            peso = float(input('Peso: '))
            altura = float(input('Altura: '))
            idade = int(input('Idade: '))
            cor = input('Cor: ')
            codcliente = int(input('Código do cliente: '))

            insert = f'insert into animal(codigo, nome, especie, raca, peso, altura, idade, cor, codcliente) values({codigo}, "{nome}", "{especie}", "{raca}", {peso}, {altura}, {idade}, "{cor}", "{codcliente}")'
            cursor.execute(insert)
            conexao_banco.commit()
            print('Cadastro realizado com sucesso!')

        else:
            print('Já existe um animal cadastrado com esse código e suas informações são:')
            print(f'Nome: {dados[0][1]}     Espécie: {dados[0][2]}     raca: {dados[0][3]}    Peso: {dados[0][4]}     Altura: {dados[0][5]}     Idade: {dados[0][6]}    Cor: {dados[0][7]}     Código do cliente: {dados[0][8]}')

    ########FUNCIONÁRIO
    elif op == 3:
        codigo = int(input('Código do funcionário:'))

        dados = verificar('funcionário', codigo)

        if len(dados) <= 0:
            nome = input('Nome: ')
            cpf = int(input('CPF: '))
            cargo = input('cargo')
            especialidade = input('Especialidade: ')
            salario = float(input('Salário: '))
            estado = input('Estado: ')
            cidade = input('Cidade: ')
            bairro = input('Bairro: ')
            endereco = input('Endereço: ')
            telefone = int(input('Telefone (sem caracteres e espaço): '))

            insert = f'insert into cliente(codigo, cpf, nome, cargo, especialidade, salario, estado, cidade, bairro, endereco, telefone) values({codigo}, {cpf}, "{nome}", "{cargo}", "{especialidade}", {salario}, "{estado}", "{cidade}", "{bairro}", "{endereco}", {telefone})'
            cursor.execute(insert)
            conexao_banco.commit()
            print('Cadastro realizado com sucesso!')

        else:
            print('Já existe um funcionário cadastrado com esse código e suas informações são:')
            print(f'Nome: {dados[0][2]}     Cpf: {dados[0][1]}     Cargo: {dados[0][3]}     Especialidade: {dados[0][4]}     Salário: {dados[0][5]}     Estado: {dados[0][6]}    Cidade: {dados[0][7]}     Bairro: {dados[0][8]}     Endereço: {dados[0][9]}    Telefone: {dados[0][10]}')

    ########ATENDIMENTO
    elif op == 4:
        codigo = int(input('Código do atendimento:'))

        dados = verificar('atendimento', codigo)

        if len(dados) <= 0:
            tipo = input('Tipo: ')
            data = input('Data: ')
            hora = input('Hora: ')
            valor = float(input('Valor: '))
            codanimal = int(input('Código do animal: '))
            codfuncionario = int(input('codfuncionario: '))

            insert = f'insert into atendimento(codigo, tipo, data, hora, valor, codanimal, codfuncionario) values({codigo}, "{tipo}", "{data}",  "{hora}", {valor}, {codanimal}, {codfuncionario})'
            cursor.execute(insert)
            conexao_banco.commit()
            print('Cadastro realizado com sucesso!')
        else:
            print('Já existe um atendimento cadastrado com esse código e suas informações são:')
            print(f'Tipo: {dados[0][1]}     Data: {dados[0][2]}     Hora: {dados[0][3]}    Valor: {dados[0][4]}     Código do animal: {dados[0][5]}    Código do funcionário: {dados[0][6]}')

    ########EXAME
    elif op == 5:
        codigo = int(input('Código do exame:'))

        dados = verificar('exame', codigo)

        if len(dados) <= 0:
            nome = input('Nome: ')
            data = input('Data: ')
            descricao = input('Descricao: ')
            resultado = input('Resultado: ')
            valor = float(input('Valor: '))
            codatendimento = int(input('Código do atendimento: '))

            insert = f'insert into exame(codigo, nome, data, descricao, resultado, valor, codatendimento) values({codigo}, "{nome}", "{data}", "{descricao}", "{resultado}" "{valor}", "{codatendimento}")'
            cursor.execute(insert)
            conexao_banco.commit()
            print('Cadastro realizado com sucesso!')
        else:
            print('Já existe um exame cadastrado com esse código e suas informações são:')
            print(f'Nome: {dados[0][1]}     Data: {dados[0][2]}     Descricao: {dados[0][3]}    Resultado: {dados[0][4]}    Valor: {dados[0][5]}     Código de atendimento: {dados[0][6]}')

    ########TRATAMENTO
    elif op == 6:
        codigo = int(input('Código do tratamento:'))

        dados = verificar('tratamento', codigo)

        if len(dados) <= 0:
            tipo = input('Tipo: ')
            data_inicio = input('Data de início: ')
            data_fim = input('Data de fim: ')
            observacoes = input('Observações: ')
            valor = float(input('Valor: '))
            codestoque = int(input('Código de estoque: '))
            codexame = int(input('Código do Exame: '))

            insert = f'insert into tratamento(codigo, tipo, datainicio, datafim, observacoes, valor, codestoque, codexame) values({codigo}, "{tipo}", "{data_inicio}", "{data_fim}", "{observacoes}", "{valor}", "{codestoque}", {codexame})'
            cursor.execute(insert)
            conexao_banco.commit()
            print('Cadastro realizado com sucesso!')
        else:
            print('Já existe um tratamento cadastrado com esse código e suas informações são:')
            print(f'Tipo: {dados[0][1]}     Data de início: {dados[0][2]}     Data de fim: {dados[0][3]}     Observacoes: {dados[0][4]}    Valor: {dados[0][5]}     Código do Estoque: {dados[0][6]}    Código do exame: {dados[0][7]}')

        ########ESTOQUE
    elif op == 7:
        codigo = int(input('Código do estoque:'))

        dados = verificar('estoque', codigo)

        if len(dados) <= 0:
            tipo = input('Tipo: ')
            nome = input('Nome: ')
            quantidade = int(input('Quantidade'))
            valor_venda = float(input('Valor de venda: '))
            valor_compra = float(input('Valor de compra: '))

            insert = f'insert into estoque(codigo, nome, tipo, quantidade, valor_venda, valor_compra) values({codigo}, "{nome}", "{tipo}", {quantidade}, {valor_venda}, {valor_compra})'
            cursor.execute(insert)
            conexao_banco.commit()
            print('Cadastro realizado com sucesso!')

        else:
            print('Já existe um estoque cadastrado com esse código e suas informações são:')
            print(f'Tipo: {dados[0][2]}     Nome: {dados[0][1]}     Quantidade: {dados[0][3]}     Valor de venda: {dados[0][4]}     Valor de compra: {dados[0][5]}')

    ########VENDA
    elif op == 8:
        descricao = input('Descricao: ')
        valor = float(input('Valor: '))
        quantidade = int(input('Quantidade: '))
        data = input('Data: ')
        codcliente = int(input('Código do cliente: '))
        codestoque = int(input('Código de estoque: '))

        insert = f'insert into exame(codigo, descricao, valor, quantidade, data, codcliente, codestoque) values({codigo}, "{descricao}", "{valor}", {quantidade}, "{data}", {codcliente}, {codestoque})'
        cursor.execute(insert)
        conexao_banco.commit()
        print('Cadastro realizado com sucesso!')

    ########DESPESA
    elif op == 9:
        descricao = input('Descricao: ')
        valor = float(input('Valor: '))
        quantidade = int(input('Quantidade: '))
        codestoque = int(input('Código de estoque: '))

        insert = f'insert into venda(descricao, valor, quantidade, codestoque) values("{descricao}", "{valor}", {quantidade}, {codestoque})'
        cursor.execute(insert)
        conexao_banco.commit()
        print('Cadastro realizado com sucesso!')

    ########LUCRO
    elif op == 10:
        mes = input('Mês: ')
        descricao = input('Descrição: ')

        select= f'select despesa.valor, funcionario.salario from despesa, funcionario where date '
        cursor.execute(select)
        despesas = cursor.fetchall()

        select= f'select atendimento.valor, tratamento.valor, venda.valor, exame.valor from atendimento, tratamento, venda, exame where date '
        cursor.execute(select)
        receitas = cursor.fetchall()

        despesas = sum(despesas)
        receitas = sum(receitas)
        lucro = receitas - despesas

        insert = f'insert into tratamento(descricao, valor, mes) values("{descricao}", "{lucro}", "{mes}")'
        cursor.execute(insert)
        conexao_banco.commit()
        print('Cadastro realizado com sucesso!')
