#!/usr/bin/python

from Models.Model import session,Servidores
from MongoDB.MongoFunctions import registrar_logs

def cadastrar_servidor():
    try:
        servidor = {}
        servidor["endereco"] = raw_input("Digite o endereco de ip do servidor: ")
        servidor["nome"] = raw_input("Digite o nome desse servidor: ")
        servidor["administrador"] = raw_input("Digite o administrador: ")
        srv = Servidores(servidor["nome"],servidor['endereco'],servidor["administrador"])
        session.add(srv)
        session.commit()
        print "Cadastrado com sucesso!!!"
    except Exception as e:
        print "Falhou ao conectar com o banco %s"%e
        session.rollback()

def remover_servidor():
    try:
        srvs = session.query(Servidores).all()
        for s in srvs:
            print "%s - %s"%(s.id,s.nome)
        srv = input("Digite o numero do servidor que voce quer remover: ")
        srv_remove = session.query(Servidores).filter(Servidores.id==srv).first()
        session.delete(srv_remove)
        session.commit()
        print "Servidor removido com sucesso!"
    except Exception as e:
        print "Ocorreu um erro! %s"%e

def definir_administrador():
    try:
        srvs = session.query(Servidores).all()
        for s in srvs:
            print "%s - %s Administrador Atual[%s]"%(s.id,s.nome,s.administrator)
        srv = input("Digite o numero do servidor que voce quer definir o administrador: ")
        admin = raw_input("Digite o email do administrador desse servidor:")
        srv_alterado = session.query(Servidores).filter(Servidores.id==srv).first()
        srv_alterado.administrator = admin
        session.commit()
        print "Administrador definido com sucesso!"
    except Exception as e:
        print "Falhou! %s"%e
        session.rollback()

def acessar_servidor(login):
    try:
        srvs = session.query(Servidores).all()
        for s in srvs:
            print "%s - %s Administrador Atual[%s]"%(s.id,s.nome,s.administrator)
        srv = input("Digite o numero do servidor que voce quer acessar: ")
        servidor = session.query(Servidores).filter(Servidores.id==srv).first()
        registrar_logs(login,servidor.endereco_ip)
    except Exception as e:
        print "Erro! %s"%e
