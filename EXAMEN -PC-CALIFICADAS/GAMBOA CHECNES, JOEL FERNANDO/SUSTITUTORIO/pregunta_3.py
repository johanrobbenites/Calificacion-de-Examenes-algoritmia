# -*- coding: utf-8 -*-
"""PREGUNTA 3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VHCbZp7GbTTNX9lPTZXlPZ0fHNFexsx8
"""

def encontrar(palabra,encont):
  lista=palabra.split(" ")
  m=lista.count(encont)
  return m

palabra=input("INGRESE LA ORACION: ")
palabra=palabra.upper()
encont=input("INGRESE LA PALABRA A ENCONTRAR: ")
encont=encont.upper()
print("LA PALABRA ","<<",encont,">>", " SE REPITE ", encontrar(palabra,encont)," VECES ")