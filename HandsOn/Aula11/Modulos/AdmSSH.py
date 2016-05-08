#!/usr/bin/python

import sys
import json
import banco


class AdmSSH:


	def exibeMenu(self):
    	print "\n1 - Cadastrar usuarios"
    	print "2 - Listar todos os usuarios"
    	print "3 - Deletar um usuario"
    	print "4 - Autenticar autenticar um usuario"
		print "5 - Logar no servidor"
    	print "6 - Sair"

	def cadastraUsuario(self):
		login = raw_input("\nDigite o nome do usuario: ")
		senha = raw_input("\nDigite a senha de usuario: ")
		novoo_usuario = User(login,senha)
		banco.cadastrar_usuario(login,senha)
		print "\nUsuario cadastrado com sucesso!"
	
###############################################################################
	def listarUsuario(self):	
		banco.listar_usuarios()
	
	def deletarUsuarios(self):
		banco.listar_usuarios()
		usuario = input("\nDigite o id do usuario a ser deletado:")
		banco.deletar_usuario(usuario)
	##############################################################################    
	def autenticaUsuario(self):
	   
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
	def sairMenu(self):

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


