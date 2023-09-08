#! /usr/bin/env python3

""" Hello world, Multi Linguas

Dependendo da variável LANG exibirá na linguagem
USAGE: ter a var LANG devidamente configurada

"""
__version__ = "0.0.1"
__author__ = "Leandro Amorim"
__license__= "Payment for bitcoins"

import os

#-----------------------------------------------------
current_language = os.getenv("LANG") [:5]
msg = "wtf"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "en_US":
    msg = "Hello World!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"




print (msg)
