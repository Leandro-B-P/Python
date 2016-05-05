#!/usr/bin/python

class Docker:
	def __init__(self):
		self.image = "ubuntu"
	

	def createContainer(self,name):
		cmd = "docker run -tdi --name %s %s /bin/bash"%(name,self.image)
		return cmd

	def removeContainer(self,name):
		cmd ="docker stop %s && docker rm %s"%(name,name)
		return cmd

	def listContainer(self):
		cmd = "docker ps -a"
		return cmd

	def getContainerAddress(self,name):
		cmd = "docker inspect %s"%name
		return cmd
		
	def execCommand(self,name,com):
		cmd = "docker exec %s %s"%(name,com)
		return cmd


