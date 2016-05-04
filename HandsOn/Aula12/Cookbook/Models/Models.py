#!/usr/bin/python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("postgresql://dexter:123456@127.0.0.1/dexterops")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Client(Base):
    __tablename__ = "client"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    cpf = Column(String)
    segment = Column(String)
    services = relationship("Service")

    def __init__(self,name="",cpf="",segment=""):
        self.name = name
        self.cpf = cpf
        self.segment = segment
    

class Product(Base):
    __tablename__ = "product"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    description = Column(String)
    image = Column(String)
    
    def __init__(self,name="",description="",image=""):
        self.name = name
        self.description = description
        self.image = image

class Service(Base):
    __tablename__ = "service"
    id = Column(Integer,primary_key=True)
    client_id = Column(Integer,ForeignKey('client.id'))
    produto_id = Column(Integer,ForeignKey('product.id'))
    request_date = Column(String)
    cancel_date = Column(String)
    client = relationship("Client")
    product = relationship("Product")

    def __init__(self,rd="",cd=""):
        self.request_date = rd
        self.cancel_date = cd

if __name__ == '__main__':
    try:
        Base.metadata.create_all(engine)
        dexter = session.query(Client).filter(Client.id==1).first()
        intranet = Product("Intranet","Container com a imagem do servico de Intranet","intranet")
        session.add(intranet)
        servico = Service("21/02/2016","")
        servico.product = intranet
        session.add(servico)
        dexter.services.append(servico)
        session.commit()
    except Exception as e:
        print "Erro: %s"%e
        session.rollback()


