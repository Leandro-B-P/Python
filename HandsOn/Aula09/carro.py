#!/usr/bin/python

class Carro:
	cor = "Vermelho"
	placa = ""
	modelo = ""
	
	def __init__(self):
 
		self.cor = "Vermelho"
		self.placa = "HYT-9863"
		self.modelo = "Hatch"
		self.ano = "2014"
		self.fabricacao = "2013"
		self.velocidade = 0
		self.velocidade_max = 200
		print "Instanciou o objeto carro!\n"
	
	def acelerar(self):
		if self.velocidade < self.velocidade_max:

			self.velocidade += 100

			print "Velocidade atual: ",self.velocidade
		
		else:
			print "Voce atingiu o limite de velocidade!"
	
	
if __name__=='__main__':
	celta = Carro()
	Carro.cor = "Verde"
	celta.acelerar()
	celta.acelerar()
	celta.acelerar()
	print Carro.cor
