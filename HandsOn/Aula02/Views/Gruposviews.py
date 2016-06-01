#!/usr/bin/python
#run.py
#Leandro Batista

from flask import Blueprint,jsonify,request
from Models.Model import Grupos as GruposModel
import json

grupos = Blueprint("grupos",__name__)

@grupos.route("/grupos/")
def index():
    g = GruposModel.objects.to_json()
    g = json.loads(g)
    return jsonify({"grupos":g})

@grupos.route("/grupos/",methods=["POST"])
def add_grupos():
    g = GruposModel()
    g.nome = request.get_json().get("nome")
    g.save()
    return jsonify({"message":"Grupo cadastrado com sucesso"})

@grupos.route("/grupos/<id>/append/",methods=["POST"])
def append_grupos(id):
    g = GruposModel.objects(id=id).first()
    g.integrantes.append(request.get_json().get("email"))
    g.save()
    return jsonify({"message":"Usuario cadastrado com sucesso"})

@grupos.route("/grupos/<id>/",methods=["PUT"])
def update_grupos(id):
    return "Atualizacao de grupos"


@grupos.route("/grupos/<id>/",methods=["GET"])
def get_grupos(id):
    return "Busca de grupos"

@grupos.route("/grupos/<id>/",methods=["DELETE"])
def delete_grupos(id):
    return "Delete de grupos"

