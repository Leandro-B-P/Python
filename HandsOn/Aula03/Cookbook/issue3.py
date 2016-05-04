#!/usr/bin/python

import json
import os
import sys

def cadastrar_usuario(): 
    usuarios = []   
    if not os.stat("banco.json").st_size == 0:
        with open("banco.json","r") as f:
            dicionario_usuarios = json.load(f)
        usuarios = dicionario_usuarios["usuarios"]
        dicionario_usuarios["usuarios"] = usuarios
    else:
        dicionario_usuarios = {"usuarios":usuarios}

    usuario = {"login":"","senha":""}
    usuario["login"] = raw_input("Digite o login do usuario: ")
    usuario["senha"] = raw_input("Digite a senha do usuario: ")
    usuarios.append(usuario)

    try:
        with open("banco.json","w") as f:
            json.dump(dicionario_usuarios,f)
    except Exception as e:
        print "Falhou ao escrever no arquivo %s"%e

def acessar_sistema():
    if not os.stat("banco.json").st_size == 0:
            with open("banco.json","r") as f:
                dicionario_usuarios = json.load(f)

    print "-= Sistema de Autenticao =-"
    login = raw_input("Digite o login do usuario: ")
    senha = raw_input("Digite a senha do usuario: ")
    
    for u in dicionario_usuarios["usuarios"]:
        if u["login"] == login and u["senha"] == senha:
            print "Usuario Autenticado com Sucesso"
            break        
    else:
        print "Usuario nao encontrado"   

def sair_sistema():
    print "Saindo do sistema..."
    sys.exit()

def menu():
    try:
        print "\
               1 - Cadastrar Usuario\n\
               2 - Acessar Sistema\n\
               3 - Sair do Sistema\n"
        opcao = input("Digite a opcao desejada: ")
        return opcao
    except Exception as e:
        print "Erro: %s"%e
        return 3

def switch(x):
    try:
        dict_options = {1:cadastrar_usuario,2:acessar_sistema,3:sair_sistema}
        dict_options[x]()
    except Exception as e:
        print "Opcao invalida"

if __name__ == '__main__':   
    while True:
        switch(menu())

    
