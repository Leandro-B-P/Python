#!/usr/bin/python

from Modulos.ssh import SSH
import json
from Modulos.Logs import Logs

class Docker(SSH,Logs):
	def __init__(self):
		SSH.__init__(self)
		self.log_file = "docker.log"
		self.image = "ubuntu"
	

	def createContainer(self,name):
		self.writeLogs("Iniciando criacao do container...")
		cmd = "docker run -tdi --name %s %s /bin/bash"%(name,self.image)
		print self.exec_command(cmd)

	def removeContainer(self,name):
		self.writeLogs("Removendo container %ss"%name)
		cmd ="docker stop %s && docker rm %s"%(name,name)
		print self.exec_command(cmd)
		self.writeLogs("Remocao finalizada...")

	def listContainer(self):
		cmd = "docker ps -a"
		print self.exec_command(cmd)

	def getContainerAddress(self,name):
		self.writeLogs("Buscando container...")
		cmd = "docker inspect %s"%name
		endereco = self.exec_command(cmd)
		endereco = json.loads(endereco)
		endereco = endereco[0].get("NetworkSettings")\
						 	  .get("Networks")\
						   	  .get("bridge")\
						 	  .get("IPAddress")
		
		self.writeLogs("Busca finalizada")
		return endereco

	def execCommand(self,name,com):
		self.writeLogs("Executando comando %s "%com)
		cmd = "docker exec %s %s"%(name,com)
		print self.exec_command(cmd)
		self.writeLogs("Comando finalizado...")

