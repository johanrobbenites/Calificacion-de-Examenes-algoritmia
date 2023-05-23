#INICIO
def quitar_espacios_en_blanco(s): #aqui quitaremos los espacios en blanco y colocaremos todo en minusculas
	s2 = s.lower() 
	return s2.strip()
	
	
def invertir_oracion(s):
	z = quitar_espacios_en_blanco(s)
	if len(z) == 0:
		return z
	else:
		return invertir_oracion(z[1: ]) + z[0]

entrada = input("Ingrese su oracion: ")
print("La cadena original es: ",entrada)

print("La oracion inversa usando recursion es: ",end="")
print(invertir_oracion(entrada))


a1 = quitar_espacios_en_blanco(entrada)
a2 = invertir_oracion(entrada)

if a1 == a2:
	print("La oracion es, en efecto, palindroma")
else:
	print("La oracion NO es palindroma")

#FIN
