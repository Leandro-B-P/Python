#!/usr/bin/python

import os
import json

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


