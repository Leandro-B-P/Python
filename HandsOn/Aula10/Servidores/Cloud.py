#!/usr/bin/python

from Servidor import Servidor

class Cloud(Servidor):
	pass

	def acesso(self):
		print "Acesso feito via ssh!"

	def contratarCPU(self):
		self.cpu += 1
		print "Total de Cpus: ",self.cpu

if __name__ == '__main__':
	c = Cloud()
	print "CPU:",c.cpu
	print "MEM:",c.memoria
	print "DISCO:",c.disco
	c.acesso()
	c.contratarCPU()
	c.contratarCPU()
	c.contratarCPU()

	
