#!/usr/bin/python

import os
import json
from Models.Model import session,Usuarios as UsuariosModel
from Servidores.Servidores import Servidores

class Usuarios:
    def __init__(self):
        pass

    def cadastrar_usuario(self): 
        try:
            usuario = {}
            usuario["nome"] = raw_input("Digite o nome do usuario: ")
            usuario["email"] = raw_input("Digite o email do usuario: ")
            usuario["senha"] = raw_input("Digite a senha do usuario: ")
            us = UsuariosModel(usuario["nome"],usuario["email"],usuario["senha"])
            session.add(us)
            session.commit()
            print "[!] Usuario cadastrado com sucesso!"
        except Exception as e:
            print "Falhou ao inserir no banco %s"%e
            session.rollback()

    def acessar_sistema(self):  
        try: 
            print "-= Sistema de Autenticao =-"
            login = raw_input("Digite o email do usuario: ")
            senha = raw_input("Digite a senha do usuario: ")
            res = session.query(UsuariosModel).filter(
                                                  UsuariosModel.email==login,
                                                  UsuariosModel.senha==senha
                                                ).first()
            if res is None:
                print "Falhou ao autenticar"
            else:
                print "Usuario Autenticado com Sucesso"
                servidor = Servidores()
                servidor.acessar_servidor(res.email)
                
        except Exception as e:
            print "Falhou ao buscar no banco de dados %s"%e


    def alterar_senha(self):
        try:
            print "-= Alteracao de Senha =-"
            login = raw_input("Digite o email do usuario: ")
            senha = raw_input("Digite a nova senha do usuario: ")
            res = session.query(UsuariosModel).filter(UsuariosModel.email==login).first()
            res.senha = senha
            print "Senha alterada com sucesso!"
            session.commit()
        except Exception as e:
            print "Falhou efetuar a alteracao %s"%e
            session.rollback()
