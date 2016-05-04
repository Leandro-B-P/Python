#!/usr/bin/python


import psycopg2


def conecta_banco():
	try:
		conexao = psycopg2.connect("host=localhost dbname=loja \
									user=python password=4linux")
		return conexao
	
	except Exception as e:

		print "\nA conexao com o banco falhou: ",e
		raise

def cadastrar_usuario(login,senha):
	try:
		conexao = conecta_banco()
		cur = conexao.cursor()
		cur.execute("insert into usuarios(login,senha) \
						values('%s','%s')"%(login,senha))

		conexao.commit()
	except Exception as e:
	
		print "\nFalha ao cadastrar usuario: ",e
		conexao.rollback()
		
	finally:

		cur.close()
		conexao.close()


def listar_usuarios():

	try:
		conexao = conecta_banco()
		cur = conexao.cursor()
		cur.execute("select * from usuarios")

		for r in cur.fetchall():
			print r

	except Exception as e:

		print "Falhou em listar os usuarios: ",e
	
	finally:

		cur.close()
		conexao.close()

def buscar_usuario(login):

	try:
		conexao = conecta_banco()
		cur = conexao.cursor()
		cur.execute("select * from usuarios where login = '%s'"%login)
		result = cur.fetchall()
		if result:
			return result
		else:
			print "Usuario nao encontrado"
	except Exception as e:
		print "Falha os buscar usuario",e

def deletar_usuario(usuario_id):

	try:
		conexao = conecta_banco()
		cur = conexao.cursor()
		cur.execute("select id from usuarios where id=%s"%usuario_id)
		if not cur.fetchall():
			print "Voce digitou um id invalido!"
			return
		cur.execute("delete from usuarios where id=%s"%usuario_id)
		conexao.commit()
		
	except Exception as e:
		print "Falha os buscar usuario",e

		conexao.rollback()
	finally:
			
			cur.close()
			conexao.close()
		
