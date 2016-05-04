#!/usr/bin/python

from pymongo import MongoClient
from random import randint
import ConfigParser
import os
import sys

class MongoOps:
    _db = ""

    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read("/var/www/4803-Python/ProjetoDexter/config.cfg")
        self._client = MongoClient(config.get("mongodb","address"))
        self._db = self._client[config.get("mongodb","base")]

    def getQueue(self):
        queue = self._db.queue.find({})
        return queue

    def getServiceToRemove(self):
        return self._db.queue.find({"status":1})
            
    def getServiceToInstall(self):
        return self._db.queue.find({"status":0})

    def populate(self):
        for i in range(0,11):
            self._db.queue.insert({"_id":i,"status":randint(0,3)})

if __name__ == "__main__":
    m = MongoOps()
    print m.getQueue().count()
