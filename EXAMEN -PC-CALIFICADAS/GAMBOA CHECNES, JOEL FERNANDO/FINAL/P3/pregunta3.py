# -*- coding: utf-8 -*-
"""pregunta3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tLPUKvzj4ZTrKzqgIewZ_SxeAsSywSyj
"""

def palindromo(palabra):
  if(len(palabra))<1:
    k="Es un palindromo"
    return k
  else:
    if palabra[0]==palabra[-1]:
      return palindromo(palabra[1:-1])
    else:
      k="No es un palindromo"
      return k

palabra=input("INGRESE UNA PALABRA: ")
print("¿La palabra",palabra," es un palindromo?: ",palindromo(palabra))