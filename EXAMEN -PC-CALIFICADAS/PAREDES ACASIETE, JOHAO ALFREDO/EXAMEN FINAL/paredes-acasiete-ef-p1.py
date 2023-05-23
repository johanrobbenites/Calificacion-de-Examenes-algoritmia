#INICIO
#NOTA: ASUMIMOS QUE EL ARCHIVO YA EXISTE EN EL ORDENADOR
#Lo primero que haremos es leer el archivo de texto y transformarlo a una lista separando los elementos por cada nueva linea
with open("ALGORITMIA.TXT", "r") as tf:
	lines = tf.read().split('\n')
#Ahora haremos lo mismo pero seperando cada linea por espacios en blanco, generamos tres vectores que almacene cada una de las palabras
#como "W12", "U15", dependiendo si la palabra empieza por W, U o V, así sabremos a qué sección pertenece

W = list()
V = list()
U = list()
for line in lines:
	new_lines = lines.split()
	#aqui haremos el chequeo para ver a que array pertenece cada palabra
	for palabra in new_lines:
		#A lo que me refiero con "palabra" es por ejemplo "W12", "U15"
		if palabra[0] == "U":
			#Solo me interesa la parte numérica de cada palabra, pues con ello realizare los calculos
			U.append(palabra[1:])
		elif palabra[0] == "W":
			#Solo me interesa la parte numérica de cada palabra, pues con ello realizare los calculos
			W.append(palabra[1:])
		elif palabra[0] == "V":
			#Solo me interesa la parte numérica de cada palabra, pues con ello realizare los calculos
			V.append(palabra[1:])
#Ahora que contamos con la data de cada seccion, calculamos lo que nos piden
promedio_W = sum(W)/len(W)
print("El promedio de la seccion U es: ", promedio_W)

promedio_U = sum(U)/len(U)
print("El promedio de la seccion U es: ", promedio_U)

promedio_V = sum(V)/len(V)
print("El promedio de la seccion V es: ", promedio_V)

#Ahora contaremos el numero de alumnos aprobados en cada seccion
contador_W = 0
contador_V = 0
contador_U = 0
for nota in W:
	if nota > 9: #Se aprueba con 10:
		contador_W = contador_W + 1

for nota in U:
	if nota > 9: #Se aprueba con 10:
		contador_U = contador_U + 1

for nota in V:
	if nota > 9: #Se aprueba con 10:
		contador_V = contador_V + 1

print("El numero de alumnos aprobados en la seccion U es de: ", contador_U)
print("El numero de alumnos aprobados en la seccion V es de: ", contador_V)
print("El numero de alumnos aprobados en la seccion W es de: ", contador_W)
tf.close()

#FIN
