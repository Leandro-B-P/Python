#!/usr/bin/python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("sqlite:///banco.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Client(Base):
    __tablename__ = "client"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    cpf = Column(String)
    segment = Column(String)
    services = relationship("service")
    

class Product(Base):
    __tablename__ = "product"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    description = Column(String)
    image = Column(String)

class Service(Base):
    __tablename__ = "service"
    id = Column(Integer,primary_key=True)
    client_id = Column(Integer,ForeignKey('client.id'))
    produto_id = Column(Integer,ForeignKey('product.id'))
    request_data = Column(Date)
    cancel_date = Column(Date)
    client = relationship("client")
    product = relationship("product")

if __name__ == '__main__':
    Base.metadata.create_all(engine)
