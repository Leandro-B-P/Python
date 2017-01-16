#!/usr/bin/env python
# -*- coding: latin-1 -*-
# author: Leandro Pereira
# contato: leandrobatistapereira98@gmail.com
#############################################
import socket
import sys
import time
import ldap
import iptc

servidor = ['servidor1.teste.com.br', 'servidor2.teste.com.br', 'servidor3.teste.com.br']


def conect_ldap():
    # CONEXAO COM OS LDAP'S
    try:
        for s in servidor:
            # CONECTANDO-SE AO LDAP
            conn = ldap.initialize('ldap://%s:389' % s)
            # PASSANDO O USER E SENHA
            conn.simple_bind_s('uid=zimbra,cn=admins,cn=zimbra', 'senha')
            # TIMEOUT DE 10 SEGUNDOS
            conn.set_option(ldap.OPT_TIMEOUT, 10)
            # BUSCA NA BASE PELO E-MAIL
            conn.search_s('dc=lab03,dc=u,dc=teste,dc=com,dc=br',
                          ldap.SCOPE_SUBTREE, '(mail=*)', ['cn', 'mail'])
            # SE TUDO ESTA OK AGUARDA 1s E PRINTA NA TELA
            time.sleep(1)
            print('%s %s Conexao Realizada com Sucesso!') % (time.ctime(), s)
            # CONVERTENDO NOME EM IP
            ip = socket.gethostbyname(s)
            return ip

    # EXCECAO EM CASO DE TIMEOUT
    except (ldap.SERVER_DOWN, ldap.TIMEOUT) as e:
        if e:
            print("Ocorreu o seguinte error (%s)") % e
            rules_iptables(s)
        else:
            sys.exit(0)


def rules_iptables(ip):

    try:
        # APLICAR AS REGRAS DE IPTABLES
        print("\nAplicando regras do IPTABLES...")
        chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
        rule = iptc.Rule()
        rule.in_interface = "eth0"
        rule.src = "%s" % ip
        target = iptc.Target(rule, "REJECT")
        rule.target = target
        chain.insert_rule(rule)
        time.sleep(1)
        # ESPERANDO 2 SEGUNDOS
        print("Regras Aplicadas... %s") % time.ctime()
	time.sleep(5)
	flush_rules()
        time.sleep(10)
        conect_ldap()
    except (ldap.SERVER_DOWN, ldap.TIMEOUT) as i:
	if i:
	    rules_iptables(s)
	else:
	    pass

def flush_rules():
    # DANDO UM FLUSH NA REGRA DE BLOQUEIO
    chainIn = iptc.Chain(iptc.Table(iptc.Table.FILTER), 'INPUT')
    chainIn.flush()
    # chainOut = iptc.Chain(iptc.Table(iptc.Table.FILTER), 'OUTPUT')
    # chainOut.flush()


conect_ldap()

