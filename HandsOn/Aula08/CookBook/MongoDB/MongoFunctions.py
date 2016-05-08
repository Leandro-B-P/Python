#!/usr/bin/python 

from pymongo import MongoClient
from datetime import datetime

def registrar_logs(login,ip):
    try:
        client = MongoClient("127.0.0.1")
        db = client["AdmSSH"]
        db.logs.insert({"administrador":login,"servidor":ip,"data":datetime.now()})
    except Exception as e:
        print "Falhou %s"%e

def listar_ultimos_acessos():
    try:
        client = MongoClient("127.0.0.1")
        db = client["AdmSSH"]
        for l in db.logs.find({}).limit(5):
            print l["administrador"]," - ",l['servidor']," - ",l["data"]
    except Exception as e:
        print "Falhou %s"%e
