# -*- coding: utf-8 -*-
"""herrera-jens-pc2-p2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10skAiKWt2Kjv2TdB4pGXZyHBZWPV1zwk
"""

arreglo = []
for i in range(4):
  arreglo.append([0]*3)
cempleado = int(input("Código de empleado: "))
while cempleado != 0:
  cproducto = int(input("Código de producto: "))
  cantidad = int(input("Cantidad: "))
  if (cempleado>=1 and cempleado<=4) and (cproducto>=1 and cproducto<=3):
    arreglo[cempleado-1][cproducto-1] += cantidad
  cempleado = int(input("Código de empleado: "))
print(arreglo)
for i in range(4):
  print("Empleado:",i+1)
  for j in range(3):
    print(f"Producto {j+1}:",arreglo[i][j])

