#!/usr/bin/python


class Docker:
    def __init__(self):
        self.image = "webservercloud"

    def criarContainer(self,nome):
        return "docker run -tdi --name %s --hostname %s %s /bin/bash"%(nome,nome,self.image)

    def pegarIPContainer(self,nome):
        return "docker inspect %s"%nome

    def acessarContainer(self,nome,comando):
        return "docker exec %s /bin/bash -c '%s'"%(nome,comando)

    def removerContainer(self,nome):
        return "docker stop %s && docker rm %s"%(nome,nome)
