#!/usr/bin/python

from Models.Model import session,Servidores as ServidoresModel
from MongoDB.MongoFunctions import MongoFunctions
from Modulos.Docker import Docker
from Modulos.SSH import SSH

import json

class Servidores:
    def __init__(self):
        pass

    def cadastrar_servidor(self):
        try:
            servidor = {}
            servidor["nome"] = raw_input("Digite o nome desse servidor: ")
            servidor["administrador"] = raw_input("Digite o administrador: ")
            ssh = SSH()
            docker = Docker()
            ssh.executarComandoRemoto(docker.criarContainer(servidor['nome']))
            srv = json.loads(ssh.executarComandoRemoto(docker.pegarIPContainer(servidor['nome'])))
            servidor["endereco"] = srv[0]['NetworkSettings']['Networks']['bridge']['IPAddress']
            srv = ServidoresModel(servidor["nome"],servidor['endereco'],servidor["administrador"])
            session.add(srv)
            session.commit()
            print "Cadastrado com sucesso!!!"
        except Exception as e:
            print "Falhou ao conectar com o banco %s"%e
            session.rollback()

    def remover_servidor(self):
        try:
            srvs = session.query(ServidoresModel).all()
            for s in srvs:
                print "%s - %s"%(s.id,s.nome)
            srv = input("Digite o numero do servidor que voce quer remover: ")
            srv_remove = session.query(ServidoresModel).filter(ServidoresModel.id==srv).first()
            session.delete(srv_remove)
            session.commit()
            print "Servidor removido com sucesso!"
        except Exception as e:
            print "Ocorreu um erro! %s"%e

    def definir_administrador(self):
        try:
            srvs = session.query(ServidoresModel).all()
            for s in srvs:
                print "%s - %s Administrador Atual[%s]"%(s.id,s.nome,s.administrator)
            srv = input("Digite o numero do servidor que voce quer definir o administrador: ")
            admin = raw_input("Digite o email do administrador desse servidor:")
            srv_alterado = session.query(ServidoresModel).filter(ServidoresModel.id==srv).first()
            srv_alterado.administrator = admin
            session.commit()
            print "Administrador definido com sucesso!"
        except Exception as e:
            print "Falhou! %s"%e
            session.rollback()

    def acessar_servidor(self,login):
        try:
            srvs = session.query(ServidoresModel).all()
            for s in srvs:
                print "%s - %s Administrador Atual[%s]"%(s.id,s.nome,s.administrator)
            srv = input("Digite o numero do servidor que voce quer acessar: ")
            servidor = session.query(ServidoresModel).filter(ServidoresModel.id==srv).first()
            mf = MongoFunctions()
            mf.registrar_logs(login,servidor.endereco_ip)

            docker = Docker()
            ssh = SSH()
            print "Para sair digite exit"
            while True:
                comando = raw_input("root@%s # "%servidor.nome)
                print ssh.executarComandoRemoto(docker.acessarContainer(servidor.nome,comando))
                if comando == "exit":
                    break
        except Exception as e:
            print "Erro! %s"%e
