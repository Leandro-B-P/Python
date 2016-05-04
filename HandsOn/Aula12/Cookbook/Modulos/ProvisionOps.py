#!/usr/bin/python

from Classes.Service import Service as ServiceClass
from Classes.ServiceDAO import ServiceDAO
from Modulos.DockerOps import DockerOps


class ProvisionOps:
    def __init__(self,id):
        self.id = id

    def installService(self):
        try:
            service = ServiceClass()
            service.id = self.id
            servicedao = ServiceDAO(service)
            service = servicedao.get()
            print "ID: %s Data de Contratacao: %s"%(service.id,service.request_date)
            print "Instalando o servico para o client: %s"%service.client.name
            print "Servico a ser instalado: %s"%service.product.name
            docker = DockerOps()
            res = docker.createContainer(service.id,service.product.image)
            print "Servico instalado com sucesso"
        except Exception as e:
            print "Ocorreu um erro: %s"%e

        
