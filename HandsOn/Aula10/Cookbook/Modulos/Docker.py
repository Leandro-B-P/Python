#!/usr/bin/python

from Modulos.SSH import SSH
import json

class Docker(SSH):
    def __init__(self):
        self.image = "webservercloud"
        SSH.__init__(self)

    def criarContainer(self,nome):
        comando = "docker run -tdi --name %s --hostname %s %s /bin/bash"%(nome,nome,self.image)
        self.executarComandoRemoto(comando)

    def pegarIPContainer(self,nome):
        comando = "docker inspect %s"%nome
        srv = json.loads(self.executarComandoRemoto(comando))
        return srv[0]['NetworkSettings']['Networks']['bridge']['IPAddress']

    def acessarContainer(self,nome,comando):
        com = "docker exec %s /bin/bash -c '%s'"%(nome,comando)
        return self.executarComandoRemoto(com)

    def removerContainer(self,nome):
        return "docker stop %s && docker rm %s"%(nome,nome)
