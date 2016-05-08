#!/usr/bin/python

from paramiko.client import SSHClient
import paramiko
import ConfigParser

class SshOps:
    def __init__(self):
        self.client = SSHClient()
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        config = ConfigParser.ConfigParser()
        config.read("/home/forlinux/www/4803-Python/ProjetoDexter/config.cfg")
        self.client.connect(config.get("docker","address"))

    def runCommand(self,command):
        stdin,stdout,stderr = self.client.exec_command(command)
        if stderr.channel.recv_exit_status() != 0:
            return {"status":1,"message":stderr.read()}
        else:
            return {"status":0,"message":stdout.read()}
