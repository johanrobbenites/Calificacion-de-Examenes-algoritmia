def palindromo(n, i, j):
    if i >= j:
        return True
    if n[i] == n[j]:
        return palindromo(n, i+1, j-1)
    else:
        return False

def texto_limpio(n):
    n = n.lower()
    n = n.replace(" ", "")
    n = n.replace("á", "a")
    n = n.replace("é", "e")
    n = n.replace("í", "i")
    n = n.replace("ó", "o")
    n = n.replace("ú", "u")
    return n

texto=input("Ingrese una oracion : ")

texto1 = texto_limpio(texto)

respuesta = palindromo(texto1, 0, len(texto1) - 1)

if respuesta==True:
    print("Es palíndromo")
else:
    print("No es palíndromo")

end=input("")