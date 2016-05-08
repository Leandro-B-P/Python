#!/usr/bin/python

import sys
import json

usuarios = []

def exibeMenu():
    print "\n1 - Para cadastrar usuarios"
    print "2 - Para listar todos os usuarios"
    print "3 - Para deletar um usuario"
    print "4 - Para autenticar um usuario"
    print "5 - Sair"

def cadastraUsuario(usuarios):

	with open("banco.txt","r") as f:
		arquivo = json.loads(f.read())
	novo_usuario = {"login":"","senha":""}
	novo_usuario["login"] = raw_input("\nDigite o nome do usuario: ")
	novo_usuario["senha"] = raw_input("\nDigite a senha de usuario: ")
	arquivo["usuarios"].append(novo_usuario)
	with open("banco.txt","w") as f:
		f.write(json.dumps(arquivo))
	print "\nUsuario cadastrado com sucesso!"
###############################################################################
def listarUsuario(usuarios):	
	with open("banco.txt","r") as f:
		conteudo = f.read()
	print conteudo
def deletarUsuarios():
    print "Deletar usuarios"
##############################################################################    
def autenticaUsuario(usuarios):
    with open("banco.txt","r") as f:
		arquivo = json.loads(f.read())
		login = raw_input("\nDigite o login do usuario: ")
		senha = raw_input("\nDigite a senha do usuario: ")
		for usuario in arquivo.get("usuarios"):
			if usuario["login"]== login and usuario.get("senha")== senha:	
				print "\nUsuario autenticado!\n"
				break
		else:
			print "\nVoce nao tem permissao para acessar este sistema!\n"
############################################################################		
def sairMenu(usuarios):

    sys.exit()

def switch(opcao,usuarios):
    try:

        dic = {1:cadastraUsuario,
               2:listarUsuario,
               3:deletarUsuarios,
               4:autenticaUsuario,
               5:sairMenu}
    
        dic[opcao](usuarios)
    except Exception as e:
        print "Voce digitou uma opcao invalida",e
while True:
	try:
		exibeMenu()
		opcao = input("\nInsira a opcao desejada: ")
		switch(opcao,usuarios)
   
	except Exception as e:
		print "Voce digitou uma opcao invalida",e


