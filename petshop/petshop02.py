import tkinter as tk
from tkinter import *
from tkinter import Label

########### MENU PRINCIPAL
def voltar():
	for widget in petshop.winfo_children():
		widget.destroy()
		
########################## ESTOQUE
	label_nome = tk.Label(petshop, text= "BEM-VINDOS A PATAS & CIA", font="Arial 65 bold", bg="lightblue", fg="#000842")
	label_nome.pack()
	label_nome.place(relx=0.5, rely=0.2, anchor="center")

	texto = tk.Label(petshop, text="O QUE VOCÊ DESEJA FAZER?", font="Arial 45", bg="lightblue", fg="#000842")
	texto.place(relx=0.5, rely=0.3, anchor="center")
	
    
	texto_1 = tk.Label(petshop, text="CONFIGURAR ESTOQUE:", font="Arial 20 bold", bg="lightblue", fg="#000842")
	texto_1.place(relx=0.25, rely=0.45, anchor="center")
	
	botao_cadastro = tk.Button(petshop, text="CADASTRAR", fg="#000842", width='15', height='3', font="Arial 15 bold", command=cadastrar_estoque)
	botao_cadastro.place(relx=0.1, rely=0.55, anchor="center")

	botao_atendimento = tk.Button(petshop, text="EXCLUIR", fg="#000842", width='15', height='3', font="Arial 15 bold")
	botao_atendimento.place(relx=0.2, rely=0.55, anchor="center")

	botao_estoque= tk.Button(petshop, text="ALTERAR", fg="#000842", width='15', height='3', font="Arial 15 bold", command=alterar_estoque)
	botao_estoque.place(relx=0.3, rely=0.55, anchor="center")

	botao_financas= tk.Button(petshop, text="PESQUISAR", fg="#000842", width='15', height='3', font="Arial 15 bold", command=pesquisar_estoque)
	botao_financas.place(relx=0.4, rely=0.55, anchor="center")

	botao_cadastro.bind("<Enter>", lambda event: botao_cadastro.config(bg='#000842', fg='white'))
	botao_cadastro.bind("<Leave>", lambda event: botao_cadastro.config(bg='white', fg='#000842',))

	botao_atendimento.bind("<Enter>", lambda event: botao_atendimento.config(bg='#000842', fg='white'))
	botao_atendimento.bind("<Leave>", lambda event: botao_atendimento.config(bg='white', fg='#000842',))

	botao_estoque.bind("<Enter>", lambda event: botao_estoque.config(bg='#000842', fg='white'))
	botao_estoque.bind("<Leave>", lambda event: botao_estoque.config(bg='white', fg='#000842',))

	botao_financas.bind("<Enter>", lambda event: botao_financas.config(bg='#000842', fg='white'))
	botao_financas.bind("<Leave>", lambda event: botao_financas.config(bg='white', fg='#000842',))
	
########################## VENDAS
	texto_1 = tk.Label(petshop, text="CONFIGURAR VENDAS:", font="Arial 20 bold", bg="lightblue", fg="#000842")
	texto_1.place(relx=0.75, rely=0.45, anchor="center")
	
	botao_cadastro1 = tk.Button(petshop, text="CADASTRAR", fg="#000842", width='15', height='3', font="Arial 15 bold", command=cadastrar_venda)
	botao_cadastro1.place(relx=0.6, rely=0.55, anchor="center")

	botao_atendimento1 = tk.Button(petshop, text="EXCLUIR", fg="#000842", width='15', height='3', font="Arial 15 bold")
	botao_atendimento1.place(relx=0.7, rely=0.55, anchor="center")

	botao_estoque1= tk.Button(petshop, text="ALTERAR", fg="#000842", width='15', height='3', font="Arial 15 bold", command=alterar_venda)
	botao_estoque1.place(relx=0.8, rely=0.55, anchor="center")

	botao_financas1= tk.Button(petshop, text="PESQUISAR", fg="#000842", width='15', height='3', font="Arial 15 bold", command=pesquisar_venda)
	botao_financas1.place(relx=0.9, rely=0.55, anchor="center")

	botao_cadastro1.bind("<Enter>", lambda event: botao_cadastro1.config(bg='#000842', fg='white'))
	botao_cadastro1.bind("<Leave>", lambda event: botao_cadastro1.config(bg='white', fg='#000842',))

	botao_atendimento1.bind("<Enter>", lambda event: botao_atendimento1.config(bg='#000842', fg='white'))
	botao_atendimento1.bind("<Leave>", lambda event: botao_atendimento1.config(bg='white', fg='#000842',))

	botao_estoque1.bind("<Enter>", lambda event: botao_estoque1.config(bg='#000842', fg='white'))
	botao_estoque1.bind("<Leave>", lambda event: botao_estoque1.config(bg='white', fg='#000842',))

	botao_financas1.bind("<Enter>", lambda event: botao_financas1.config(bg='#000842', fg='white'))
	botao_financas1.bind("<Leave>", lambda event: botao_financas1.config(bg='white', fg='#000842',))


#################### ANIMAIS
	texto_3 = tk.Label(petshop, text="CONFIGURAR ANIMAIS:", font="Arial 20 bold", bg="lightblue", fg="#000832")
	texto_3.place(relx=0.75, rely=0.75, anchor="center")
	
	botao_cadastro3 = tk.Button(petshop, text="CADASTRAR", fg="#000832", width='15', height='3', font="Arial 15 bold", command=cadastrar_animais)
	botao_cadastro3.place(relx=0.6, rely=0.85, anchor="center")

	botao_atendimento3 = tk.Button(petshop, text="EXCLUIR", fg="#000832", width='15', height='3', font="Arial 15 bold")
	botao_atendimento3.place(relx=0.7, rely=0.85, anchor="center")

	botao_estoque3= tk.Button(petshop, text="ALTERAR", fg="#000832", width='15', height='3', font="Arial 15 bold", command=alterar_animais)
	botao_estoque3.place(relx=0.8, rely=0.85, anchor="center")

	botao_financas3= tk.Button(petshop, text="PESQUISAR", fg="#000832", width='15', height='3', font="Arial 15 bold", command=pesquisar_animal)
	botao_financas3.place(relx=0.9, rely=0.85, anchor="center")

	botao_cadastro3.bind("<Enter>", lambda event: botao_cadastro3.config(bg='#000832', fg='white'))
	botao_cadastro3.bind("<Leave>", lambda event: botao_cadastro3.config(bg='white', fg='#000832',))

	botao_atendimento3.bind("<Enter>", lambda event: botao_atendimento3.config(bg='#000832', fg='white'))
	botao_atendimento3.bind("<Leave>", lambda event: botao_atendimento3.config(bg='white', fg='#000832',))

	botao_estoque3.bind("<Enter>", lambda event: botao_estoque3.config(bg='#000832', fg='white'))
	botao_estoque3.bind("<Leave>", lambda event: botao_estoque3.config(bg='white', fg='#000832',))

	botao_financas3.bind("<Enter>", lambda event: botao_financas3.config(bg='#000832', fg='white'))
	botao_financas3.bind("<Leave>", lambda event: botao_financas3.config(bg='white', fg='#000842',))


##############################BANHO E TOSA
	texto_4 = tk.Label(petshop, text="CONFIGURAR BANHO E TOSA:", font="Arial 20 bold", bg="lightblue", fg="#000842")
	texto_4.place(relx=0.25, rely=0.75, anchor="center")
	
	botao_cadastro4 = tk.Button(petshop, text="CADASTRAR", fg="#000842", width='15', height='4', font="Arial 15 bold", command=cadastrar_banho)
	botao_cadastro4.place(relx=0.1, rely=0.85, anchor="center")

	botao_atendimento4 = tk.Button(petshop, text="EXCLUIR", fg="#000842", width='15', height='4', font="Arial 15 bold")
	botao_atendimento4.place(relx=0.2, rely=0.85, anchor="center")

	botao_estoque4= tk.Button(petshop, text="ALTERAR", fg="#000842", width='15', height='4', font="Arial 15 bold", command=alterar_banho)
	botao_estoque4.place(relx=0.3, rely=0.85, anchor="center")

	botao_financas4= tk.Button(petshop, text="PESQUISAR", fg="#000842", width='15', height='4', font="Arial 15 bold", command=pesquisar_banho)
	botao_financas4.place(relx=0.4, rely=0.85, anchor="center")

	botao_cadastro4.bind("<Enter>", lambda event: botao_cadastro4.config(bg='#000842', fg='white'))
	botao_cadastro4.bind("<Leave>", lambda event: botao_cadastro4.config(bg='white', fg='#000842',))

	botao_atendimento4.bind("<Enter>", lambda event: botao_atendimento4.config(bg='#000842', fg='white'))
	botao_atendimento4.bind("<Leave>", lambda event: botao_atendimento4.config(bg='white', fg='#000842',))

	botao_estoque4.bind("<Enter>", lambda event: botao_estoque4.config(bg='#000842', fg='white'))
	botao_estoque4.bind("<Leave>", lambda event: botao_estoque4.config(bg='white', fg='#000842',))

	botao_financas4.bind("<Enter>", lambda event: botao_financas4.config(bg='#000842', fg='white'))
	botao_financas4.bind("<Leave>", lambda event: botao_financas4.config(bg='white', fg='#000842',))

##############DEF'S CADASTRAR
		
def cadastrar_estoque():
	for widget in petshop.winfo_children():
		widget.destroy()

	texto_estoque = tk.Label(petshop, text="CONFIGURAÇÕES DE ESTOQUE", font="Arial 30 bold", bg="lightblue", fg="#000842")
	texto_estoque.pack()
	texto_estoque.place(relx=0.5, rely=0.1, anchor="center")

	codigo = tk.Label(petshop, text="CÓDIGO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	codigo.pack()
	codigo.place(relx=0.4, rely=0.2, anchor="center")
	caixa_codigo = tk.Entry(petshop, width=75)
	caixa_codigo.pack()
	caixa_codigo.place(relx=0.55, rely=0.2, anchor="center")

	tipo = tk.Label(petshop, text="TIPO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	tipo.pack()
	tipo.place(relx=0.4, rely=0.25, anchor="center")
	caixa_tipo = tk.Entry(petshop, width=75)
	caixa_tipo.pack()
	caixa_tipo.place(relx=0.55, rely=0.25, anchor="center")

	nome = tk.Label(petshop, text="NOME: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	nome.pack()
	nome.place(relx=0.4, rely=0.3, anchor="center")
	caixa_nome = tk.Entry(petshop, width=75)
	caixa_nome.pack()
	caixa_nome.place(relx=0.55, rely=0.3, anchor="center")

	quantidade = tk.Label(petshop, text="QUANTIDADE: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	quantidade.pack()
	quantidade.place(relx=0.4, rely=0.35, anchor="center")
	caixa_quantidade = tk.Entry(petshop, width=68)
	caixa_quantidade.pack()
	caixa_quantidade.place(relx=0.56, rely=0.35, anchor="center")

	valor_venda = tk.Label(petshop, text="VALOR DA VENDA: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	valor_venda.pack()
	valor_venda.place(relx=0.4, rely=0.4, anchor="center")
	caixa_valor_venda = tk.Entry(petshop, width=60)
	caixa_valor_venda.pack()
	caixa_valor_venda.place(relx=0.57, rely=0.4, anchor="center")

	valor_compra = tk.Label(petshop, text="VALOR DA COMPRA: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	valor_compra.pack()
	valor_compra.place(relx=0.4, rely=0.45, anchor="center")
	caixa_valor_compra = tk.Entry(petshop, width=60)
	caixa_valor_compra.pack()
	caixa_valor_compra.place(relx=0.57, rely=0.45, anchor="center")

	disponibilidade = tk.Label(petshop, text="DISPONIBILIDADE: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	disponibilidade.pack()
	disponibilidade.place(relx=0.4, rely=0.5, anchor="center")
	caixa_disponibilidade = tk.Entry(petshop, width=60)
	caixa_disponibilidade.pack()
	caixa_disponibilidade.place(relx=0.57, rely=0.5, anchor="center")

	botao_cadastrar = tk.Button(petshop, text="CADASTRAR", width='20', height='0', font="Arial 10 bold", fg="#000842")
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

def cadastrar_venda():
	for widget in petshop.winfo_children():
		widget.destroy()

	texto_estoque = tk.Label(petshop, text="CONFIGURAÇÕES DE VENDAS", font="Arial 30 bold", bg="lightblue", fg="#000842")
	texto_estoque.pack()
	texto_estoque.place(relx=0.5, rely=0.1, anchor="center")

	codigo = tk.Label(petshop, text="CÓDIGO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	codigo.pack()
	codigo.place(relx=0.4, rely=0.2, anchor="center")
	caixa_codigo = tk.Entry(petshop, width=75)
	caixa_codigo.pack()
	caixa_codigo.place(relx=0.55, rely=0.2, anchor="center")

	tipo = tk.Label(petshop, text="TIPO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	tipo.pack()
	tipo.place(relx=0.4, rely=0.25, anchor="center")
	caixa_tipo = tk.Entry(petshop, width=75)
	caixa_tipo.pack()
	caixa_tipo.place(relx=0.55, rely=0.25, anchor="center")

	nome = tk.Label(petshop, text="NOME: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	nome.pack()
	nome.place(relx=0.4, rely=0.3, anchor="center")
	caixa_nome = tk.Entry(petshop, width=75)
	caixa_nome.pack()
	caixa_nome.place(relx=0.55, rely=0.3, anchor="center")

	quantidade = tk.Label(petshop, text="QUANTIDADE: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	quantidade.pack()
	quantidade.place(relx=0.4, rely=0.35, anchor="center")
	caixa_quantidade = tk.Entry(petshop, width=68)
	caixa_quantidade.pack()
	caixa_quantidade.place(relx=0.56, rely=0.35, anchor="center")

	valor_venda = tk.Label(petshop, text="VALOR DA VENDA: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	valor_venda.pack()
	valor_venda.place(relx=0.4, rely=0.4, anchor="center")
	caixa_valor_venda = tk.Entry(petshop, width=60)
	caixa_valor_venda.pack()
	caixa_valor_venda.place(relx=0.57, rely=0.4, anchor="center")

	valor_compra = tk.Label(petshop, text="VALOR DA COMPRA: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	valor_compra.pack()
	valor_compra.place(relx=0.4, rely=0.45, anchor="center")
	caixa_valor_compra = tk.Entry(petshop, width=60)
	caixa_valor_compra.pack()
	caixa_valor_compra.place(relx=0.57, rely=0.45, anchor="center")

	disponibilidade = tk.Label(petshop, text="DISPONIBILIDADE: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	disponibilidade.pack()
	disponibilidade.place(relx=0.4, rely=0.5, anchor="center")
	caixa_disponibilidade = tk.Entry(petshop, width=60)
	caixa_disponibilidade.pack()
	caixa_disponibilidade.place(relx=0.57, rely=0.5, anchor="center")

	botao_cadastrar = tk.Button(petshop, text="CADASTRAR", width='20', height='0', font="Arial 10 bold", fg="#000842")
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

	texto_estoque = tk.Label(petshop, text="CONFIGURAÇÕES DE ANIMAIS", font="Arial 30 bold", bg="lightblue", fg="#000842")
	texto_estoque.pack()
	texto_estoque.place(relx=0.5, rely=0.1, anchor="center")

	codigo = tk.Label(petshop, text="CÓDIGO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	codigo.pack()
	codigo.place(relx=0.4, rely=0.2, anchor="center")
	caixa_codigo = tk.Entry(petshop, width=75)
	caixa_codigo.pack()
	caixa_codigo.place(relx=0.55, rely=0.2, anchor="center")

	tipo = tk.Label(petshop, text="TIPO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	tipo.pack()
	tipo.place(relx=0.4, rely=0.25, anchor="center")
	caixa_tipo = tk.Entry(petshop, width=75)
	caixa_tipo.pack()
	caixa_tipo.place(relx=0.55, rely=0.25, anchor="center")

	nome = tk.Label(petshop, text="NOME: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	nome.pack()
	nome.place(relx=0.4, rely=0.3, anchor="center")
	caixa_nome = tk.Entry(petshop, width=75)
	caixa_nome.pack()
	caixa_nome.place(relx=0.55, rely=0.3, anchor="center")

	quantidade = tk.Label(petshop, text="QUANTIDADE: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	quantidade.pack()
	quantidade.place(relx=0.4, rely=0.35, anchor="center")
	caixa_quantidade = tk.Entry(petshop, width=68)
	caixa_quantidade.pack()
	caixa_quantidade.place(relx=0.56, rely=0.35, anchor="center")

	valor_venda = tk.Label(petshop, text="VALOR DA VENDA: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	valor_venda.pack()
	valor_venda.place(relx=0.4, rely=0.4, anchor="center")
	caixa_valor_venda = tk.Entry(petshop, width=60)
	caixa_valor_venda.pack()
	caixa_valor_venda.place(relx=0.57, rely=0.4, anchor="center")

	valor_compra = tk.Label(petshop, text="VALOR DA COMPRA: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	valor_compra.pack()
	valor_compra.place(relx=0.4, rely=0.45, anchor="center")
	caixa_valor_compra = tk.Entry(petshop, width=60)
	caixa_valor_compra.pack()
	caixa_valor_compra.place(relx=0.57, rely=0.45, anchor="center")

	disponibilidade = tk.Label(petshop, text="DISPONIBILIDADE: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	disponibilidade.pack()
	disponibilidade.place(relx=0.4, rely=0.5, anchor="center")
	caixa_disponibilidade = tk.Entry(petshop, width=60)
	caixa_disponibilidade.pack()
	caixa_disponibilidade.place(relx=0.57, rely=0.5, anchor="center")

	botao_cadastrar = tk.Button(petshop, text="CADASTRAR", width='20', height='0', font="Arial 10 bold", fg="#000842")
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

def cadastrar_banho():
	for widget in petshop.winfo_children():
		widget.destroy()

	texto_estoque = tk.Label(petshop, text="CONFIGURAÇÕES DE BANHO E TOSA", font="Arial 30 bold", bg="lightblue", fg="#000842")
	texto_estoque.pack()
	texto_estoque.place(relx=0.5, rely=0.1, anchor="center")

	codigo = tk.Label(petshop, text="CÓDIGO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	codigo.pack()
	codigo.place(relx=0.4, rely=0.2, anchor="center")
	caixa_codigo = tk.Entry(petshop, width=75)
	caixa_codigo.pack()
	caixa_codigo.place(relx=0.55, rely=0.2, anchor="center")

	tipo = tk.Label(petshop, text="TIPO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	tipo.pack()
	tipo.place(relx=0.4, rely=0.25, anchor="center")
	caixa_tipo = tk.Entry(petshop, width=75)
	caixa_tipo.pack()
	caixa_tipo.place(relx=0.55, rely=0.25, anchor="center")

	nome = tk.Label(petshop, text="NOME: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	nome.pack()
	nome.place(relx=0.4, rely=0.3, anchor="center")
	caixa_nome = tk.Entry(petshop, width=75)
	caixa_nome.pack()
	caixa_nome.place(relx=0.55, rely=0.3, anchor="center")

	quantidade = tk.Label(petshop, text="QUANTIDADE: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	quantidade.pack()
	quantidade.place(relx=0.4, rely=0.35, anchor="center")
	caixa_quantidade = tk.Entry(petshop, width=68)
	caixa_quantidade.pack()
	caixa_quantidade.place(relx=0.56, rely=0.35, anchor="center")

	valor_venda = tk.Label(petshop, text="VALOR DA VENDA: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	valor_venda.pack()
	valor_venda.place(relx=0.4, rely=0.4, anchor="center")
	caixa_valor_venda = tk.Entry(petshop, width=60)
	caixa_valor_venda.pack()
	caixa_valor_venda.place(relx=0.57, rely=0.4, anchor="center")

	valor_compra = tk.Label(petshop, text="VALOR DA COMPRA: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	valor_compra.pack()
	valor_compra.place(relx=0.4, rely=0.45, anchor="center")
	caixa_valor_compra = tk.Entry(petshop, width=60)
	caixa_valor_compra.pack()
	caixa_valor_compra.place(relx=0.57, rely=0.45, anchor="center")

	disponibilidade = tk.Label(petshop, text="DISPONIBILIDADE: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	disponibilidade.pack()
	disponibilidade.place(relx=0.4, rely=0.5, anchor="center")
	caixa_disponibilidade = tk.Entry(petshop, width=60)
	caixa_disponibilidade.pack()
	caixa_disponibilidade.place(relx=0.57, rely=0.5, anchor="center")

	botao_cadastrar = tk.Button(petshop, text="CADASTRAR", width='20', height='0', font="Arial 10 bold", fg="#000842")
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


###############DEF'S ALTERAR

def alterar_estoque():
	for widget in petshop.winfo_children():
		widget.destroy()

	texto_estoque = tk.Label(petshop, text="ALTERAÇÃO NO ESTOQUE", font="Arial 30 bold", bg="lightblue", fg="#000842")
	texto_estoque.pack()
	texto_estoque.place(relx=0.5, rely=0.1, anchor="center")

	codigo_alteracao = tk.Label(petshop, text="ID DE ALTERAÇÃO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	codigo_alteracao.pack()
	codigo_alteracao.place(relx=0.4, rely=0.2, anchor="center")
	caixa_codigo = tk.Entry(petshop, width=68)
	caixa_codigo.pack()
	caixa_codigo.place(relx=0.55, rely=0.2, anchor="center")

	tipo = tk.Label(petshop, text="TIPO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	tipo.pack()
	tipo.place(relx=0.4, rely=0.25, anchor="center")
	caixa_tipo = tk.Entry(petshop, width=75)
	caixa_tipo.pack()
	caixa_tipo.place(relx=0.55, rely=0.25, anchor="center")

	nome = tk.Label(petshop, text="NOME: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	nome.pack()
	nome.place(relx=0.4, rely=0.3, anchor="center")
	caixa_nome = tk.Entry(petshop, width=75)
	caixa_nome.pack()
	caixa_nome.place(relx=0.55, rely=0.3, anchor="center")

	quantidade = tk.Label(petshop, text="QUANTIDADE: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	quantidade.pack()
	quantidade.place(relx=0.4, rely=0.35, anchor="center")
	caixa_quantidade = tk.Entry(petshop, width=68)
	caixa_quantidade.pack()
	caixa_quantidade.place(relx=0.56, rely=0.35, anchor="center")

	valor_venda = tk.Label(petshop, text="VALOR DA VENDA: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	valor_venda.pack()
	valor_venda.place(relx=0.4, rely=0.4, anchor="center")
	caixa_valor_venda = tk.Entry(petshop, width=60)
	caixa_valor_venda.pack()
	caixa_valor_venda.place(relx=0.57, rely=0.4, anchor="center")

	valor_compra = tk.Label(petshop, text="VALOR DA COMPRA: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	valor_compra.pack()
	valor_compra.place(relx=0.4, rely=0.45, anchor="center")
	caixa_valor_compra = tk.Entry(petshop, width=60)
	caixa_valor_compra.pack()
	caixa_valor_compra.place(relx=0.57, rely=0.45, anchor="center")

	disponibilidade = tk.Label(petshop, text="DISPONIBILIDADE: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	disponibilidade.pack()
	disponibilidade.place(relx=0.4, rely=0.5, anchor="center")
	caixa_disponibilidade = tk.Entry(petshop, width=60)
	caixa_disponibilidade.pack()
	caixa_disponibilidade.place(relx=0.57, rely=0.5, anchor="center")

	botao_cadastrar = tk.Button(petshop, text="CADASTRAR", width='20', height='0', font="Arial 10 bold", fg="#000842")
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

def alterar_venda():
	for widget in petshop.winfo_children():
		widget.destroy()

	texto_estoque = tk.Label(petshop, text="ALTERAÇÃO DE VENDAS", font="Arial 30 bold", bg="lightblue", fg="#000842")
	texto_estoque.pack()
	texto_estoque.place(relx=0.5, rely=0.1, anchor="center")

	codigo = tk.Label(petshop, text="CÓDIGO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	codigo.pack()
	codigo.place(relx=0.4, rely=0.2, anchor="center")
	caixa_codigo = tk.Entry(petshop, width=75)
	caixa_codigo.pack()
	caixa_codigo.place(relx=0.55, rely=0.2, anchor="center")

	tipo = tk.Label(petshop, text="TIPO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	tipo.pack()
	tipo.place(relx=0.4, rely=0.25, anchor="center")
	caixa_tipo = tk.Entry(petshop, width=75)
	caixa_tipo.pack()
	caixa_tipo.place(relx=0.55, rely=0.25, anchor="center")

	nome = tk.Label(petshop, text="NOME: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	nome.pack()
	nome.place(relx=0.4, rely=0.3, anchor="center")
	caixa_nome = tk.Entry(petshop, width=75)
	caixa_nome.pack()
	caixa_nome.place(relx=0.55, rely=0.3, anchor="center")

	quantidade = tk.Label(petshop, text="QUANTIDADE: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	quantidade.pack()
	quantidade.place(relx=0.4, rely=0.35, anchor="center")
	caixa_quantidade = tk.Entry(petshop, width=68)
	caixa_quantidade.pack()
	caixa_quantidade.place(relx=0.56, rely=0.35, anchor="center")

	valor_venda = tk.Label(petshop, text="VALOR DA VENDA: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	valor_venda.pack()
	valor_venda.place(relx=0.4, rely=0.4, anchor="center")
	caixa_valor_venda = tk.Entry(petshop, width=60)
	caixa_valor_venda.pack()
	caixa_valor_venda.place(relx=0.57, rely=0.4, anchor="center")

	valor_compra = tk.Label(petshop, text="VALOR DA COMPRA: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	valor_compra.pack()
	valor_compra.place(relx=0.4, rely=0.45, anchor="center")
	caixa_valor_compra = tk.Entry(petshop, width=60)
	caixa_valor_compra.pack()
	caixa_valor_compra.place(relx=0.57, rely=0.45, anchor="center")

	disponibilidade = tk.Label(petshop, text="DISPONIBILIDADE: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	disponibilidade.pack()
	disponibilidade.place(relx=0.4, rely=0.5, anchor="center")
	caixa_disponibilidade = tk.Entry(petshop, width=60)
	caixa_disponibilidade.pack()
	caixa_disponibilidade.place(relx=0.57, rely=0.5, anchor="center")

	botao_cadastrar = tk.Button(petshop, text="CADASTRAR", width='20', height='0', font="Arial 10 bold", fg="#000842")
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

def alterar_animais():
	for widget in petshop.winfo_children():
		widget.destroy()

	texto_estoque = tk.Label(petshop, text="ALTERAÇÃO DE ANIMAIS", font="Arial 30 bold", bg="lightblue", fg="#000842")
	texto_estoque.pack()
	texto_estoque.place(relx=0.5, rely=0.1, anchor="center")

	codigo = tk.Label(petshop, text="CÓDIGO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	codigo.pack()
	codigo.place(relx=0.4, rely=0.2, anchor="center")
	caixa_codigo = tk.Entry(petshop, width=75)
	caixa_codigo.pack()
	caixa_codigo.place(relx=0.55, rely=0.2, anchor="center")

	tipo = tk.Label(petshop, text="TIPO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	tipo.pack()
	tipo.place(relx=0.4, rely=0.25, anchor="center")
	caixa_tipo = tk.Entry(petshop, width=75)
	caixa_tipo.pack()
	caixa_tipo.place(relx=0.55, rely=0.25, anchor="center")

	nome = tk.Label(petshop, text="NOME: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	nome.pack()
	nome.place(relx=0.4, rely=0.3, anchor="center")
	caixa_nome = tk.Entry(petshop, width=75)
	caixa_nome.pack()
	caixa_nome.place(relx=0.55, rely=0.3, anchor="center")

	quantidade = tk.Label(petshop, text="QUANTIDADE: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	quantidade.pack()
	quantidade.place(relx=0.4, rely=0.35, anchor="center")
	caixa_quantidade = tk.Entry(petshop, width=68)
	caixa_quantidade.pack()
	caixa_quantidade.place(relx=0.56, rely=0.35, anchor="center")

	valor_venda = tk.Label(petshop, text="VALOR DA VENDA: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	valor_venda.pack()
	valor_venda.place(relx=0.4, rely=0.4, anchor="center")
	caixa_valor_venda = tk.Entry(petshop, width=60)
	caixa_valor_venda.pack()
	caixa_valor_venda.place(relx=0.57, rely=0.4, anchor="center")

	valor_compra = tk.Label(petshop, text="VALOR DA COMPRA: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	valor_compra.pack()
	valor_compra.place(relx=0.4, rely=0.45, anchor="center")
	caixa_valor_compra = tk.Entry(petshop, width=60)
	caixa_valor_compra.pack()
	caixa_valor_compra.place(relx=0.57, rely=0.45, anchor="center")

	disponibilidade = tk.Label(petshop, text="DISPONIBILIDADE: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	disponibilidade.pack()
	disponibilidade.place(relx=0.4, rely=0.5, anchor="center")
	caixa_disponibilidade = tk.Entry(petshop, width=60)
	caixa_disponibilidade.pack()
	caixa_disponibilidade.place(relx=0.57, rely=0.5, anchor="center")

	botao_cadastrar = tk.Button(petshop, text="CADASTRAR", width='20', height='0', font="Arial 10 bold", fg="#000842")
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

	codigo = tk.Label(petshop, text="CÓDIGO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	codigo.pack()
	codigo.place(relx=0.4, rely=0.2, anchor="center")
	caixa_codigo = tk.Entry(petshop, width=75)
	caixa_codigo.pack()
	caixa_codigo.place(relx=0.55, rely=0.2, anchor="center")

	tipo = tk.Label(petshop, text="TIPO: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	tipo.pack()
	tipo.place(relx=0.4, rely=0.25, anchor="center")
	caixa_tipo = tk.Entry(petshop, width=75)
	caixa_tipo.pack()
	caixa_tipo.place(relx=0.55, rely=0.25, anchor="center")

	nome = tk.Label(petshop, text="NOME: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	nome.pack()
	nome.place(relx=0.4, rely=0.3, anchor="center")
	caixa_nome = tk.Entry(petshop, width=75)
	caixa_nome.pack()
	caixa_nome.place(relx=0.55, rely=0.3, anchor="center")

	quantidade = tk.Label(petshop, text="QUANTIDADE: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	quantidade.pack()
	quantidade.place(relx=0.4, rely=0.35, anchor="center")
	caixa_quantidade = tk.Entry(petshop, width=68)
	caixa_quantidade.pack()
	caixa_quantidade.place(relx=0.56, rely=0.35, anchor="center")

	valor_venda = tk.Label(petshop, text="VALOR DA VENDA: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	valor_venda.pack()
	valor_venda.place(relx=0.4, rely=0.4, anchor="center")
	caixa_valor_venda = tk.Entry(petshop, width=60)
	caixa_valor_venda.pack()
	caixa_valor_venda.place(relx=0.57, rely=0.4, anchor="center")

	valor_compra = tk.Label(petshop, text="VALOR DA COMPRA: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	valor_compra.pack()
	valor_compra.place(relx=0.4, rely=0.45, anchor="center")
	caixa_valor_compra = tk.Entry(petshop, width=60)
	caixa_valor_compra.pack()
	caixa_valor_compra.place(relx=0.57, rely=0.45, anchor="center")

	disponibilidade = tk.Label(petshop, text="DISPONIBILIDADE: ", font="Arial 20 bold", bg="lightblue", fg="#000842" )
	disponibilidade.pack()
	disponibilidade.place(relx=0.4, rely=0.5, anchor="center")
	caixa_disponibilidade = tk.Entry(petshop, width=60)
	caixa_disponibilidade.pack()
	caixa_disponibilidade.place(relx=0.57, rely=0.5, anchor="center")

	botao_cadastrar = tk.Button(petshop, text="CADASTRAR", width='20', height='0', font="Arial 10 bold", fg="#000842")
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

def pesquisar_estoque():
	for widget in petshop.winfo_children():
		widget.destroy()

	texto = tk.Label(petshop, text="O QUE VOCÊ DESEJA PESQUISAR NO ESTOQUE?", font="Arial 45 bold", bg="lightblue", fg="#000842")
	texto.place(relx=0.5, rely=0.2, anchor="center")
	
	caixa_pesquisa_estoque = tk.Entry(petshop, width=120)
	caixa_pesquisa_estoque.pack()
	caixa_pesquisa_estoque.place(relx=0.45, rely=0.3, anchor="center")

	botao_pesquisar = tk.Button(petshop, text="PESQUISAR", width='20', height='0', font="Arial 10 bold", fg="#000842")
	botao_pesquisar.pack()
	botao_pesquisar.place(relx=0.7, rely=0.3, anchor="center")

	botao_pesquisar.bind("<Enter>", lambda event: botao_pesquisar.config(bg='#000842', fg='white'))
	botao_pesquisar.bind("<Leave>", lambda event: botao_pesquisar.config(bg='white', fg='#000842',))

	botao_voltar = tk.Button(petshop, text="VOLTAR AO MENU", width='20', height='0', font="Arial 10 bold", fg="#000842", command=voltar)
	botao_voltar.pack()
	botao_voltar.place(relx=0.5, rely=0.95, anchor="center")

	botao_voltar.bind("<Enter>", lambda event: botao_voltar.config(bg='#000842', fg='white'))
	botao_voltar.bind("<Leave>", lambda event: botao_voltar.config(bg='white', fg='#000842',))

def pesquisar_venda():
	for widget in petshop.winfo_children():
		widget.destroy()

	texto = tk.Label(petshop, text="O QUE VOCÊ DESEJA PESQUISAR NAS VENDAS?", font="Arial 45 bold", bg="lightblue", fg="#000842")
	texto.place(relx=0.5, rely=0.2, anchor="center")
	
	caixa_pesquisa_estoque = tk.Entry(petshop, width=120)
	caixa_pesquisa_estoque.pack()
	caixa_pesquisa_estoque.place(relx=0.45, rely=0.3, anchor="center")

	botao_pesquisar = tk.Button(petshop, text="PESQUISAR", width='20', height='0', font="Arial 10 bold", fg="#000842")
	botao_pesquisar.pack()
	botao_pesquisar.place(relx=0.7, rely=0.3, anchor="center")

	botao_pesquisar.bind("<Enter>", lambda event: botao_pesquisar.config(bg='#000842', fg='white'))
	botao_pesquisar.bind("<Leave>", lambda event: botao_pesquisar.config(bg='white', fg='#000842',))

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
	
	caixa_pesquisa_estoque = tk.Entry(petshop, width=120)
	caixa_pesquisa_estoque.pack()
	caixa_pesquisa_estoque.place(relx=0.45, rely=0.3, anchor="center")

	botao_pesquisar = tk.Button(petshop, text="PESQUISAR", width='20', height='0', font="Arial 10 bold", fg="#000842")
	botao_pesquisar.pack()
	botao_pesquisar.place(relx=0.7, rely=0.3, anchor="center")

	botao_pesquisar.bind("<Enter>", lambda event: botao_pesquisar.config(bg='#000842', fg='white'))
	botao_pesquisar.bind("<Leave>", lambda event: botao_pesquisar.config(bg='white', fg='#000842',))

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
	
	caixa_pesquisa_estoque = tk.Entry(petshop, width=120)
	caixa_pesquisa_estoque.pack()
	caixa_pesquisa_estoque.place(relx=0.45, rely=0.3, anchor="center")

	botao_pesquisar = tk.Button(petshop, text="PESQUISAR", width='20', height='0', font="Arial 10 bold", fg="#000842")
	botao_pesquisar.pack()
	botao_pesquisar.place(relx=0.7, rely=0.3, anchor="center")

	botao_pesquisar.bind("<Enter>", lambda event: botao_pesquisar.config(bg='#000842', fg='white'))
	botao_pesquisar.bind("<Leave>", lambda event: botao_pesquisar.config(bg='white', fg='#000842',))

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