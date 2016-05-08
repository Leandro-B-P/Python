#!/usr/bin/python

import psycopg2

try:
    con = psycopg2.connect("host=127.0.0.1 dbname=python user=devops password=4linux")
    print "Conexao com o banco efetuada com sucesso!"
    cur = con.cursor()
    cur.execute("select * from scripts order by id")
    for r in cur.fetchall():
        print r[0],r[1]   
except Exception as e:
    print "Erro: %s"%e
finally:
    cur.close()
    con.close()
    print "Conexao com o banco de dados finalizada com sucesso!"





