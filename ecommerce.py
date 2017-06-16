#!/usr/bin/python
# -*- coding: utf-8 _-*-
# author: Leandro Batista
# e-mail: leandrobatistapereira98@gmail.com

carrinho = []

produto1 = {'nome': 'Tenis', 'valor': 21.70}
produto2 = {'nome': 'Meia', 'valor': 10}
produto3 = {'nome': 'Camiseta', 'valor': 17.30}
produto4 = {'nome': 'Calca', 'valor': 300.00}

carrinho.append(produto1)
carrinho.append(produto2)
carrinho.append(produto3)
carrinho.append(produto4)

print "Seu carrinho possui ", len(carrinho), " itens."
total = 0
for c in carrinho:
    total += c['valor']

print 'O valor total e de ', total
