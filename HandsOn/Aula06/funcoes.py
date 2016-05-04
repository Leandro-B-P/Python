#!/usr/bin/python

import sys
import json
import banco

usuarios = []


def exibeMenu():
    print "\n1 - Para cadastrar usuarios"
    print "2 - Para listar todos os usuarios"
    print "3 - Para deletar um usuario"
    print "4 - Para autenticar um usuario"
    print "5 - Sair"

def cadastraUsuario():
	login = raw_input("\nDigite o nome do usuario: ")
	senha = raw_input("\nDigite a senha de usuario: ")
	banco.cadastrar_usuario(login,senha)
	print "\nUsuario cadastrado com sucesso!"
	
###############################################################################
def listarUsuario():	
	banco.listar_usuarios()
	
def deletarUsuarios():
	banco.listar_usuarios()
	usuario = input("\nDigite o id do usuario a ser deletado:")
	banco.deletar_usuario(usuario)
##############################################################################    
def autenticaUsuario():
   
	login = raw_input("\nDigite o login do usuario: ")
	senha = raw_input("\nDigite a senha do usuario: ")
	usuario = banco.buscar_usuario(login)
	for u in usuario:
		if u[1] == login and u[2] == senha:
			print "\nSeja bem vindo! "+u[1]
		break
	else:
		print "\nSenha incorreta!"
############################################################################		
def sairMenu():

    sys.exit()

def switch(opcao,usuarios):
    try:

        dic = {1:cadastraUsuario,
               2:listarUsuario,
               3:deletarUsuarios,
               4:autenticaUsuario,
               5:sairMenu}
    
        dic[opcao]()
    except Exception as e:
        print "Voce digitou uma opcao invalida",e
while True:
	try:
		exibeMenu()
		opcao = input("\nInsira a opcao desejada: ")
		switch(opcao,usuarios)
   
	except Exception as e:
		print "Voce digitou uma opcao invalida",e


