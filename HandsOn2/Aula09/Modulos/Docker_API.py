#!/usr/bin/python

from docker import Client
import ConfigParser
from Modulos.SSHAPI import SSHAPI
import json

class DockerAPI(SSHAPI):
    def __init__(self):
        try:
            SSHAPI.__init__(self)
            config = ConfigParser.ConfigParser()
            config.read("deploy.cfg")
            self.docker_client = Client("tcp://%s:2376"%config.get("docker","server"))
        except Exception as e:
            print "Falhou ao conectar com Docker:",e

    def  list_Container(self):
         for c in self.docker_client.containers(all=True):
            print c.get("Names")

    def create_container(self,nome,imagem="ubuntu"):
        res = self.docker_client.create_container(name=nome,image=imagem,
                                                  command="/bin/bash",
                                                  tty=True,
                                                  stdin_open=True,
                                                  detach=True)
        if res:
            return res

        else:
            print " Falhou ao criar o container ",res

    def start_container(self,id):
        try:
            self.docker_client.start(container=id)
            print "Container executado"
        except Exception as e:
            print " Falhou ao iniciar o container ",e

    def get_container(self,nome):
        try:
            todos = self.docker_client.containers(all=True)
          
            nome = "/"+nome
            
            container = [ c for c in todos if nome in c.get("Names") ][0]
            return container
        except Exception as e:
            print " Falhou ao buscar container",e

    def _exec(self,container,cmd):
        c = "docker exec %s %s "%(container,cmd)
        self.exec_ssh_command(c)

    def get_container_address(self,nome):
        address = self.get_container(nome)
        address = address.get("NetworkSettings")\
                         .get("Networks").get("bridge")\
                         .get("IPAddress")
        return address       

if __name__=='__main__':

    da = DockerAPI()
    da.create_container("LEANDRO","ubuntu")
    da.start_container(container_id)
    da.list_Container()
    da.get_container_address()
