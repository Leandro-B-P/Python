#!/usr/bin/python


def func1(*args):
    print "\nForam passados",len(args),"parametros\n"
    print args[0]

def func2(**kwargs):
    print "\nForam passados",len(kwargs),"parametros\n"
    print kwargs

quadrado = lambda x: x*x

print quadrado(2)
