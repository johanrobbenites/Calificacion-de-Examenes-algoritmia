n= int(input("ingrese un numero : "))
a=[0]*n
aprobados=0
for i in range(0,n):
    a[i]= int(input(f"ingrese la nota del alumno numero {i+1} : "))
    if a[i] >=10 and a[i]<20:
        aprobados = aprobados + 1
aprobados_porcentaje= (aprobados*100)/n
print(a) , print(str(round(aprobados_porcentaje,2)) +" % de aprobados"), print("----------------------")
aprobados = 0
while aprobados_porcentaje < 70:
    for i in range(0,n):
        if a[i] <20:
            a[i]= a[i]+1
        if a[i] >=10 and a[i]<20:
            aprobados = aprobados +1
    aprobados_porcentaje = (aprobados*100)/n
    print(a)
    print(str(round(aprobados_porcentaje,2)) +" % de aprobados")
    print("----------------------")
    aprobados = 0
resultado_final = round(aprobados_porcentaje,2)
print(f"El procentaje final de aprobados es : {resultado_final}")
end= input(" ")