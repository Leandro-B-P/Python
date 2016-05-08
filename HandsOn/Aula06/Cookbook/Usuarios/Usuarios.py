#!/usr/bin/python

import os
import json
import psycopg2

def cadastrar_usuario(): 
    try:
        con = psycopg2.connect("host=127.0.0.1 dbname=admssh user=dexter password=123456")
        cur = con.cursor()
        usuario = {}
        usuario["nome"] = raw_input("Digite o nome do usuario: ")
        usuario["login"] = raw_input("Digite o email do usuario: ")
        usuario["senha"] = raw_input("Digite a senha do usuario: ")
        cur.execute("insert into usuarios(nome,email,senha) \
                     values('%s','%s','%s')"%(
                                              usuario["nome"],
                                              usuario["login"],
                                              usuario["senha"]
                                            )
                   )
        con.commit()
        print "[!] Usuario cadastrado com sucesso!"
    except Exception as e:
        print "Falhou ao inserir no banco %s"%e
        con.rollback()
    finally:
        cur.close()
        con.close()

def acessar_sistema():  
    try:
        con = psycopg2.connect("host=127.0.0.1 dbname=admssh user=dexter password=123456")
        cur = con.cursor() 
        print "-= Sistema de Autenticao =-"
        login = raw_input("Digite o email do usuario: ")
        senha = raw_input("Digite a senha do usuario: ")
        cur.execute("select * from usuarios where email='%s' and senha='%s'"%(login,senha))    
        if cur.fetchone() is None:
            print "Falhou ao autenticar"
        else:
            print "Usuario Autenticado com Sucesso"
    except Exception as e:
        print "Falhou ao buscar no banco de dados %s"%e
    finally:
        cur.close()
        con.close()


def alterar_senha():
    try:
        con = psycopg2.connect("host=127.0.0.1 dbname=admssh user=dexter password=123456")
        cur = con.cursor() 
        print "-= Alteracao de Senha =-"
        login = raw_input("Digite o email do usuario: ")
        senha = raw_input("Digite a nova senha do usuario: ")
        cur.execute("update usuarios set senha='%s' where email='%s'"%(senha,login))    
        con.commit()
        print "Senha alterada com sucesso!"
    except Exception as e:
        print "Falhou efetuar a alteracao %s"%e
    finally:
        cur.close()
        con.close()
