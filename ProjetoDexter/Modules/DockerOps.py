#!/usr/bin/python

from Modules.SshOps import SshOps

class DockerOps:
    
    def __init__(self):
        pass

    def createContainer(self,id,image):
        command = "docker run -d -ti --name %s %s"%("%s_%s"%(image,id),'webservercloud')
        ssh = SshOps()
        res = ssh.runCommand(command)
        if res['status'] == 1:
            print res['message']
        else:
            command = "docker exec %s bash /opt/4linux/makeclass.sh %s"%(id,image)
            res = ssh.runCommand(command)
    
    def removeContainer(self,id,image):
        command = "docker stop %s"%("%s_%s"%(image,id))
        ssh = SshOps()
        res = ssh.runCommand(command)
        if res['status'] == 1:
            print res['message']
        
        command = "docker rm %s"%("%s_%s"%(image,id))
        res = ssh.runCommand(command)
        if res['status'] == 1:
            print res['message']
        else:
            print res['message']
