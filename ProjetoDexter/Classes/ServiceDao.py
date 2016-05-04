#!/usr/bin/python

from Classes.Service import Service as ServiceClass
from Classes.Client import Client as ClientClass
from Classes.Product import Product as ProductClass
from Models.Model import Service as ServiceTable,Client,Product, session

class ServiceDao:

    def __init__(self,service=""):
        self._service = service

    def get(self):
        try:
            service = session.query(ServiceTable,Client,Product).join(Client,Product).filter(ServiceTable.id==self._service._id).first()

            if service is None:
                return None
            else:
                c = ClientClass(service.Client.name,service.Client.cpf,service.Client.segment)
                c._id = service.Client.id

                p = ProductClass(service.Product.name,service.Product.description,service.Product.image)
                p._id = service.Product.id

                s = ServiceClass(service.Service.request_date,service.Service.cancel_date)
                s._id = service.Service.id
                s._client = c
                s._product = p

                return s
        except Exception as e:
            print "Deu erro: ",e
