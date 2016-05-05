#!/usr/bin/python


from paramiko import SSHClient
import paramiko

class SSH:
    def __init__(self):
		
        self.client = SSHClient()
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname="192.168.0.2",
                            username="forlinux",
                            password="4linux")


    def exec_command(self,cmd):
        stdin,stdout,stderr = self.client.exec_command(cmd)
        if stderr.channel.recv_exit_status() != 0:
            return stderr.read()
        else:
            return stdout.read()

if __name__=='__main__':
    rhost = SSH()
    print rhost.exec_command("cat /etc/hostname")
