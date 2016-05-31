#!/usr/bin/python

import jenkins
from lxml import etree
import yaml

class JenkinsAPI:
    def __init__(self):
        try:
            self.server = jenkins.Jenkins("http://192.168.201.127:8080")
            print self.server.get_version()
        except Exception as e:
            print "Falhou ao conectar com o servidor: ",e
    
    def create_job(self,nome):
        try:
            xml = self._generate_jobs_steps()
            self.server.create_job(nome,xml)
            print "Job criada com sucesso"
        except Exception as e:
            print "Falhou ao criar job: ",e

    def _generate_jobs_steps(self):
        #Lendo arquivo XML
        with open("Templates/base.xml") as f:
            base_xml = f.read()
        #Convertendo em objeto do ElementTree
        base_xml = etree.XML(base_xml)
        #procura por elemento builders dentro do XML
        for element in base_xml.findall("builders"):
            builders = element
        #Le o arquivo no formato yaml
        with open("deploy_wordpress.yml","r") as f:
            arquivo_yaml = yaml.load(f.read())
        #pega a lista de comands do arquivo yaml e gera o xml
        for c in arquivo_yaml.get("command"):
            #cria step do tipo Shell
            step = etree.Element("hudson.tasks.Shell")
            #cria comando do step do Jenkins
            command = etree.Element("command")
            #adiciona o comando do arquivo yaml dentro da tag command do xml
            command.text = c
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
