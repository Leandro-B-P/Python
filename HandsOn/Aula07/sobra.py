""" 		new_user = Users()
		new_user.nome = 'Leandro'
		new_user.descricao = 'Aluno do curso de python'
		new_user.senha = '12345'
		session.add(new_user)
		session.commit()
		all_users = session.query(Users).all()
		for user in all_users:
			print user.id,"-",user.nome
		
		usuario = session.query(Users).filter(Users.id==1).first()
		usuario.nome = "Vitor"
		session.commit()
		
		test = session.query(Users).filter(Users.id==1).first()
		if test:
			print "Usuario nao existe!"
		session.delete(test)
		session.commit()
	"""	
