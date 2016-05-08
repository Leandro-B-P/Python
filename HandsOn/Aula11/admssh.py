#!/usr/bin/python

import sys
from Classes.User import User
from Classes.Server import Server

class AdmSSH:


	def exibeMenu(self):
		print "1 - Cadastrar usuarios"
		print "2 - Listar todos os usuarios"
		print "3 - Deletar um usuario"
		print "4 - Autenticar autenticar um usuario"
		print "5 - Criar no servidor"
		print "6 - Listar Servidor"
		print "7 - Remover Servidor"
		print "8 - Sair"		
		
	def cadastraUsuario(self):
		login = raw_input("\nDigite o nome do usuario: ")
		senha = raw_input("\nDigite a senha de usuario: ")
		novo_usuario = User(login,senha)
		novo_usuario.save()
		
	
###############################################################################

	def listarUsuario(self):
	
		all_users = User()
		all_users = all_users.listAll()
		for user in all_users:
			print user.id,"-",user.nome
##############################################################################
	
	def deletarUsuarios(self):
		login = raw_input("\nDigite o login do usuario: ")
		user = User()
		user = user.get(login)
		if user:
			user.remove()
		else:
			
			print "Usuario nao encontrado!"
	##############################################################################    
	def autenticaUsuario(self):
	   
		login = raw_input("\nDigite o login do usuario: ")
		senha = raw_input("\nDigite a senha do usuario: ")
		user = User()
		user.get(login)
		if user:
			if user.nome == login and user.senha == senha:
				print "\nSeja bem vindo %s! ",user.nome
			
			else:
				print "\nAcesso negado!"
		else:
			
			print "\nUsuario nao encontrado!"


	def criarServidor(self):
		nome = raw_input("Digite o nome do servidor: ")
		novo = Server(nome)
		novo.instalar()
		
	############################################################################		
	def listarServidor(self):
		s = Server()

		s.listar()
		
	def removerServidor(self):
		nome = raw_input("Digite o nome do servidor:")
		s = Server()
		s.remove(nome)
	def sairMenu(self):

		sys.exit()

	def switch(self,opcao):
		try:

		    dic = {1:self.cadastraUsuario,
		           2:self.listarUsuario,
		           3:self.deletarUsuarios,
		           4:self.autenticaUsuario,
				   5:self.criarServidor,
				   6:self.listarServidor,
				   7:self.removerServidor,
		           8:self.sairMenu}
		
		    dic[opcao]()
		except Exception as e:
		    print "Voce digitou uma opcao invalida",e
while True:
	try:
		admssh = AdmSSH()
		admssh.exibeMenu()
		opcao = input("\nInsira a opcao desejada: ")
		admssh.switch(opcao)
   
	except Exception as e:
		
		print "Voce digitou uma opcao invalida",e


