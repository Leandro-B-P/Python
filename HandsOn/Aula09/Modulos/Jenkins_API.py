#!/usr/bin/python

import jenkins
from lxml import etree
import yaml
import ConfigParser

class JenkinsAPI:
    def __init__(self):
        try:
            config = ConfigParser.ConfigParser()
            config.read("deploy.cfg")
            self.server = jenkins.Jenkins("http://%s:8080"%config.get("jenkins","server"))
            self.server.get_version()
        except Exception as e:
            print "Falhou ao conectar com o servidor: ",e
    
    def create_job(self,nome,repo,steps):
        try:
            xml = self._generate_jobs_steps(repo,steps)
            self.server.create_job(nome,xml)
            print "Job criada com sucesso"
        except Exception as e:
            print "Falhou ao criar job: ",e

    def _generate_jobs_steps(self,repo,steps):
        #Lendo arquivo XML
        with open("Templates/base.xml") as f:
            base_xml = f.read().replace("REPO_TESTE",str(repo))
        #Convertendo em objeto do ElementTree
        base_xml = etree.XML(base_xml)
        #procura por elemento builders dentro do XML
        for element in base_xml.findall("builders"):
            builders = element
        #pega a lista de comands do arquivo yaml e gera o xml
        apaga_dir = "rm -rf /var/www/html"
        git_clone = "git clone %s /var/www/html/"%repo
        steps.append(apaga_dir)
        steps.append(git_clone)
        for c in steps:
            #cria step do tipo Shell
            step = etree.Element("hudson.tasks.Shell")
            #cria comando do step do Jenkins
            command = etree.Element("command")
            #adiciona o comando do arquivo yaml dentro da tag command do xml
            command.text = 'ssh forlinux@192.168.201.124 "%s"'%c
            #adiciona o elemento command como filho do elemento hudson.taks.Shell
            step.append(command)
            #adiciona o elemento hudson.taks.Shell como filho do elemento builders
            builders.append(step)
        return etree.tostring(base_xml)

    def execute_job(self,nome):
        try:
            self.server.build_job(nome)
            print "Job executada com sucesso"
        except Exception as e:
            print "Falhou ao executar job ",e

if __name__ == '__main__':
    j = JenkinsAPI()
    #j.create_job("LeandroJobs")
    j.execute_job("JobAPT")
    #j.generate_job_steps()    
