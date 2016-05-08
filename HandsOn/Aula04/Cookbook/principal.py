#!/usr/bin/python

from Pacote.ssh import executar_comando_remoto as exec_command
import token

token.validar_token()
exec_command("cat /etc/hostname")
