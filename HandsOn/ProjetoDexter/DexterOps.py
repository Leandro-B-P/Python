#!/usr/bin/python

servicos = []

srv1 = {"id":1,"nome":"website"}
srv2 = {"id":2,"nome":"intranet"}
srv3 = {"id":3,"nome":"backup"}

servicos.append(srv1)
servicos.append(srv2)
servicos.append(srv3)


servico = input("entre com o ID do servico a ser instalado: ")

for s in servicos:
    if s['id'] == servico:
        print "Instalando o servico %s"%s['nome']
        break
else:
    print "Servico nao encontrado"
