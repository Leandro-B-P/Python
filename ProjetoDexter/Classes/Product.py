#!/usr/bin/python


class Product:
    _id = ""
    _name = ""
    _description = ""
    _image = ""

    def __init__(self,name="",description="",image=""):
        self._name = name
        self._description = description
        self._image = image
