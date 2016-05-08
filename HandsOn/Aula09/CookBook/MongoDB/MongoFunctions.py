#!/usr/bin/python 

from pymongo import MongoClient
from datetime import datetime

class MongoFunctions:
    def __init__(self):
        self.client = MongoClient("127.0.0.1")
        self.db = self.client["AdmSSH"]
   
    def registrar_logs(self,login,ip):
        try:            
            self.db.logs.insert({"administrador":login,"servidor":ip,"data":datetime.now()})
        except Exception as e:
            print "Falhou %s"%e

    def listar_ultimos_acessos(self):
        try:
            for l in self.db.logs.find({}).limit(5):
                print l["administrador"]," - ",l['servidor']," - ",l["data"]
        except Exception as e:
            print "Falhou %s"%e
