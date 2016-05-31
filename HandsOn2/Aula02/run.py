#!/usr/bin/python
#run.py
#Leandro Batista

from flask import Flask,request
from Views.Gruposviews import grupos
from Views.Usuariosviews import usuarios

app = Flask(__name__)
app.register_blueprint(grupos)
app.register_blueprint(usuarios)

#Criando decorator

#def valida_usuario(func):
    #Funcao decorada - recebe qualquer parametro
#    def f(*args,**kwargs):
        
#        if request.args.get("token") != "4linux":
#           return "Acesso negado!"
#        else:
#            return func(*args,**kwargs)
#    return f

#def force_auth(*args,**kwargs):
#        if request.args.get("token") != "4linux":
#            return "Acesso negado!"
        

#app.before_request(force_auth)
            
@app.route("/")
def index():
    return "Debug ativado"


if __name__=='__main__':
    app.run(port=3000,host="0.0.0.0",debug=True)
