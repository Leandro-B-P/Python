#!/usr/bin/python

from Modulos.docker import Docker
from Models.Model import session, Servers as ServerModel

class Server:

	def __init__(self,nome=""):
		self.nome = nome
	
	def instalar(self):

		try:
			d = Docker()
			d.createContainer(self.nome)
			endereco = d.getContainerAddres(self.nome)
			s = ServerModel()
			s.nome = self.nome
			s.descricao = endereco
			session.add(s)
			session.commit()	

		except Exception as e:
			session.rollback()	
			print "Falhou ao instalar o servidor: ",e

	def listar(self):
		try:

			servidores = session.query(ServerModel).all()
			for s in servidores:
				print s.id,"-",s.nome,"-",s.descricao

		except Exception as e:
			print "Falhou ao listar:",e

	def remove(self,nome):
		try:

			servidor = session.query(ServerModel)\
							  .filter(SeverModel.nome==nome)\
							  .first()			
			if servidor:
				d = Docker()
				d.removeContainer(nome)
				session.delete(servidor)
				sessionn.commit()
				print "Servidor removido com sucesso!"
			else:
				print "Servidor nao encontrado."

		except Exception as e:
			print "Falhou ao remover servidor:",e
