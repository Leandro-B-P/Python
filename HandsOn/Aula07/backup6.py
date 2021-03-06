#!/usr/bin/python
#
#Alchemy
#
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import datetime
import random

engine = create_engine("postgresql://python:4linux@localhost/loja")
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
Base = declarative_base()


usuarios_grupos = Table('usuarios_grupos',
	Base.metadata,
	Column('users_id',Integer,ForeignKey('users.id')),	
	Column('groups_id',Integer,ForeignKey('groups.id')),
)


class Users(Base):
	__tablename__='users'
	id = Column(Integer,primary_key=True)
	nome = Column(String)
	descricao = Column(Text)
	senha = Column(String)
	servers = relationship("Servers")
	groups = relationship("Groups",secondary=usuarios_grupos)
	tokens =  relationship("Tokens")

class Servers(Base):
	__tablename__='servers'
	id = Column(Integer,primary_key=True)
	nome = Column(String)
	descricao = Column(Text)
	user_id = Column(Integer,ForeignKey("users.id"))

class Groups(Base):
	__tablename__='groups'
	id = Column(Integer,primary_key=True)
	nome = Column(String)
	
class Tokens(Base):
	__tablename__='tokens'
	id = Column(Integer,primary_key=True)
	nome = Column(String)
	user_id = Column(Integer,ForeignKey("users.id"))
	server_id = Column(Integer,ForeignKey("servers.id"))
	token =Column(String)
	date_request = Column(DateTime,default=datetime.now())
	servers = relationship("Servers")
	users = relationship("Users")

if __name__=='__main__':
	try:
		Base.metadata.create_all(engine)
		token = Tokens()
		token.token = str(random.randint(100000,999999))
		servidor = session.query(Servers).filter(Servers.id==1).first()
		token.server = servidor
		usuario = session.query(Users).filter(Users.id==2).first()
		usuario.tokens.append(token)
		session.add(token)
		session.commit()

	except Exception as e:
		session.rollback()
		print "Falhou ao criar o banco",e
