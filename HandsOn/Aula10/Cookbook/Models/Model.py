#!/usr/bin/python

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey,Table
from sqlalchemy.orm import sessionmaker,relationship,Session

engine = create_engine("postgresql://dexter:123456@127.0.0.1/admssh")
Session = sessionmaker()
Session.configure(bind=engine)

session = Session()

Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer,primary_key=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)

    def __init__(self,nome="",email="",senha=""):
        self.nome = nome
        self.email = email
        self.senha = senha

class Servidores(Base):
    __tablename__ = 'servidores'
    id = Column(Integer,primary_key=True)
    nome = Column(String)
    endereco_ip = Column(String)
    administrator = Column(String)

    def __init__(self,nome="",endereco="",administrator=""):
        self.nome = nome
        self.endereco_ip = endereco
        self.administrator = administrator


if __name__ == '__main__':
    try:  
        Base.metadata.create_all(engine)
    except Exception as e:
        print "Erro: %s"%e
