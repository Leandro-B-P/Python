#!/usr/bin/python

from paramiko.client import SSHClient
import paramiko
import sys


def executar_comando_remoto(com):
    hosts = ["192.168.0.2"]
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for h in hosts:
        try:
            ssh.connect(h)
            stdin,stdout,stderr = ssh.exec_command(com)
            if stderr.channel.recv_exit_status() != 0:
                print stderr.read()
            else:
                print stdout.read()
        except Exception as e:
            print "Nao conseguiu conectar ao servidor %s"%e
