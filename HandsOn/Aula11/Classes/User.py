#!/usr/bin/python


from Models.Model import session, Users as UserModel


class User:

	def __init__(self,login="",senha=""):
		self.login = login
		self.senha = senha

	def save(self):
		try:
			u = UserModel(self)
			session.add(u)
			session.commit()
			print "\nUsuario Cadastrado com sucesso\n!"

		except Exception as e:
			session.rollback()

			print "Falhou ao salvar o usuario!",e

	def listAll(self):
		try:
			all_users = session.query(UserModel).all()
			return all_users

		except Exception as e:

			print "Falhou ao listar o usuario!",e


	def get(self,login):
		
		try:
			user = session.query(UserModel)\
						  .filter(UserModel.nome==login)\
						  .first()
			if user:
				self.nome = user.nome
				self.senha = user.senha
				return self

			else:

				return None

		except Exception as e:

			print "Falhou ao buscar o usuario!",e


	def remove(self):
		try:
			user = session.query(UserModel)\
						  .filter(UserModel.nome==self.nome)\
						  .first()

			session.delete(user)
			session.commit()
			print "\nUsuario deletado com sucesso!\n"
		except Exception as e:
		
			session.rollback()

			print "Falhou ao remover",e

		
