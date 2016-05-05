#!/usr/bin/python

from Usuarios.Usuarios import Usuarios #cadastrar_usuario, acessar_sistema, alterar_senha
from Servidores.Servidores import Servidores #cadastrar_servidor,remover_servidor,definir_administrador
from MongoDB.MongoFunctions import MongoFunctions #listar_ultimos_acessos
import sys


def sair_sistema():
    print "Saindo do sistema..."
    sys.exit()

def menu():
    try:
        mf = MongoFunctions()
        mf.listar_ultimos_acessos()
        print "\
               1 - Cadastrar Usuario\n\
               2 - Acessar Sistema\n\
               3 - Cadastrar Servidor\n\
               4 - Remover Servidor\n\
               5 - Definir Administrador\n\
               6 - Alterar Senha\n\
               7 - Sair do Sistema"
        opcao = input("Digite a opcao desejada: ")
        return opcao
    except Exception as e:
        print "Erro: %s"%e
        return 3

def switch(x):
    try:
        srv = Servidores()
        usr = Usuarios()
        dict_options = {
                        1:usr.cadastrar_usuario,
                        2:usr.acessar_sistema,
                        3:srv.cadastrar_servidor,
                        4:srv.remover_servidor,
                        5:srv.definir_administrador,
                        6:usr.alterar_senha,
                        7:sair_sistema,
                       }
        dict_options[x]()
    except Exception as e:
        print "Opcao invalida %s"%e

if __name__ == '__main__':   
    while True:
        switch(menu())
