# -*- coding: utf-8 -*-
"""Untitled51.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kMqHPQUAfC6Qz9lcU-lfP5NhkHvECM8W
"""

m = []
for i in range(4):
  m.append([0]*3)
print(m)
codigo = -18
while codigo != 0:
  codigo_producto = int(input("INGRESE EL CODIGO DEL PRODUCTO DEL 1 AL 3: "))
  cantidad = int(input("INGRESE LA CANTIDAD: "))
  if (codigo >= 1 and codigo <= 4) and (codigo_producto >= 1 and codigo_producto <= 3) and cantidad > 0:
    m[codigo-1][codigo_producto-1] = m[codigo-1][codigo_producto-1] + cantidad
  codigo = int(input("INGRESE EL CODIGO DEL EMPLEADO DEL 1 AL 4: "))
for i in range(4):
  print("EMPLEADO: ", i+1)
  for j in range(3):
    print("CODIGO PRODUCTO: ", j+1, " ", m[i][j])