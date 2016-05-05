#!/usr/bin/python


from docker import Docker
from ssh import SSH
import sys, json

class Provisionamento:

	def __init__(self):
		pass

	def contratar(self,name,template):
		d = Docker()
		s = SSH()
		s.exec_command(d.createContainer(name))
		#metodo da propria classe
		self.instalar(name,template)
		endereco = s.exec_command(d.getContainerAddress(name))
		endereco = json.loads(endereco)
		print endereco[0].get("NetworkSettings")\
						 .get("Networks")\
						 .get("bridge")\
						 .get("IPAddress")

	def instalar(self,name,template):
		with open("Templates/%s.json"%template,"r") as f:
			comandos = json.loads(f.read())
		d = Docker()
		s = SSH() 
		for c in comandos.get("comandos"):
			print s.exec_command(d.execCommand(name,c))

	def cancelar(self,name):
		d = Docker()
		s = SSH()
		print s.exec_command(d.removeContainer(name))

	def listar_servicos(self):
		d = Docker()
		s = SSH()
		print s.exec_command(d.listContainer())


if __name__=='__main__':
	prov = Provisionamento()
	prov.listar_servicos()
	servico = sys.argv[1]
	template = sys.argv[2]
	prov.contratar(servico,template)
