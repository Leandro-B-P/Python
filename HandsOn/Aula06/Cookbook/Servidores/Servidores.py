#!/usr/bin/python

import os
import json
import psycopg2

def cadastrar_servidor():
    try:
        con = psycopg2.connect("host=127.0.0.1 dbname=admssh user=dexter password=123456")
        cur = con.cursor()
        servidor = {}
        servidor["endereco"] = raw_input("Digite o endereco de ip do servidor: ")
        servidor["nome"] = raw_input("Digite o nome desse servidor: ")
        servidor["administrador"] = raw_input("Digite o administrador: ")
        cur.execute("insert into servidores(nome,endereco_ip,administrator)\
                     values('%s','%s','%s')"%(
                            servidor['nome'],servidor['endereco'],servidor['administrador'])
                   )
        con.commit()
        print "Cadastrado com sucesso!!!"
    except Exception as e:
        print "Falhou ao conectar com o banco %s"%e
        con.rollback()
    finally:
        cur.close()
        con.close()

 

def remover_servidor():
    try:
        con = psycopg2.connect("host=127.0.0.1 dbname=admssh user=dexter password=123456")
        cur = con.cursor()
        cur.execute("select * from servidores")
        for s in cur.fetchall():
            print "%s - %s"%(s[0],s[1])
        srv = input("Digite o numero do servidor que voce quer remover: ")
        cur.execute("delete from servidores where id=%s"%srv)
        con.commit()
        print "Servidor removido com sucesso!"
    finally:
        cur.close()
        con.close()

def definir_administrador():
    try:
        con = psycopg2.connect("host=127.0.0.1 dbname=admssh user=dexter password=123456")
        cur = con.cursor()
        cur.execute("select * from servidores")
        for s in cur.fetchall():
            print "%s - %s Administrador Atual[%s]"%(s[0],s[1],s[3])
        srv = input("Digite o numero do servidor que voce quer definir o administrador: ")
        admin = raw_input("Digite o email do administrador desse servidor:")
        cur.execute("update servidores set administrator='%s' where id=%s"%(admin,srv))
        con.commit()
        print "Administrador definido com sucesso!"
    except Exception as e:
        print "Falhou! %s"%e
    finally:
        cur.close()
        con.close()

