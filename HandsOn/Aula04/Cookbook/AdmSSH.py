#!/usr/bin/python

from Usuarios.Usuarios import cadastrar_usuario, acessar_sistema
from Servidores.Servidores import cadastrar_servidor,remover_servidor,definir_administrador
import sys


def sair_sistema():
    print "Saindo do sistema..."
    sys.exit()

def menu():
    try:
        print "\
               1 - Cadastrar Usuario\n\
               2 - Acessar Sistema\n\
               3 - Cadastrar Servidor\n\
               4 - Remover Servidor\n\
               5 - Definir Administrador\n\
               6 - Sair do Sistema"
        opcao = input("Digite a opcao desejada: ")
        return opcao
    except Exception as e:
        print "Erro: %s"%e
        return 3

def switch(x):
    try:
        dict_options = {
                        1:cadastrar_usuario,
                        2:acessar_sistema,
                        3:cadastrar_servidor,
                        4:remover_servidor,
                        5:definir_administrador,
                        6:sair_sistema,
                       }
        dict_options[x]()
    except Exception as e:
        print "Opcao invalida %s"%e

if __name__ == '__main__':   
    while True:
        switch(menu())
