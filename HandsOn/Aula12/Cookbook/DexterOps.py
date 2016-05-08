#!/usr/bin/python

from Modulos.MongoOps import MongoOps
from Modulos.ProvisionOps import ProvisionOps

def Start():
    mongo = MongoOps()
    print "Existem %s servicos na fila"%(mongo.getQueue().count())
    for service in mongo.getServiceToInstall():
        prov = ProvisionOps(service["_id"])
        prov.installService()


if __name__ == '__main__':
    Start()
