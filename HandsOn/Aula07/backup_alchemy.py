#!/usr/bin/python
#
#Alchemy
#
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

engine = create_engine("postgresql://python:4linux@localhost/loja")
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


Base = declarative_base()



class Users(Base):
	__tablename__='users'
	id = Column(Integer,primary_key=True)
	nome = Column(String)
	descricao = Column(Text)
	senha = Column(String)
	servers = relationship("Servers")

class Servers(Base):
	__tablename__='servers'
	id = Column(Integer,primary_key=True)
	nome = Column(String)
	descricao = Column(Text)
	user_id = Column(Integer,ForeignKey("users.id"))

if __name__=='__main__':
	try:
		Base.metadata.create_all(engine)
		dns = Servers()
		dns.nome = "Bacula"
		dns.descricao = "Servidor Bacula"
		session.add(dns)
		session.commit()
		print " Servidor cadastrado com sucesso!"
		todos = session.query(Servers).all()
		for s in  todos:
			print s.id,"-",s.nome

	
	except Exception as e:
		session.rollback()
		print "Falhou ao criar o banco",e
