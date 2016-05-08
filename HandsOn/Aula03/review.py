#!/usr/bin/python


celulares = ["lg","sansung","apple"]

produtos = {"celulares":[]}


produtos["celulares"]= celulares


for celular in celulares:
    dicionario = {}
    dicionario["marca"] = celular
    produtos["celulares"].append(dicionario)


print produtos
