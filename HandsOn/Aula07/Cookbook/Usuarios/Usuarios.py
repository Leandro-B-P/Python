#!/usr/bin/python

import os
import json
from Models.Model import session,Usuarios

def cadastrar_usuario(): 
    try:
        usuario = {}
        usuario["nome"] = raw_input("Digite o nome do usuario: ")
        usuario["email"] = raw_input("Digite o email do usuario: ")
        usuario["senha"] = raw_input("Digite a senha do usuario: ")
        us = Usuarios(usuario["nome"],usuario["email"],usuario["senha"])
        session.add(us)
        session.commit()
        print "[!] Usuario cadastrado com sucesso!"
    except Exception as e:
        print "Falhou ao inserir no banco %s"%e
        session.rollback()

def acessar_sistema():  
    try: 
        print "-= Sistema de Autenticao =-"
        login = raw_input("Digite o email do usuario: ")
        senha = raw_input("Digite a senha do usuario: ")
        res = session.query(Usuarios).filter(
                                              Usuarios.email==login,
                                              Usuarios.senha==senha
                                            ).first()
        if res is None:
            print "Falhou ao autenticar"
        else:
            print "Usuario Autenticado com Sucesso"
    except Exception as e:
        print "Falhou ao buscar no banco de dados %s"%e


def alterar_senha():
    try:
        print "-= Alteracao de Senha =-"
        login = raw_input("Digite o email do usuario: ")
        senha = raw_input("Digite a nova senha do usuario: ")
        res = session.query(Usuarios).filter(Usuarios.email==login).first()
        res.senha = senha
        print "Senha alterada com sucesso!"
        session.commit()
    except Exception as e:
        print "Falhou efetuar a alteracao %s"%e
        session.rollback()
