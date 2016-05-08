#!/usrbin/python

from paramiko.client import SSHClient
import paramiko
import sys

def executar_comando(servidor,senha):	
	ssh = SSHClient()
	ssh.load_system_host_keys()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


	try:
		ssh.connect("localhost",username="forlinux",password=senha)
		stdin, stdout, stderr = ssh.exec_command("ls -la")	
		if stderr.channel_recv_exit_status() != 0:
			print stderr.read()
		else:
			print stdout.read()

	except Exception as e:
			
		print "A conexao falhou"


if __name__ == '__main__':

	print "Executando em linha de comando"
