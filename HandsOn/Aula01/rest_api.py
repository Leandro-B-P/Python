#!/usr/bin/python

import requests
import json

def listar_usuarios():
    response = json.loads(requests.get("http://0.0.0.0:5000/usuarios/").content)
    for r in response.get("usuarios"):
        print r.get("id"),r.get("nome")

def verificar_usuarios(email):
    response = json.loads(requests.get("http://0.0.0.0:5000/usuarios/").content)
    for r in response.get("usuarios"):
        if email == r.get("email"):
            return r.get("id")
    else:
         return False

def atualizar_usuario(uid):
    #Entrada dos novos dados do usuario
    nome = raw_input("Digite o nome do usuario: ")
    email = raw_input("Digite o novo email do usuario: ")
    #Colocando dados no dicionario
    dados = {"nome":nome,"email":email}
    #Convertendo dicionario em string
    dados = json.dumps(dados)
    #Setando headers
    cabecalho = {"Content-Type":"application/json"}
    #Enviando dados para o servidor
    response = requests.put("http://0.0.0.0:5000/usuarios/%s/"%uid,data=dados,headers=cabecalho)

    print response.content

def inserir_usuario():
    #Entrada de dados
    dados = {}
    dados["nome"] = raw_input("Digite o nome do usuario: ")
    dados["email"] = raw_input("Digite o email do usuario: ")
    #Setando cabecalho
    cabecalho = {"Content-Type":"application/json"}
    #Verificando a existencia de um usuario
    usuario = verificar_usuarios(dados.get("email"))
    #Se existe deletar
    if usuario:
    
        print "Usuario ja existe na base!"
        deletar_usuario(usuario)
    #Convertendo dicionario en String
        dados = json.dumps(dados)
    #Fazendo requisicao
    response = requests.post("http://0.0.0.0:5000/usuarios/",data=dados,headers=cabecalho)
    print response.content

def deletar_usuario(uid):
    response = requests.delete("http://0.0.0.0:5000/usuarios/%s/"%uid)
    print response.content
    

if __name__== "__main__":
    #verificar_usuarios()
    listar_usuarios()
    inserir_usuario()
    #uid = input("Digite o id do usuario: ")
    #deletar_usuario(uid)
    #atualizar_usuario(uid)
    
