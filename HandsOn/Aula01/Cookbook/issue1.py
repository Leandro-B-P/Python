#!/usr/bin/python

usuario = "arthur.dent"
password = "mochileiro"


login = raw_input("Digite o seu login de usuario: ")
senha = raw_input("Digite a sua senha: ")

if (login == usuario) and (senha == password):
    print "Usuario autenticado com sucesso!"
    print "Seja Bem Vindo %s "%login
else:
    print "Acesso Negado!"
