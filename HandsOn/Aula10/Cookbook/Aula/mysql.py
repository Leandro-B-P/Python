#!/usr/bin/python

import MySQLdb

try:
    con = MySQLdb.connect(host="127.0.0.1",user="devops",db="python",passwd="4linux")
    print "Conexao efetuada com sucesso!"
    cur = con.cursor()
    cur.execute("select * from script order by id desc")
    print cur.fetchone()
except Exception as e:
    print "Erro: %s"%e
finally:
    cur.close()
    con.close()
    print "Conexao finalizada com o banco!"
