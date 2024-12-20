import tkinter as tk
from tkinter import *
import cadastrar
import alterar
import pesquisar
import deletar

########### MENU PRINCIPAL
def voltar():
	for widget in petshop.winfo_children():
		widget.destroy()
		
	label_nome = tk.Label(petshop, text= "BEM-VINDOS A PATAS & CIA", font="Arial 65 bold", bg="lightblue", fg="#000842")
	label_nome.pack()
	label_nome.place(relx=0.5, rely=0.2, anchor="center")

	texto = tk.Label(petshop, text="O QUE VOCÊ DESEJA FAZER?", font="Arial 45", bg="lightblue", fg="#000842")
	texto.place(relx=0.5, rely=0.3, anchor="center")
	
 ########################## FUNCIONÁRIO  
	texto_1 = tk.Label(petshop, text="CONFIGURAR FUNCIONÁRIO:", font="Arial 20 bold", bg="lightblue", fg="#000842")
	texto_1.place(relx=0.25, rely=0.45, anchor="center")
	
	botao_cadastro = tk.Button(petshop, text="CADASTRAR", fg="#000842", width='15', height='3', font="Arial 15 bold", command=cadastrar_funcionario)
	botao_cadastro.place(relx=0.1, rely=0.55, anchor="center")

	botao_atendimento = tk.Button(petshop, text="EXCLUIR", fg="#000842", width='15', height='3', font="Arial 15 bold", command=excluir_funcionario)
	botao_atendimento.place(relx=0.2, rely=0.55, anchor="center")

	botao_funcionario= tk.Button(petshop, text="ALTERAR", fg="#000842", width='15', height='3', font="Arial 15 bold", command=alterar_funcionario)
	botao_funcionario.place(relx=0.3, rely=0.55, anchor="center")

	botao_financas= tk.Button(petshop, text="PESQUISAR", fg="#000842", width='15', height='3', font="Arial 15 bold", command=pesquisar_funcionario)
	botao_financas.place(relx=0.4, rely=0.55, anchor="center")

	botao_cadastro.bind("<Enter>", lambda event: botao_cadastro.config(bg='#000842', fg='white'))
	botao_cadastro.bind("<Leave>", lambda event: botao_cadastro.config(bg='white', fg='#000842',))

	botao_atendimento.bind("<Enter>", lambda event: botao_atendimento.config(bg='#000842', fg='white'))
	botao_atendimento.bind("<Leave>", lambda event: botao_atendimento.config(bg='white', fg='#000842',))

	botao_funcionario.bind("<Enter>", lambda event: botao_funcionario.config(bg='#000842', fg='white'))
	botao_funcionario.bind("<Leave>", lambda event: botao_funcionario.config(bg='white', fg='#000842',))

	botao_financas.bind("<Enter>", lambda event: botao_financas.config(bg='#000842', fg='white'))
	botao_financas.bind("<Leave>", lambda event: botao_financas.config(bg='white', fg='#000842',))
	
########################## CLIENTES
	texto_1 = tk.Label(petshop, text="CONFIGURAR PROPRIETÁRIO:", font="Arial 20 bold", bg="lightblue", fg="#000842")
	texto_1.place(relx=0.75, rely=0.45, anchor="center")
	
	botao_cadastro1 = tk.Button(petshop, text="CADASTRAR", fg="#000842", width='15', height='3', font="Arial 15 bold", command=cadastrar_clientes)
	botao_cadastro1.place(relx=0.6, rely=0.55, anchor="center")

	botao_atendimento1 = tk.Button(petshop, text="EXCLUIR", fg="#000842", width='15', height='3', font="Arial 15 bold", command=excluir_clientes)
	botao_atendimento1.place(relx=0.7, rely=0.55, anchor="center")

	botao_funcionario1= tk.Button(petshop, text="ALTERAR", fg="#000842", width='15', height='3', font="Arial 15 bold", command=alterar_clientes)
	botao_funcionario1.place(relx=0.8, rely=0.55, anchor="center")

	botao_financas1= tk.Button(petshop, text="PESQUISAR", fg="#000842", width='15', height='3', font="Arial 15 bold", command=pesquisar_clientes)
	botao_financas1.place(relx=0.9, rely=0.55, anchor="center")

	botao_cadastro1.bind("<Enter>", lambda event: botao_cadastro1.config(bg='#000842', fg='white'))
	botao_cadastro1.bind("<Leave>", lambda event: botao_cadastro1.config(bg='white', fg='#000842',))

	botao_atendimento1.bind("<Enter>", lambda event: botao_atendimento1.config(bg='#000842', fg='white'))
	botao_atendimento1.bind("<Leave>", lambda event: botao_atendimento1.config(bg='white', fg='#000842',))

	botao_funcionario1.bind("<Enter>", lambda event: botao_funcionario1.config(bg='#000842', fg='white'))
	botao_funcionario1.bind("<Leave>", lambda event: botao_funcionario1.config(bg='white', fg='#000842',))

	botao_financas1.bind("<Enter>", lambda event: botao_financas1.config(bg='#000842', fg='white'))
	botao_financas1.bind("<Leave>", lambda event: botao_financas1.config(bg='white', fg='#000842',))


#################### ANIMAIS
	texto_3 = tk.Label(petshop, text="CONFIGURAR ANIMAIS:", font="Arial 20 bold", bg="lightblue", fg="#000832")
	texto_3.place(relx=0.75, rely=0.75, anchor="center")
	
	botao_cadastro3 = tk.Button(petshop, text="CADASTRAR", fg="#000832", width='15', height='3', font="Arial 15 bold", command=cadastrar_animais)
	botao_cadastro3.place(relx=0.6, rely=0.85, anchor="center")

	botao_atendimento3 = tk.Button(petshop, text="EXCLUIR", fg="#000832", width='15', height='3', font="Arial 15 bold", command=excluir_animais)
	botao_atendimento3.place(relx=0.7, rely=0.85, anchor="center")

	botao_funcionario3= tk.Button(petshop, text="ALTERAR", fg="#000832", width='15', height='3', font="Arial 15 bold", command=alterar_animais)
	botao_funcionario3.place(relx=0.8, rely=0.85, anchor="center")

	botao_financas3= tk.Button(petshop, text="PESQUISAR", fg="#000832", width='15', height='3', font="Arial 15 bold", command=pesquisar_animal)
	botao_financas3.place(relx=0.9, rely=0.85, anchor="center")

	botao_cadastro3.bind("<Enter>", lambda event: botao_cadastro3.config(bg='#000832', fg='white'))
	botao_cadastro3.bind("<Leave>", lambda event: botao_cadastro3.config(bg='white', fg='#000832',))

	botao_atendimento3.bind("<Enter>", lambda event: botao_atendimento3.config(bg='#000832', fg='white'))
	botao_atendimento3.bind("<Leave>", lambda event: botao_atendimento3.config(bg='white', fg='#000832',))

	botao_funcionario3.bind("<Enter>", lambda event: botao_funcionario3.config(bg='#000832', fg='white'))
	botao_funcionario3.bind("<Leave>", lambda event: botao_funcionario3.config(bg='white', fg='#000832',))

	botao_financas3.bind("<Enter>", lambda event: botao_financas3.config(bg='#000832', fg='white'))
	botao_financas3.bind("<Leave>", lambda event: botao_financas3.config(bg='white', fg='#000842',))


##############################BANHO E TOSA
	texto_4 = tk.Label(petshop, text="CONFIGURAR BANHO E TOSA:", font="Arial 20 bold", bg="lightblue", fg="#000842")
	texto_4.place(relx=0.25, rely=0.75, anchor="center")
	
	botao_cadastro4 = tk.Button(petshop, text="CADASTRAR", fg="#000842", width='15', height='4', font="Arial 15 bold", command=cadastrar_banho)
	botao_cadastro4.place(relx=0.1, rely=0.85, anchor="center")

	botao_atendimento4 = tk.Button(petshop, text="EXCLUIR", fg="#000842", width='15', height='4', font="Arial 15 bold", command=excluir_banho)
	botao_atendimento4.place(relx=0.2, rely=0.85, anchor="center")

	botao_funcionario4= tk.Button(petshop, text="ALTERAR", fg="#000842", width='15', height='4', font="Arial 15 bold", command=alterar_banho)
	botao_funcionario4.place(relx=0.3, rely=0.85, anchor="center")

	botao_financas4= tk.Button(petshop, text="PESQUISAR", fg="#000842", width='15', height='4', font="Arial 15 bold", command=pesquisar_banho)
	botao_financas4.place(relx=0.4, rely=0.85, anchor="center")

	botao_cadastro4.bind("<Enter>", lambda event: botao_cadastro4.config(bg='#000842', fg='white'))
	botao_cadastro4.bind("<Leave>", lambda event: botao_cadastro4.config(bg='white', fg='#000842',))

	botao_atendimento4.bind("<Enter>", lambda event: botao_atendimento4.config(bg='#000842', fg='white'))
	botao_atendimento4.bind("<Leave>", lambda event: botao_atendimento4.config(bg='white', fg='#000842',))

	botao_funcionario4.bind("<Enter>", lambda event: botao_funcionario4.config(bg='#000842', fg='white'))
	botao_funcionario4.bind("<Leave>", lambda event: botao_funcionario4.config(bg='white', fg='#000842',))

	botao_financas4.bind("<Enter>", lambda event: botao_financas4.config(bg='#000842', fg='white'))
	botao_financas4.bind("<Leave>", lambda event: botao_financas4.config(bg='white', fg='#000842',))

##############DEF'S CADASTRAR
#
def cadastro(tabela, info):
	print(tabela)
	print(info)

def cadastrar_funcionario():
	for widget in petshop.winfo_children():
		widget.destroy()

	texto = tk.Label(petshop, text="CADASTRO FUNCIONÁRIOS", font="Arial 30 bold", bg="lightblue", fg="#000842")
	texto.pack()
	texto.place(relx=0.5, rely=0.1, anchor="center")

	codigo = tk.Label(petshop, text="ID: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	codigo.pack()
	codigo.place(relx=0.4, rely=0.2, anchor="center")
	caixa_codigo = tk.Entry(petshop, width=75)
	caixa_codigo.pack()
	caixa_codigo.place(relx=0.55, rely=0.2, anchor="center")

	nome = tk.Label(petshop, text="NOME: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	nome.pack()
	nome.place(relx=0.4, rely=0.25, anchor="center")
	caixa_nome = tk.Entry(petshop, width=75)
	caixa_nome.pack()
	caixa_nome.place(relx=0.55, rely=0.25, anchor="center")

	telefone = tk.Label(petshop, text="TELEFONE: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	telefone.pack()
	telefone.place(relx=0.4, rely=0.3, anchor="center")
	caixa_telefone = tk.Entry(petshop, width=70)
	caixa_telefone.pack()
	caixa_telefone.place(relx=0.555, rely=0.3, anchor="center")

	cargo = tk.Label(petshop, text="CARGO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	cargo.pack()
	cargo.place(relx=0.4, rely=0.35, anchor="center")
	caixa_cargo = tk.Entry(petshop, width=75)
	caixa_cargo.pack()
	caixa_cargo.place(relx=0.55, rely=0.35, anchor="center")

	salario = tk.Label(petshop, text="SALÁRIO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	salario.pack()
	salario.place(relx=0.4, rely=0.4, anchor="center")
	caixa_salario = tk.Entry(petshop, width=73)
	caixa_salario.pack()
	caixa_salario.place(relx=0.55, rely=0.4, anchor="center")

	cep = tk.Label(petshop, text="CEP: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	cep.pack()
	cep.place(relx=0.4, rely=0.45, anchor="center")
	caixa_cep = tk.Entry(petshop, width=75)
	caixa_cep.pack()
	caixa_cep.place(relx=0.55, rely=0.45, anchor="center")


	botao_cadastrar= tk.Button(petshop, text="CADASTRAR", width='20', height='0', font="Arial 10 bold", fg="#000842", command= lambda: cadastrar.cadastrar('funcionario', info = [int(caixa_codigo.get()), caixa_nome.get(), int(caixa_telefone.get()) ,caixa_cargo.get(), float(caixa_salario.get()), int(caixa_cep.get())]))
	botao_cadastrar.pack()
	botao_cadastrar.place(relx=0.4, rely=0.6, anchor="center")


	botao_cadastrar.bind("<Enter>", lambda event: botao_cadastrar.config(bg='#000842', fg='white'))
	botao_cadastrar.bind("<Leave>", lambda event: botao_cadastrar.config(bg='white', fg='#000842',))

	botao_limpar = tk.Button(petshop, text="LIMPAR", width='20', height='0', font="Arial 10 bold", fg="#000842")
	botao_limpar.pack()
	botao_limpar.place(relx=0.5, rely=0.6, anchor="center")

	botao_limpar.bind("<Enter>", lambda event: botao_limpar.config(bg='#000842', fg='white'))
	botao_limpar.bind("<Leave>", lambda event: botao_limpar.config(bg='white', fg='#000842',))

	botao_voltar = tk.Button(petshop, text="VOLTAR AO MENU", width='20', height='0', font="Arial 10 bold", fg="#000842", command=voltar)
	botao_voltar.pack()
	botao_voltar.place(relx=0.6, rely=0.6, anchor="center")

	botao_voltar.bind("<Enter>", lambda event: botao_voltar.config(bg='#000842', fg='white'))
	botao_voltar.bind("<Leave>", lambda event: botao_voltar.config(bg='white', fg='#000842',))

def cadastrar_clientes():
	for widget in petshop.winfo_children():
		widget.destroy()

	texto = tk.Label(petshop, text="CADASTRO DE PROPRIETÁRIOS", font="Arial 30 bold", bg="lightblue", fg="#000842")
	texto.pack()
	texto.place(relx=0.5, rely=0.1, anchor="center")

	codigo = tk.Label(petshop, text="CÓDIGO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	codigo.pack()
	codigo.place(relx=0.4, rely=0.2, anchor="center")
	caixa_codigo = tk.Entry(petshop, width=75)
	caixa_codigo.pack()
	caixa_codigo.place(relx=0.55, rely=0.2, anchor="center")

	nome = tk.Label(petshop, text="NOME: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	nome.pack()
	nome.place(relx=0.4, rely=0.25, anchor="center")
	caixa_nome = tk.Entry(petshop, width=75)
	caixa_nome.pack()
	caixa_nome.place(relx=0.55, rely=0.25, anchor="center")

	telefone = tk.Label(petshop, text="TELEFONE: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	telefone.pack()
	telefone.place(relx=0.4, rely=0.3, anchor="center")
	caixa_telefone = tk.Entry(petshop, width=70)
	caixa_telefone.pack()
	caixa_telefone.place(relx=0.56, rely=0.3, anchor="center")

	cep = tk.Label(petshop, text="CEP: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	cep.pack()
	cep.place(relx=0.4, rely=0.35, anchor="center")
	caixa_cep = tk.Entry(petshop, width=75)
	caixa_cep.pack()
	caixa_cep.place(relx=0.55, rely=0.35, anchor="center")

	botao_cadastrar = tk.Button(petshop, text="CADASTRAR", width='20', height='0', font="Arial 10 bold", fg="#000842", command= lambda: cadastrar.cadastrar('proprietario', info = [int(caixa_codigo.get()), caixa_nome.get(), int(caixa_telefone.get()), int(caixa_cep.get())]))
	botao_cadastrar.pack()
	botao_cadastrar.place(relx=0.4, rely=0.4, anchor="center")

	botao_cadastrar.bind("<Enter>", lambda event: botao_cadastrar.config(bg='#000842', fg='white'))
	botao_cadastrar.bind("<Leave>", lambda event: botao_cadastrar.config(bg='white', fg='#000842',))

	botao_limpar = tk.Button(petshop, text="LIMPAR", width='20', height='0', font="Arial 10 bold", fg="#000842")
	botao_limpar.pack()
	botao_limpar.place(relx=0.5, rely=0.4, anchor="center")

	botao_limpar.bind("<Enter>", lambda event: botao_limpar.config(bg='#000842', fg='white'))
	botao_limpar.bind("<Leave>", lambda event: botao_limpar.config(bg='white', fg='#000842',))

	botao_voltar = tk.Button(petshop, text="VOLTAR AO MENU", width='20', height='0', font="Arial 10 bold", fg="#000842", command=voltar)
	botao_voltar.pack()
	botao_voltar.place(relx=0.6, rely=0.4, anchor="center")

	botao_voltar.bind("<Enter>", lambda event: botao_voltar.config(bg='#000842', fg='white'))
	botao_voltar.bind("<Leave>", lambda event: botao_voltar.config(bg='white', fg='#000842',))

def cadastrar_banho():
	for widget in petshop.winfo_children():
		widget.destroy()

	texto = tk.Label(petshop, text="CADASTRAR DE BANHO E TOSA", font="Arial 30 bold", bg="lightblue", fg="#000842")
	texto.pack()
	texto.place(relx=0.5, rely=0.1, anchor="center")

	codigo = tk.Label(petshop, text="CÓDIGO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	codigo.pack()
	codigo.place(relx=0.4, rely=0.2, anchor="center")
	caixa_codigo = tk.Entry(petshop, width=75)
	caixa_codigo.pack()
	caixa_codigo.place(relx=0.55, rely=0.2, anchor="center")

	data = tk.Label(petshop, text="DATA: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	data.pack()
	data.place(relx=0.4, rely=0.25, anchor="center")
	caixa_data = tk.Entry(petshop, width=73)
	caixa_data.pack()
	caixa_data.place(relx=0.55, rely=0.25, anchor="center")

	horario = tk.Label(petshop, text="HORÁRIO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	horario.pack()
	horario.place(relx=0.4, rely=0.3, anchor="center")
	caixa_horario = tk.Entry(petshop, width=75)
	caixa_horario.pack()
	caixa_horario.place(relx=0.55, rely=0.3, anchor="center")

	tipo = tk.Label(petshop, text="TIPO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	tipo.pack()
	tipo.place(relx=0.4, rely=0.35, anchor="center")
	caixa_tipo = tk.Entry(petshop, width=75)
	caixa_tipo.pack()
	caixa_tipo.place(relx=0.55, rely=0.35, anchor="center")

	valor = tk.Label(petshop, text="VALOR: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	valor.pack()
	valor.place(relx=0.4, rely=0.4, anchor="center")
	caixa_valor = tk.Entry(petshop, width=75)
	caixa_valor.pack()
	caixa_valor.place(relx=0.55, rely=0.4, anchor="center")

	idanimal = tk.Label(petshop, text="IDANIMAL: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	idanimal.pack()
	idanimal.place(relx=0.4, rely=0.45, anchor="center")
	caixa_idanimal = tk.Entry(petshop, width=68)
	caixa_idanimal.pack()
	caixa_idanimal.place(relx=0.56, rely=0.45, anchor="center")

	idfuncionario = tk.Label(petshop, text="IDFUNCIONÁRIO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	idfuncionario.pack()
	idfuncionario.place(relx=0.4, rely=0.5, anchor="center")
	caixa_idfuncionario = tk.Entry(petshop, width=60)
	caixa_idfuncionario.pack()
	caixa_idfuncionario.place(relx=0.57, rely=0.5, anchor="center")

	botao_cadastrar = tk.Button(petshop, text="CADASTRAR", width='20', height='0', font="Arial 10 bold", fg="#000842", command= lambda: cadastrar.cadastrar('banho', info = [int(caixa_codigo.get()), caixa_data.get(), caixa_horario.get(), caixa_tipo.get(), float(caixa_valor.get()), int(caixa_idanimal.get()), int(caixa_idfuncionario.get())]))
	botao_cadastrar.pack()
	botao_cadastrar.place(relx=0.4, rely=0.6, anchor="center")

	botao_cadastrar.bind("<Enter>", lambda event: botao_cadastrar.config(bg='#000842', fg='white'))
	botao_cadastrar.bind("<Leave>", lambda event: botao_cadastrar.config(bg='white', fg='#000842',))

	botao_limpar = tk.Button(petshop, text="LIMPAR", width='20', height='0', font="Arial 10 bold", fg="#000842")
	botao_limpar.pack()
	botao_limpar.place(relx=0.5, rely=0.6, anchor="center")

	botao_limpar.bind("<Enter>", lambda event: botao_limpar.config(bg='#000842', fg='white'))
	botao_limpar.bind("<Leave>", lambda event: botao_limpar.config(bg='white', fg='#000842',))

	botao_voltar = tk.Button(petshop, text="VOLTAR AO MENU", width='20', height='0', font="Arial 10 bold", fg="#000842", command=voltar)
	botao_voltar.pack()
	botao_voltar.place(relx=0.6, rely=0.6, anchor="center")

	botao_voltar.bind("<Enter>", lambda event: botao_voltar.config(bg='#000842', fg='white'))
	botao_voltar.bind("<Leave>", lambda event: botao_voltar.config(bg='white', fg='#000842',))

def cadastrar_animais():
	for widget in petshop.winfo_children():
		widget.destroy()

	texto_estoque = tk.Label(petshop, text="CADASTRO DO ANIMAL", font="Arial 30 bold", bg="lightblue", fg="#000842")
	texto_estoque.pack()
	texto_estoque.place(relx=0.5, rely=0.1, anchor="center")

	codigo = tk.Label(petshop, text="CÓDIGO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	codigo.pack()
	codigo.place(relx=0.4, rely=0.2, anchor="center")
	caixa_codigo = tk.Entry(petshop, width=75)
	caixa_codigo.pack()
	caixa_codigo.place(relx=0.55, rely=0.2, anchor="center")

	especie = tk.Label(petshop, text="ESPÉCIE: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	especie.pack()
	especie.place(relx=0.4, rely=0.25, anchor="center")
	caixa_especie = tk.Entry(petshop, width=75)
	caixa_especie.pack()
	caixa_especie.place(relx=0.55, rely=0.25, anchor="center")

	raca = tk.Label(petshop, text="RAÇA: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	raca.pack()
	raca.place(relx=0.4, rely=0.3, anchor="center")
	caixa_raca = tk.Entry(petshop, width=75)
	caixa_raca.pack()
	caixa_raca.place(relx=0.55, rely=0.3, anchor="center")

	nome = tk.Label(petshop, text="NOME: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	nome.pack()
	nome.place(relx=0.4, rely=0.35, anchor="center")
	caixa_nome = tk.Entry(petshop, width=75)
	caixa_nome.pack()
	caixa_nome.place(relx=0.55, rely=0.35, anchor="center")

	peso = tk.Label(petshop, text="PESO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	peso.pack()
	peso.place(relx=0.4, rely=0.4, anchor="center")
	caixa_peso = tk.Entry(petshop, width=68)
	caixa_peso.pack()
	caixa_peso.place(relx=0.56, rely=0.4, anchor="center")

	altura = tk.Label(petshop, text="ALTURA: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	altura.pack()
	altura.place(relx=0.4, rely=0.45, anchor="center")
	caixa_altura = tk.Entry(petshop, width=60)
	caixa_altura.pack()
	caixa_altura.place(relx=0.57, rely=0.45, anchor="center")

	idade = tk.Label(petshop, text="IDADE: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	idade.pack()
	idade.place(relx=0.4, rely=0.5, anchor="center")
	caixa_idade = tk.Entry(petshop, width=60)
	caixa_idade.pack()
	caixa_idade.place(relx=0.57, rely=0.5, anchor="center")

	cor = tk.Label(petshop, text="COR: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	cor.pack()
	cor.place(relx=0.4, rely=0.55, anchor="center")
	caixa_cor = tk.Entry(petshop, width=60)
	caixa_cor.pack()
	caixa_cor.place(relx=0.57, rely=0.55, anchor="center")

	idproprietario = tk.Label(petshop, text="IDPROPRIETÁRIO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	idproprietario.pack()
	idproprietario.place(relx=0.4, rely=0.6, anchor="center")
	caixa_idproprietario = tk.Entry(petshop, width=60)
	caixa_idproprietario.pack()
	caixa_idproprietario.place(relx=0.57, rely=0.6, anchor="center")


	botao_cadastrar = tk.Button(petshop, text="CADASTRAR", width='20', height='0', font="Arial 10 bold", fg="#000842", command= lambda: cadastrar.cadastrar('animal', info = [int(caixa_codigo.get()), caixa_nome.get(), caixa_especie.get(), caixa_raca.get(), float(caixa_peso.get()), float(caixa_altura.get()), int(caixa_idade.get()), caixa_cor.get(), int(caixa_idproprietario.get())]))
	botao_cadastrar.pack()
	botao_cadastrar.place(relx=0.4, rely=0.65, anchor="center")

	botao_cadastrar.bind("<Enter>", lambda event: botao_cadastrar.config(bg='#000842', fg='white'))
	botao_cadastrar.bind("<Leave>", lambda event: botao_cadastrar.config(bg='white', fg='#000842',))

	botao_limpar = tk.Button(petshop, text="LIMPAR", width='20', height='0', font="Arial 10 bold", fg="#000842")
	botao_limpar.pack()
	botao_limpar.place(relx=0.5, rely=0.65, anchor="center")

	botao_limpar.bind("<Enter>", lambda event: botao_limpar.config(bg='#000842', fg='white'))
	botao_limpar.bind("<Leave>", lambda event: botao_limpar.config(bg='white', fg='#000842',))

	botao_voltar = tk.Button(petshop, text="VOLTAR AO MENU", width='20', height='0', font="Arial 10 bold", fg="#000842", command=voltar)
	botao_voltar.pack()
	botao_voltar.place(relx=0.6, rely=0.65, anchor="center")

	botao_voltar.bind("<Enter>", lambda event: botao_voltar.config(bg='#000842', fg='white'))
	botao_voltar.bind("<Leave>", lambda event: botao_voltar.config(bg='white', fg='#000842',))


###############DEF'S ALTERAR

def alterar_funcionario():
	for widget in petshop.winfo_children():
		widget.destroy()

	texto= tk.Label(petshop, text="ALTERAÇÃO NO FUNCIONÁRIO", font="Arial 30 bold", bg="lightblue", fg="#000842")
	texto.pack()
	texto.place(relx=0.5, rely=0.1, anchor="center")

	codigo = tk.Label(petshop, text="ID DE ALTERAÇÃO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	codigo.pack()
	codigo.place(relx=0.4, rely=0.2, anchor="center")
	caixa_codigo = tk.Entry(petshop, width=60)
	caixa_codigo.pack()
	caixa_codigo.place(relx=0.57, rely=0.2, anchor="center")

	telefone = tk.Label(petshop, text="TELEFONE: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	telefone.pack()
	telefone.place(relx=0.4, rely=0.3, anchor="center")
	caixa_telefone = tk.Entry(petshop, width=70)
	caixa_telefone.pack()
	caixa_telefone.place(relx=0.555, rely=0.3, anchor="center")

	cargo = tk.Label(petshop, text="CARGO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	cargo.pack()
	cargo.place(relx=0.4, rely=0.35, anchor="center")
	caixa_cargo = tk.Entry(petshop, width=75)
	caixa_cargo.pack()
	caixa_cargo.place(relx=0.55, rely=0.35, anchor="center")

	salario = tk.Label(petshop, text="SALÁRIO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	salario.pack()
	salario.place(relx=0.4, rely=0.4, anchor="center")
	caixa_salario = tk.Entry(petshop, width=73)
	caixa_salario.pack()
	caixa_salario.place(relx=0.55, rely=0.4, anchor="center")

	cep = tk.Label(petshop, text="CEP: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	cep.pack()
	cep.place(relx=0.4, rely=0.45, anchor="center")
	caixa_cep = tk.Entry(petshop, width=75)
	caixa_cep.pack()
	caixa_cep.place(relx=0.55, rely=0.45, anchor="center")

	botao_cadastrar= tk.Button(petshop, text="ALTERAR", width='20', height='0', font="Arial 10 bold", fg="#000842", command= lambda: alterar.alterando('funcionario', int(caixa_codigo.get()) if caixa_codigo.get() else None, modifica= [int(caixa_telefone.get()) if caixa_telefone.get() else None, caixa_cargo.get() if caixa_cargo.get() else None, float(caixa_salario.get()) if caixa_salario.get() else None, int(caixa_cep.get()) if caixa_cep.get() else None]))

	botao_cadastrar.pack()
	botao_cadastrar.place(relx=0.4, rely=0.6, anchor="center")


	botao_cadastrar.bind("<Enter>", lambda event: botao_cadastrar.config(bg='#000842', fg='white'))
	botao_cadastrar.bind("<Leave>", lambda event: botao_cadastrar.config(bg='white', fg='#000842',))

	botao_limpar = tk.Button(petshop, text="LIMPAR", width='20', height='0', font="Arial 10 bold", fg="#000842")
	botao_limpar.pack()
	botao_limpar.place(relx=0.5, rely=0.6, anchor="center")

	botao_limpar.bind("<Enter>", lambda event: botao_limpar.config(bg='#000842', fg='white'))
	botao_limpar.bind("<Leave>", lambda event: botao_limpar.config(bg='white', fg='#000842',))

	botao_voltar = tk.Button(petshop, text="VOLTAR AO MENU", width='20', height='0', font="Arial 10 bold", fg="#000842", command=voltar)
	botao_voltar.pack()
	botao_voltar.place(relx=0.6, rely=0.6, anchor="center")

	botao_voltar.bind("<Enter>", lambda event: botao_voltar.config(bg='#000842', fg='white'))
	botao_voltar.bind("<Leave>", lambda event: botao_voltar.config(bg='white', fg='#000842',))

def alterar_clientes():
	for widget in petshop.winfo_children():
		widget.destroy()

	texto = tk.Label(petshop, text="ALTERAÇÃO DO CLIENTE", font="Arial 30 bold", bg="lightblue", fg="#000842")
	texto.pack()
	texto.place(relx=0.5, rely=0.1, anchor="center")

	codigo = tk.Label(petshop, text="ID DE ALTERAÇÃO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	codigo.pack()
	codigo.place(relx=0.4, rely=0.2, anchor="center")
	caixa_codigo = tk.Entry(petshop, width=65)
	caixa_codigo.pack()
	caixa_codigo.place(relx=0.57, rely=0.2, anchor="center")

	telefone = tk.Label(petshop, text="TELEFONE: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	telefone.pack()
	telefone.place(relx=0.4, rely=0.3, anchor="center")
	caixa_telefone = tk.Entry(petshop, width=70)
	caixa_telefone.pack()
	caixa_telefone.place(relx=0.56, rely=0.3, anchor="center")

	cep = tk.Label(petshop, text="CEP: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	cep.pack()
	cep.place(relx=0.4, rely=0.35, anchor="center")
	caixa_cep = tk.Entry(petshop, width=75)
	caixa_cep.pack()
	caixa_cep.place(relx=0.55, rely=0.35, anchor="center")
	botao_cadastrar = tk.Button(petshop, text="ALTERAR", width='20', height='0', font="Arial 10 bold", fg="#000842", command= lambda: alterar.alterando('proprietario', int(caixa_codigo.get()) if caixa_codigo.get() else None, modifica= [int(caixa_telefone.get()) if caixa_telefone.get() else None, int(caixa_cep.get()) if caixa_cep.get() else None]))
	botao_cadastrar.pack()
	botao_cadastrar.place(relx=0.4, rely=0.4, anchor="center")

	botao_cadastrar.bind("<Enter>", lambda event: botao_cadastrar.config(bg='#000842', fg='white'))
	botao_cadastrar.bind("<Leave>", lambda event: botao_cadastrar.config(bg='white', fg='#000842',))

	botao_limpar = tk.Button(petshop, text="LIMPAR", width='20', height='0', font="Arial 10 bold", fg="#000842")
	botao_limpar.pack()
	botao_limpar.place(relx=0.5, rely=0.4, anchor="center")

	botao_limpar.bind("<Enter>", lambda event: botao_limpar.config(bg='#000842', fg='white'))
	botao_limpar.bind("<Leave>", lambda event: botao_limpar.config(bg='white', fg='#000842',))

	botao_voltar = tk.Button(petshop, text="VOLTAR AO MENU", width='20', height='0', font="Arial 10 bold", fg="#000842", command=voltar)
	botao_voltar.pack()
	botao_voltar.place(relx=0.6, rely=0.4, anchor="center")

	botao_voltar.bind("<Enter>", lambda event: botao_voltar.config(bg='#000842', fg='white'))
	botao_voltar.bind("<Leave>", lambda event: botao_voltar.config(bg='white', fg='#000842',))

def alterar_animais():
	for widget in petshop.winfo_children():
		widget.destroy()

	texto_estoque = tk.Label(petshop, text="ALTERAÇÃO DE ANIMAIS", font="Arial 30 bold", bg="lightblue", fg="#000842")
	texto_estoque.pack()
	texto_estoque.place(relx=0.5, rely=0.1, anchor="center")

	codigo = tk.Label(petshop, text="ID DE ALTERAÇÃO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	codigo.pack()
	codigo.place(relx=0.4, rely=0.2, anchor="center")
	caixa_codigo = tk.Entry(petshop, width=60)
	caixa_codigo.pack()
	caixa_codigo.place(relx=0.57, rely=0.2, anchor="center")

	peso = tk.Label(petshop, text="PESO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	peso.pack()
	peso.place(relx=0.4, rely=0.3, anchor="center")
	caixa_peso = tk.Entry(petshop, width=68)
	caixa_peso.pack()
	caixa_peso.place(relx=0.56, rely=0.3, anchor="center")

	altura = tk.Label(petshop, text="ALTURA: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	altura.pack()
	altura.place(relx=0.4, rely=0.35, anchor="center")
	caixa_altura = tk.Entry(petshop, width=60)
	caixa_altura.pack()
	caixa_altura.place(relx=0.57, rely=0.35, anchor="center")

	idade = tk.Label(petshop, text="IDADE: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	idade.pack()
	idade.place(relx=0.4, rely=0.4, anchor="center")
	caixa_idade = tk.Entry(petshop, width=60)
	caixa_idade.pack()
	caixa_idade.place(relx=0.57, rely=0.4, anchor="center")

	idproprietario = tk.Label(petshop, text="IDPROPRIETÁRIO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	idproprietario.pack()
	idproprietario.place(relx=0.4, rely=0.45, anchor="center")
	caixa_idproprietario = tk.Entry(petshop, width=60)
	caixa_idproprietario.pack()
	caixa_idproprietario.place(relx=0.57, rely=0.45, anchor="center")

	botao_cadastrar = tk.Button(petshop, text="ALTERAR", width='20', height='0', font="Arial 10 bold", fg="#000842", command= lambda: alterar.alterando('animal', int(caixa_codigo.get()) if caixa_codigo.get() else None, modifica= [float(caixa_peso.get()) if caixa_peso.get() else None, float(caixa_altura.get()) if caixa_altura.get() else None, int(caixa_idade.get()) if caixa_idade.get() else None, int(caixa_idproprietario.get()) if caixa_idproprietario.get() else None]))
	botao_cadastrar.pack()
	botao_cadastrar.place(relx=0.4, rely=0.6, anchor="center")

	botao_cadastrar.bind("<Enter>", lambda event: botao_cadastrar.config(bg='#000842', fg='white'))
	botao_cadastrar.bind("<Leave>", lambda event: botao_cadastrar.config(bg='white', fg='#000842',))

	botao_limpar = tk.Button(petshop, text="LIMPAR", width='20', height='0', font="Arial 10 bold", fg="#000842")
	botao_limpar.pack()
	botao_limpar.place(relx=0.5, rely=0.6, anchor="center")

	botao_limpar.bind("<Enter>", lambda event: botao_limpar.config(bg='#000842', fg='white'))
	botao_limpar.bind("<Leave>", lambda event: botao_limpar.config(bg='white', fg='#000842',))

	botao_voltar = tk.Button(petshop, text="VOLTAR AO MENU", width='20', height='0', font="Arial 10 bold", fg="#000842", command=voltar)
	botao_voltar.pack()
	botao_voltar.place(relx=0.6, rely=0.6, anchor="center")

	botao_voltar.bind("<Enter>", lambda event: botao_voltar.config(bg='#000842', fg='white'))
	botao_voltar.bind("<Leave>", lambda event: botao_voltar.config(bg='white', fg='#000842',))

def alterar_banho():
	for widget in petshop.winfo_children():
		widget.destroy()

	texto_estoque = tk.Label(petshop, text="ALTERAÇÃO DE BANHO E TOSAS", font="Arial 30 bold", bg="lightblue", fg="#000842")
	texto_estoque.pack()
	texto_estoque.place(relx=0.5, rely=0.1, anchor="center")

	codigo = tk.Label(petshop, text="ID DE ALTERAÇÃO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	codigo.pack()
	codigo.place(relx=0.4, rely=0.2, anchor="center")
	caixa_codigo = tk.Entry(petshop, width=60)
	caixa_codigo.pack()
	caixa_codigo.place(relx=0.57, rely=0.2, anchor="center")

	data = tk.Label(petshop, text="DATA: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	data.pack()
	data.place(relx=0.4, rely=0.25, anchor="center")
	caixa_data = tk.Entry(petshop, width=73)
	caixa_data.pack()
	caixa_data.place(relx=0.55, rely=0.25, anchor="center")

	horario = tk.Label(petshop, text="HORÁRIO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	horario.pack()
	horario.place(relx=0.4, rely=0.3, anchor="center")
	caixa_horario = tk.Entry(petshop, width=75)
	caixa_horario.pack()
	caixa_horario.place(relx=0.55, rely=0.3, anchor="center")

	tipo = tk.Label(petshop, text="TIPO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	tipo.pack()
	tipo.place(relx=0.4, rely=0.35, anchor="center")
	caixa_tipo = tk.Entry(petshop, width=75)
	caixa_tipo.pack()
	caixa_tipo.place(relx=0.55, rely=0.35, anchor="center")

	valor = tk.Label(petshop, text="VALOR: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	valor.pack()
	valor.place(relx=0.4, rely=0.4, anchor="center")
	caixa_valor = tk.Entry(petshop, width=75)
	caixa_valor.pack()
	caixa_valor.place(relx=0.55, rely=0.4, anchor="center")

	idanimal = tk.Label(petshop, text="IDANIMAL: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	idanimal.pack()
	idanimal.place(relx=0.4, rely=0.45, anchor="center")
	caixa_idanimal = tk.Entry(petshop, width=68)
	caixa_idanimal.pack()
	caixa_idanimal.place(relx=0.56, rely=0.45, anchor="center")

	idfuncionario = tk.Label(petshop, text="IDFUNCIONÁRIO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	idfuncionario.pack()
	idfuncionario.place(relx=0.4, rely=0.5, anchor="center")
	caixa_idfuncionario = tk.Entry(petshop, width=60)
	caixa_idfuncionario.pack()
	caixa_idfuncionario.place(relx=0.57, rely=0.5, anchor="center")

	botao_cadastrar = tk.Button(petshop, text="ALTERAR", width='20', height='0', font="Arial 10 bold", fg="#000842", command= lambda: alterar.alterando('banho', int(caixa_codigo.get()) if caixa_codigo.get() else None, modifica= [caixa_data.get() if caixa_data.get() else None, caixa_horario.get() if caixa_horario.get() else None, caixa_tipo.get() if caixa_tipo.get() else None, float(caixa_valor.get()) if caixa_valor.get() else None, int(caixa_idanimal.get()) if caixa_idanimal.get() else None, int(caixa_idfuncionario.get()) if caixa_idfuncionario.get() else None]))
	botao_cadastrar.pack()
	botao_cadastrar.place(relx=0.4, rely=0.6, anchor="center")

	botao_cadastrar.bind("<Enter>", lambda event: botao_cadastrar.config(bg='#000842', fg='white'))
	botao_cadastrar.bind("<Leave>", lambda event: botao_cadastrar.config(bg='white', fg='#000842',))

	botao_limpar = tk.Button(petshop, text="LIMPAR", width='20', height='0', font="Arial 10 bold", fg="#000842")
	botao_limpar.pack()
	botao_limpar.place(relx=0.5, rely=0.6, anchor="center")

	botao_limpar.bind("<Enter>", lambda event: botao_limpar.config(bg='#000842', fg='white'))
	botao_limpar.bind("<Leave>", lambda event: botao_limpar.config(bg='white', fg='#000842',))

	botao_voltar = tk.Button(petshop, text="VOLTAR AO MENU", width='20', height='0', font="Arial 10 bold", fg="#000842", command=voltar)
	botao_voltar.pack()
	botao_voltar.place(relx=0.6, rely=0.6, anchor="center")

	botao_voltar.bind("<Enter>", lambda event: botao_voltar.config(bg='#000842', fg='white'))
	botao_voltar.bind("<Leave>", lambda event: botao_voltar.config(bg='white', fg='#000842',))

###############DEF'S PESQUISAR

def pesquisar_funcionario():
	for widget in petshop.winfo_children():
		widget.destroy()

	texto = tk.Label(petshop, text="O QUE VOCÊ DESEJA PESQUISAR DOS FUNCIONÁRIOS?", font="Arial 45 bold", bg="lightblue", fg="#000842")
	texto.place(relx=0.5, rely=0.2, anchor="center")
	
	caixa_pesquisa = tk.Entry(petshop, width=120)
	caixa_pesquisa.pack()
	caixa_pesquisa.place(relx=0.45, rely=0.3, anchor="center")

	botao_pesquisar = tk.Button(petshop, text="PESQUISAR", width='20', height='0', font="Arial 10 bold", fg="#000842", command= lambda: pesquisar.pesquisar('funcionario', petshop, checkboxes= [codigo.get() if codigo.get() else None, nome.get() if nome.get() else None, telefone.get() if telefone.get() else None, cargo.get() if cargo.get() else None, salario.get() if salario.get() else None, cep.get() if cep.get() else None, todos.get() if todos.get() else None], termo = caixa_pesquisa.get() if caixa_pesquisa.get() else None))
	botao_pesquisar.pack()
	botao_pesquisar.place(relx=0.7, rely=0.3, anchor="center")

	botao_pesquisar.bind("<Enter>", lambda event: botao_pesquisar.config(bg='#000842', fg='white'))
	botao_pesquisar.bind("<Leave>", lambda event: botao_pesquisar.config(bg='white', fg='#000842',))

	codigo = BooleanVar()
	check_codigo = tk.Checkbutton(petshop, text="código", variable = codigo)
	check_codigo.pack()
	check_codigo.place(relx=0.35, rely=0.4, anchor="center", width=100)

	nome = BooleanVar()
	check_nome = tk.Checkbutton(petshop, text="nome", variable = nome)
	check_nome.pack()
	check_nome.place(relx=0.4, rely=0.4, anchor="center", width=100)

	telefone = BooleanVar()
	check_telefone = tk.Checkbutton(petshop, text="telefone", variable = telefone)
	check_telefone.pack()
	check_telefone.place(relx=0.45, rely=0.4, anchor="center", width=100)

	cargo = BooleanVar()
	check_cargo = tk.Checkbutton(petshop, text="Cargo", variable = cargo)
	check_cargo.pack()
	check_cargo.place(relx=0.5, rely=0.4, anchor="center", width=100)

	salario = BooleanVar()
	check_salario = tk.Checkbutton(petshop, text="salário", variable = salario)
	check_salario.pack()
	check_salario.place(relx=0.55, rely=0.4, anchor="center", width=100)

	cep = BooleanVar()
	check_cep = tk.Checkbutton(petshop, text="cep", variable = cep)
	check_cep.pack()
	check_cep.place(relx=0.6, rely=0.4, anchor="center", width=100)

	todos = BooleanVar()
	check_todos = tk.Checkbutton(petshop, text="todos", variable = todos)
	check_todos.pack()
	check_todos.place(relx=0.65, rely=0.4, anchor="center", width=100)

	botao_voltar = tk.Button(petshop, text="VOLTAR AO MENU", width='20', height='0', font="Arial 10 bold", fg="#000842", command=voltar)
	botao_voltar.pack()
	botao_voltar.place(relx=0.5, rely=0.95, anchor="center")

	botao_voltar.bind("<Enter>", lambda event: botao_voltar.config(bg='#000842', fg='white'))
	botao_voltar.bind("<Leave>", lambda event: botao_voltar.config(bg='white', fg='#000842',))

def pesquisar_clientes():
	for widget in petshop.winfo_children():
		widget.destroy()

	texto = tk.Label(petshop, text="O QUE VOCÊ DESEJA PESQUISAR DOS PROPRIETÁRIOS?", font="Arial 45 bold", bg="lightblue", fg="#000842")
	texto.place(relx=0.5, rely=0.2, anchor="center")
	
	caixa_pesquisa = tk.Entry(petshop, width=120)
	caixa_pesquisa.pack()
	caixa_pesquisa.place(relx=0.45, rely=0.3, anchor="center")

	botao_pesquisar = tk.Button(petshop, text="PESQUISAR", width='20', height='0', font="Arial 10 bold", fg="#000842", command= lambda: pesquisar.pesquisar('proprietario', petshop, checkboxes= [codigo.get() if codigo.get() else None, nome.get() if nome.get() else None, telefone.get() if telefone.get() else None, todos.get() if todos.get() else None], termo = caixa_pesquisa.get() if caixa_pesquisa.get() else None))
	botao_pesquisar.pack()
	botao_pesquisar.place(relx=0.7, rely=0.3, anchor="center")

	botao_pesquisar.bind("<Enter>", lambda event: botao_pesquisar.config(bg='#000842', fg='white'))
	botao_pesquisar.bind("<Leave>", lambda event: botao_pesquisar.config(bg='white', fg='#000842',))

	codigo = BooleanVar()
	check_codigo = tk.Checkbutton(petshop, text="código", variable = codigo, onvalue=1, offvalue=0)
	check_codigo.pack()
	check_codigo.place(relx=0.4, rely=0.4, anchor="center", width=100)

	nome = BooleanVar()
	check_nome = tk.Checkbutton(petshop, text="nome", variable = nome, onvalue=1, offvalue=0)
	check_nome.pack()
	check_nome.place(relx=0.45, rely=0.4, anchor="center", width=100)

	telefone = BooleanVar()
	check_telefone = tk.Checkbutton(petshop, text="telefone", variable = telefone, onvalue=1, offvalue=0)
	check_telefone.pack()
	check_telefone.place(relx=0.5, rely=0.4, anchor="center", width=100)

	cep = BooleanVar()
	check_cep = tk.Checkbutton(petshop, text="cep", variable = cep, onvalue=1, offvalue=0)
	check_cep.pack()
	check_cep.place(relx=0.55, rely=0.4, anchor="center", width=100)

	todos = BooleanVar()
	check_todos = tk.Checkbutton(petshop, text="todos", variable = todos, onvalue=1, offvalue=0)
	check_todos.pack()
	check_todos.place(relx=0.6, rely=0.4, anchor="center", width=100)

	botao_voltar = tk.Button(petshop, text="VOLTAR AO MENU", width='20', height='0', font="Arial 10 bold", fg="#000842", command=voltar)
	botao_voltar.pack()
	botao_voltar.place(relx=0.5, rely=0.95, anchor="center")

	botao_voltar.bind("<Enter>", lambda event: botao_voltar.config(bg='#000842', fg='white'))
	botao_voltar.bind("<Leave>", lambda event: botao_voltar.config(bg='white', fg='#000842',))

def pesquisar_animal():
	for widget in petshop.winfo_children():
		widget.destroy()

	texto = tk.Label(petshop, text="O QUE VOCÊ DESEJA PESQUISAR DOS ANIMAIS?", font="Arial 45 bold", bg="lightblue", fg="#000842")
	texto.place(relx=0.5, rely=0.2, anchor="center")
	
	caixa_pesquisa = tk.Entry(petshop, width=120)
	caixa_pesquisa.pack()
	caixa_pesquisa.place(relx=0.45, rely=0.3, anchor="center")

	botao_pesquisar = tk.Button(petshop, text="PESQUISAR", width='20', height='0', font="Arial 10 bold", fg="#000842", command= lambda: pesquisar.pesquisar('funcionario', petshop, checkboxes= [codigo.get() if codigo.get() else None, nome.get() if nome.get() else None, especie.get() if especie.get() else None, raca.get() if raca.get() else None, peso.get() if peso.get() else None, altura.get() if altura.get() else None, idade.get() if idade.get() else None, cor.get() if cor.get() else None, codproprietario.get() if codproprietario.get() else None, todos.get() if todos.get() else None], termo = caixa_pesquisa.get() if caixa_pesquisa.get() else None))
	botao_pesquisar.pack()
	botao_pesquisar.place(relx=0.7, rely=0.3, anchor="center")

	botao_pesquisar.bind("<Enter>", lambda event: botao_pesquisar.config(bg='#000842', fg='white'))
	botao_pesquisar.bind("<Leave>", lambda event: botao_pesquisar.config(bg='white', fg='#000842',))

	codigo = BooleanVar()
	check_codigo = tk.Checkbutton(petshop, text="código", variable = codigo, onvalue=1, offvalue=0)
	check_codigo.pack()
	check_codigo.place(relx=0.25, rely=0.4, anchor="center", width=100)

	nome = BooleanVar()
	check_nome = tk.Checkbutton(petshop, text="nome", variable = nome, onvalue=1, offvalue=0)
	check_nome.pack()
	check_nome.place(relx=0.3, rely=0.4, anchor="center", width=100)

	especie = BooleanVar()
	check_especie = tk.Checkbutton(petshop, text="espécie", variable = especie, onvalue=1, offvalue=0)
	check_especie.pack()
	check_especie.place(relx=0.35, rely=0.4, anchor="center", width=100)

	raca = BooleanVar()
	check_raca = tk.Checkbutton(petshop, text="raça", variable = raca, onvalue=1, offvalue=0)
	check_raca.pack()
	check_raca.place(relx=0.4, rely=0.4, anchor="center", width=100)
	
	peso = BooleanVar()
	check_peso = tk.Checkbutton(petshop, text="peso", variable = peso, onvalue=1, offvalue=0)
	check_peso.pack()
	check_peso.place(relx=0.45, rely=0.4, anchor="center", width=100)
	
	altura = BooleanVar()
	check_altura = tk.Checkbutton(petshop, text="altura", variable = altura, onvalue=1, offvalue=0)
	check_altura.pack()
	check_altura.place(relx=0.5, rely=0.4, anchor="center", width=100)

	idade = BooleanVar()
	check_idade = tk.Checkbutton(petshop, text="idade", variable = idade, onvalue=1, offvalue=0)
	check_idade.pack()
	check_idade.place(relx=0.55, rely=0.4, anchor="center", width=100)

	cor = BooleanVar()
	check_cor = tk.Checkbutton(petshop, text="cor", variable = cor, onvalue=1, offvalue=0)
	check_cor.pack()
	check_cor.place(relx=0.6, rely=0.4, anchor="center", width=100)

	codproprietario = BooleanVar()
	check_codproprietario = tk.Checkbutton(petshop, text="codproprietario", variable = codproprietario, onvalue=1, offvalue=0)
	check_codproprietario.pack()
	check_codproprietario.place(relx=0.65, rely=0.4, anchor="center", width=100)

	todos = BooleanVar()
	check_todos = tk.Checkbutton(petshop, text="todos", variable = todos, onvalue=1, offvalue=0)
	check_todos.pack()
	check_todos.place(relx=0.7, rely=0.4, anchor="center", width=95)

	botao_voltar = tk.Button(petshop, text="VOLTAR AO MENU", width='20', height='0', font="Arial 10 bold", fg="#000842", command=voltar)
	botao_voltar.pack()
	botao_voltar.place(relx=0.5, rely=0.95, anchor="center")

	botao_voltar.bind("<Enter>", lambda event: botao_voltar.config(bg='#000842', fg='white'))
	botao_voltar.bind("<Leave>", lambda event: botao_voltar.config(bg='white', fg='#000842',))

def pesquisar_banho():
	for widget in petshop.winfo_children():
		widget.destroy()

	texto = tk.Label(petshop, text="O QUE VOCÊ DESEJA PESQUISAR DO BANHO E TOSA?", font="Arial 45 bold", bg="lightblue", fg="#000842")
	texto.place(relx=0.5, rely=0.2, anchor="center")
	
	caixa_pesquisa = tk.Entry(petshop, width=120)
	caixa_pesquisa.pack()
	caixa_pesquisa.place(relx=0.45, rely=0.3, anchor="center")

	botao_pesquisar = tk.Button(petshop, text="PESQUISAR", width='20', height='0', font="Arial 10 bold", fg="#000842", command= lambda: pesquisar.pesquisar('funcionario', petshop, checkboxes= [codigo.get() if codigo.get() else None, data.get() if data.get() else None, data.get() if data.get() else None, tipo.get() if tipo.get() else None, valor.get() if valor.get() else None, idanimal.get() if idanimal.get() else None, idfuncionario.get() if idfuncionario.get() else None, todos.get() if todos.get() else None], termo = caixa_pesquisa.get() if caixa_pesquisa.get() else None))
	botao_pesquisar.pack()
	botao_pesquisar.place(relx=0.7, rely=0.3, anchor="center")

	botao_pesquisar.bind("<Enter>", lambda event: botao_pesquisar.config(bg='#000842', fg='white'))
	botao_pesquisar.bind("<Leave>", lambda event: botao_pesquisar.config(bg='white', fg='#000842',))

	codigo = BooleanVar()
	check_codigo = tk.Checkbutton(petshop, text="código", variable = codigo, onvalue=1, offvalue=0)
	check_codigo.pack()
	check_codigo.place(relx=0.3, rely=0.4, anchor="center", width=100)

	horario = BooleanVar()
	check_horario = tk.Checkbutton(petshop, text="horário", variable = horario, onvalue=1, offvalue=0)
	check_horario.pack()
	check_horario.place(relx=0.35, rely=0.4, anchor="center", width=100)

	data = BooleanVar()
	check_data = tk.Checkbutton(petshop, text="espécie", variable = data, onvalue=1, offvalue=0)
	check_data.pack()
	check_data.place(relx=0.4, rely=0.4, anchor="center", width=100)

	tipo = BooleanVar()
	check_tipo = tk.Checkbutton(petshop, text="raça", variable = tipo, onvalue=1, offvalue=0)
	check_tipo.pack()
	check_tipo.place(relx=0.45, rely=0.4, anchor="center", width=100)
	
	valor = BooleanVar()
	check_valor = tk.Checkbutton(petshop, text="valor", variable = valor, onvalue=1, offvalue=0)
	check_valor.pack()
	check_valor.place(relx=0.55, rely=0.4, anchor="center", width=100)
	
	idanimal = BooleanVar()
	check_idanimal = tk.Checkbutton(petshop, text="idanimal", variable = idanimal, onvalue=1, offvalue=0)
	check_idanimal.pack()
	check_idanimal.place(relx=0.6, rely=0.4, anchor="center", width=100)

	idfuncionario = BooleanVar()
	check_idfuncionario = tk.Checkbutton(petshop, text="idfuncionario", variable = idfuncionario, onvalue=1, offvalue=0)
	check_idfuncionario.pack()
	check_idfuncionario.place(relx=0.65, rely=0.4, anchor="center", width=100)

	todos = BooleanVar()
	check_todos = tk.Checkbutton(petshop, text="todos", variable = todos, onvalue=1, offvalue=0)
	check_todos.pack()
	check_todos.place(relx=0.7, rely=0.4, anchor="center", width=95)

	botao_voltar = tk.Button(petshop, text="VOLTAR AO MENU", width='20', height='0', font="Arial 10 bold", fg="#000842", command=voltar)
	botao_voltar.pack()
	botao_voltar.place(relx=0.5, rely=0.95, anchor="center")

	botao_voltar.bind("<Enter>", lambda event: botao_voltar.config(bg='#000842', fg='white'))
	botao_voltar.bind("<Leave>", lambda event: botao_voltar.config(bg='white', fg='#000842',))

###############DEF'S EXCLUIR 

def excluir_funcionario():
	for widget in petshop.winfo_children():
		widget.destroy()

	texto = tk.Label(petshop, text="O QUE VOCÊ DESEJA EXCLUIR DO FUNCIONÁRIO?", font="Arial 45 bold", bg="lightblue", fg="#000842")
	texto.place(relx=0.5, rely=0.2, anchor="center")
	
	caixa_pesquisa = tk.Entry(petshop, width=120)
	caixa_pesquisa.pack()
	caixa_pesquisa.place(relx=0.45, rely=0.3, anchor="center")

	botao_excluir = tk.Button(petshop, text="EXCLUIR", width='20', height='0', font="Arial 10 bold", fg="#000842", command= lambda: deletar.deletar('funcionario', int(caixa_pesquisa.get()) if caixa_pesquisa.get() else None))
	botao_excluir.pack()
	botao_excluir.place(relx=0.7, rely=0.3, anchor="center")

	botao_excluir.bind("<Enter>", lambda event: botao_excluir.config(bg='#000842', fg='white'))
	botao_excluir.bind("<Leave>", lambda event: botao_excluir.config(bg='white', fg='#000842',))

	botao_voltar = tk.Button(petshop, text="VOLTAR AO MENU", width='20', height='0', font="Arial 10 bold", fg="#000842", command=voltar)
	botao_voltar.pack()
	botao_voltar.place(relx=0.5, rely=0.95, anchor="center")

	botao_voltar.bind("<Enter>", lambda event: botao_voltar.config(bg='#000842', fg='white'))
	botao_voltar.bind("<Leave>", lambda event: botao_voltar.config(bg='white', fg='#000842',))

def excluir_clientes():
	for widget in petshop.winfo_children():
		widget.destroy()

	texto = tk.Label(petshop, text="O QUE VOCÊ DESEJA EXCLUIR DO PROPRIETÁRIO?", font="Arial 45 bold", bg="lightblue", fg="#000842")
	texto.place(relx=0.5, rely=0.2, anchor="center")
	
	caixa_pesquisa = tk.Entry(petshop, width=120)
	caixa_pesquisa.pack()
	caixa_pesquisa.place(relx=0.45, rely=0.3, anchor="center")

	botao_excluir = tk.Button(petshop, text="EXCLUIR", width='20', height='0', font="Arial 10 bold", fg="#000842", command= lambda: deletar.deletar('proprietario', int(caixa_pesquisa.get()) if caixa_pesquisa.get() else None))
	botao_excluir.pack()
	botao_excluir.place(relx=0.7, rely=0.3, anchor="center")

	botao_excluir.bind("<Enter>", lambda event: botao_excluir.config(bg='#000842', fg='white'))
	botao_excluir.bind("<Leave>", lambda event: botao_excluir.config(bg='white', fg='#000842',))

	botao_voltar = tk.Button(petshop, text="VOLTAR AO MENU", width='20', height='0', font="Arial 10 bold", fg="#000842", command=voltar)
	botao_voltar.pack()
	botao_voltar.place(relx=0.5, rely=0.95, anchor="center")

	botao_voltar.bind("<Enter>", lambda event: botao_voltar.config(bg='#000842', fg='white'))
	botao_voltar.bind("<Leave>", lambda event: botao_voltar.config(bg='white', fg='#000842',))

def excluir_animais():
	for widget in petshop.winfo_children():
		widget.destroy()

	texto = tk.Label(petshop, text="O QUE VOCÊ DESEJA EXCLUIR DOS ANIMAIS?", font="Arial 45 bold", bg="lightblue", fg="#000842")
	texto.place(relx=0.5, rely=0.2, anchor="center")
	
	caixa_pesquisa = tk.Entry(petshop, width=120)
	caixa_pesquisa.pack()
	caixa_pesquisa.place(relx=0.45, rely=0.3, anchor="center")
	
	botao_excluir = tk.Button(petshop, text="EXCLUIR", width='20', height='0', font="Arial 10 bold", fg="#000842", command= lambda: deletar.deletar('animal', int(caixa_pesquisa.get()) if caixa_pesquisa.get() else None))
	botao_excluir.pack()
	botao_excluir.place(relx=0.7, rely=0.3, anchor="center")

	botao_excluir.bind("<Enter>", lambda event: botao_excluir.config(bg='#000842', fg='white'))
	botao_excluir.bind("<Leave>", lambda event: botao_excluir.config(bg='white', fg='#000842'))


	botao_voltar = tk.Button(petshop, text="VOLTAR AO MENU", width='20', height='0', font="Arial 10 bold", fg="#000842", command=voltar)
	botao_voltar.pack()
	botao_voltar.place(relx=0.5, rely=0.95, anchor="center")

	botao_voltar.bind("<Enter>", lambda event: botao_voltar.config(bg='#000842', fg='white'))
	botao_voltar.bind("<Leave>", lambda event: botao_voltar.config(bg='white', fg='#000842'))

def excluir_banho():
	for widget in petshop.winfo_children():
		widget.destroy()

	texto = tk.Label(petshop, text="O QUE VOCÊ DESEJA EXCLUIR DO BANHO E TOSA?", font="Arial 45 bold", bg="lightblue", fg="#000842")
	texto.place(relx=0.5, rely=0.2, anchor="center")
	
	caixa_pesquisa = tk.Entry(petshop, width=120)
	caixa_pesquisa.pack()
	caixa_pesquisa.place(relx=0.45, rely=0.3, anchor="center")

	botao_excluir = tk.Button(petshop, text="EXCLUIR", width='20', height='0', font="Arial 10 bold", fg="#000842", command= lambda: deletar.deletar('banho', int(caixa_pesquisa.get()) if caixa_pesquisa.get() else None))
	botao_excluir.pack()
	botao_excluir.place(relx=0.7, rely=0.3, anchor="center")

	botao_excluir.bind("<Enter>", lambda event: botao_excluir.config(bg='#000842', fg='white'))
	botao_excluir.bind("<Leave>", lambda event: botao_excluir.config(bg='white', fg='#000842',))

	botao_voltar = tk.Button(petshop, text="VOLTAR AO MENU", width='20', height='0', font="Arial 10 bold", fg="#000842", command=voltar)
	botao_voltar.pack()
	botao_voltar.place(relx=0.5, rely=0.95, anchor="center")

	botao_voltar.bind("<Enter>", lambda event: botao_voltar.config(bg='#000842', fg='white'))
	botao_voltar.bind("<Leave>", lambda event: botao_voltar.config(bg='white', fg='#000842',))

petshop = tk.Tk()
petshop.configure(bg="lightblue")
petshop.state('zoomed')
petshop.title("Clínica Veterinária Petshop")
voltar()

petshop.mainloop()