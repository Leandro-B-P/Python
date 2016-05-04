		devops = Groups()
		devops.nome = 'Devops'
		session.add(devops)
		infra = Groups()
		infra.nome = 'Infraestrutura'
		session.add(infra)
		dev = Groups()
		dev.nome = 'Desenvolvimento'
		session.add(dev)
		session.commit()
