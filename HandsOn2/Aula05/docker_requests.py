#!/usr/bin/python

from docker import Client

class DockerAPI:
    def __init__(self):

        self.docker_client = Client("tcp://192.168.201.124:2376")

    def  list_Container(self):
         for c in self.docker_client.containers(all=True):
            print c.get("Names")

    def create_container(self,nome,imagem):
        res = self.docker_client.create_container(name=nome,image=imagem)
        if res:
            return res

        else:
            print " Falhou ao criar o container ",res

    def start_container(self,id):
        try:
            self.docker_clientt.start(container=id)
            print "Container executado"
        except Exception as e:
            print " Falhou ao iniciar o container ",e        

if __name__=='__main__':

    da = DockerAPI()
    da.create_container("LEANDRO","ubuntu")
    da.start_container(container_id)
    da.list_Container()
