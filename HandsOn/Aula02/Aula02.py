#!/usr/bin/python


usuario = "leandro.pereira"
password = "1234"

print "\t1 - Para cadastrar usuarioss \n \
	2 - Para listar todos os usuarios \n \
	3 - Para deletar um usuario \n\
        4 - Para autenticar um usuario "


opcao = input("\nDigite  a opcao deseja :")

if opcao == 1:

    print "Cadastrar usuarios selecionado"

elif opcao == 2:

    print "Listar usuarios selecionado"

elif opcao == 3:

    print "Deletar usuarios selecionados"

elif opcao == 4:

    nome = raw_input("Digite o login: ")
    senha = raw_input("Digite senha: ")
    
    if nome == usuario and senha == password:
    
        print "Seja bem vindo",nome

    else:
        print "Acesso negado!"


