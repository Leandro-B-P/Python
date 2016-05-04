#!/usr/bin/python

import sys

#Dicionario
servidor = {"nome":"DNS",
	    "vcpus": 4,
	    "memoria": 2048,
	    "disco":[{"vda":"50G"},{"vdb":"50G"}]
	   }


#print "discos: ", servidor.get("disco")[1]..get("vdb")

for d in servidor.get("disco"):
    chave = d.keys()[0]
    print chave, d.get(chave)

sys.exit()

#Matriz

matriz = [[1,22,33,],
          [25,63,89]]

print matriz[1][2]

lista =["python", "c", "asp", "vb", "ruby", "java", "go"]


for item in lista:
    if item == "nodejs":
        
        print "Nodejs encontrado"
else:

    print "Nao encontrado"

lista =["python", "c", "asp", "vb", "ruby", "java", "go"]
for pos, item in enumerate(lista):
    print pos," - ",item


valor = ""
print "Digite #sair para sair"
while valor != "#sair":
    valor = raw_input("Digite uma opcao: ")




contador = 1

while contador < 10:
   print contador
   contador += 1


for i in range(0, 10):
    print i
