#!/usr/bin/python

from paramiko.client import SSHClient
import paramiko

class SSHOps:
    def __init__(self):
        self.client = SSHClient()
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect("192.168.0.2")

    def runCommand(self,comando):
        stdin,stdout,stderr = self.client.exec_command(comando)
        if stderr.channel.recv_exit_status() != 0:
            return {"status":1,"message":stderr.read()}
        else:
            return {"status":0,"message":stdout.read()}
