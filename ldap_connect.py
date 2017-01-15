#!/usr/bin/env python
# -*- coding: latin-1 -*-
# author: Leandro Pereira
# contato: leandrobatistapereira98@gmail.com
import socket
import sys
import time
import ldap
import iptc

servidor = ['servidor1.com.br',
            'servidor2.com.br', 'servidor3.com.br']


def conect_ldap():
    # CONEXAO COM OS LDAP'S
    try:
        for s in servidor:
            conn = ldap.initialize('ldap://%s:389' % s)
            conn.simple_bind_s('uid=admin,cn=test,cn=br', 'senha')
            conn.set_option(ldap.OPT_TIMEOUT, 10)
            conn.search_s('dc=teste,dc=domain,dc=com,dc=br',
                          ldap.SCOPE_SUBTREE, '(mail=*)', ['cn', 'mail'])
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
        time.sleep(300)
        conect_ldap()
    except ldap.OPT_SUCCESS:
        flush_rules()


def flush_rules():
    # DANDO UM FLUSH NA REGRA DE BLOQUEIO
    chainIn = iptc.Chain(iptc.Table(iptc.Table.FILTER), 'INPUT')
    chainIn.flush()
    # chainOut = iptc.Chain(iptc.Table(iptc.Table.FILTER), 'OUTPUT')
    # chainOut.flush()


conect_ldap()
