#INICIO
#Como estamos trabajando con tablas, lo mejor será trabajar con DATA FRAMES pues el manejo de la data haciendo uso de este
#tipo de entidades es mucho más rápido y fácil de manejar

#antes que nada, contaremos el numero de vendedores que contiene el .txt pues ese dato lo usaremos mas tarde
with open('DATOS_DE_VENTA.txt') as myfile:
    total_lineas = sum(1 for line in myfile)

import pandas as pd
#Lo primero que hacemos será cargar nuestro archivo de texto a nuestra Panda Data Frame
#Nuevamente, como indica el problema, el txt ya existe y en este caso asumimos que lleva como nombre "DATOS_DE_VENTA"
df = pd.read_table('DATOS_DE_VENTA.txt',header=None,sep=" ",columns = ["Monto","Nombre"]) #sin cabezera pues en el ejemplo del problema se ve que no tiene
							     #como separador usamos la coma, y también añadimos las cabeceras que el archivo de texto no tiene
#ahora que tenemos nuestro data frame en la variable df, lo que haremos será ordenar según lo que nos piden
df_ordenado_x_mayor_ventas = df.sort_values('Monto',ascending=False)

#creamos una lista en orden con una lista ascendente y ordenada de numeros desde el 1 hasta el numero total de vendedores
lista_puestos = range(1,total_lineas)

#ahora con la lista ordenada, añadimos las columnas que necesitamos: Pto, Bono, Porc
df_actualizada = df_ordenado_x_mayor_ventas.assign(Pto = lista_puestos) #el encabezado de esta columna será "Pto"
df_actualizada = df_actualizada.assign(Porc = 11-Pto) #el encabezado de esta columna será "Porc"
df_actualizada = df_actualizada.assign(Bono = Monto*Pto) #el encabezado de esta columna será "Bono"

#finalmente, imprimos el resultado que nos piden
print(df_actualizada)
#FIN
