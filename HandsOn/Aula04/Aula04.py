#!/usrbin/python

from modulos.SSHModulo import executar_comando as executar_ssh
from modulos.ValidacaoModulo import validar_token


if validar_token():

	executar_ssh("localhost","4linux")	

else:
	print "Seu token expirou"

