#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: Leandro Batista
# e-mail: leandrobatistapereira98@gmail.com

import requests


paginas = []
site = raw_input('Digite a url do site: ')
directory_list = raw_input('Digite a sua wordlist: ')
direc_list = open(directory_list, 'r')
diretorios = direc_list.readlines()
direc_list.close()

for diretorio in diretorios:
    diretorio = diretorio.replace('\n', '')
    barra = site + '/' + diretorio
    r = requests.get(barra)
    status = r.status_code
    if status != 301 and status != 404:
       if not "Page not found" in r.content:
          print "[+] PAGINA ENCONTRADA!: " + barra
          paginas.append(r)
       else:
           print "[-] PAGE NOT FOUND: " + barra
    else:
        print "[-] PAGE NOT FOUND: " + barra

for pagina in paginas:
    print pagina
