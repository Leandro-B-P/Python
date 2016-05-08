#!/usr/bin/python

from Servidor import Servidor

class Fisico(Servidor):
	def __init__(self):
		Servidor.__init__(self)
		self.slots = 4
		self.slots_ocupados = 2
		self.memorias = 4
		self.memoria_ocupadas = 2
	
	
		

if __name__ == '__main__':
	f = Fisico()
	print "CPU:",f.cpu
	print "MEM:",f.memoria
	print "DISCO:",f.disco
	f.acesso()
	print "===================="
	f.contratarDisco()
	f.contratarDisco()
	f.contratarDisco()
	f.contratarMemoria()
	f.contratarMemoria()
	f.contratarMemoria()
	
