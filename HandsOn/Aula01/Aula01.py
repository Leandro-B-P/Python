#!/usr/bin/python
""" 
	Bloco de comentario
	do 
	python
"""
#########################################

nome = raw_input("\nDigite seu nome: ")
#print type(nome)
print "\nSeu nome e "+nome

idade = input("\nDigite sua idade: ")
#print type(idade)

print "\nSua idade e ",idade,"anos"

if idade >= 18:
    print "\nVoce e maior de idade!"

else:

    print "\nVoce e menor  de idade"


#Tipos de variaveis

CONSTANTE = 3.14
inteiro = 22
texto = "exemplo de strig"
boole = False
lista = [1,2,3,3.14,"teste"]
tupla = (1,2,3,"teste")
dicionario = {"chave":"valor","chave1":"valor1","chave2":"valor2"}


print lista[2]
print tupla[0]
print dicionario["chave"], dicionario.get("chave2")


#Operadores

num1 = 5
num2 = 1

print num1 + num2
print num1 - num2
print num1 * num2
print num1 / num2
print num1 % num2



#Operadores Logicos

if 10 > 11 and 10 > 9:

    print "10 e maior"

else:

    print "10 nao e maior que os 2 numeros"


if 10 > 5 or 10 > 11 or 10  > 12 or 10 > 13:

    print "10 e maior tambem"

else:

    print "10 nao e maior que pelo menos um dos numero" 


