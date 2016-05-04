#!/usr/bin/python
#
#NoSql
###################

from pymongo import MongoClient

def conecta_banco():

	client = MongoClient("127.0.0.1")
	db = client["teste"]
	return db

def listarServidores():
	db = conecta_banco()
	for s in db.servers.find():

		print s.get("nome"),"-",s.get("endereco"),"-",s.get("_id"),"Administradores",s.get("administradores")

def cadastrarServidor():
	novo_servidor = {"nome":"","endereco":"","administradores":""}
	novo_servidor["nome"]= raw_input("Digite o nome do servidor: ")
	novo_servidor["endereco"]= raw_input("Digite o endereco do servidor: ")
	db = conecta_banco()
	db.servers.insert(novo_servidor)
	print "\nServidor cadastrado com sucesso!\n"

def definirAdministrador(endereco):
#	senha_admin = {"login":""}
	db = conecta_banco()
	login = raw_input("Digite login do administrador: ")
	busca = {"endereco":endereco}
	administradores = {"administradores":{"login":login}}
	valores = {"$addToSet":administradores}
	db.servers.update(busca,valores)
	print "Dados atualizados!"

def deletarServidor(endereco):
	db = conecta_banco()
	busca = {"endereco":endereco}
	db.servers.remove(busca)
	print "Servidor deletado com sucesso!"

def deletarAdministrador(endereco):
	db = conecta_banco()
	login = raw_input("Digite login do administrador: ")
	busca = {"endereco":endereco,"administradores.login":login}
	valores = {"administradores":{"login":login}}
	db.servers.update(busca,{"$pull":valores})
	print "Administrador deletado com sucesso!"

if __name__ == '__main__':
	#cadastrarServidor()
	listarServidores()
	endereco = raw_input("Digite o endereco ip do servidor: ")
	#definirAdministrador(endereco)
	deletarAdministrador(endereco)
	#deletarServidor(endereco)
