		todos = session.query(Servers).all()
		for s in todos:
			print s.id,"-",s.nome,"-",s.user_id
		adms = session.query(Users).all()
		for a in adms:
			print a.id,"-",a.nome
		
 		leandro = session.query(Users).filter(Users.id==3).first()
		apache = session.query(Servers).filter(Servers.id==5).first()
		leandro.servers.append(apache)
		session.commit()
		adms = session.query(Users,Servers).join(Servers).all()
		for a in adms:
			print a.Users.nome,"administra",a.Servers.nome
			
			
