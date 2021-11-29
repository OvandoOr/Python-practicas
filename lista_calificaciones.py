alumnos=[["Nombre","Calificacion"]]

num=int(input("Dame la cantidad de alumnos a calificar: "))

for i in range(num):
    columna=[]
    nombre=input("Dame el nombre del alumno: ")
    columna.append(nombre)
    calificacion=int(input("Dame la calificacion del alumno: "))
    columna.append(calificacion)
    alumnos.append(columna)

print(alumnos)

print("Mi lista separada por guiones es: ")
cont=0
for columnas1 in alumnos:
    if(cont>0):
        print("El alumno",columnas1[0], "tiene la calificacion de",str(columnas1[1]))
    cont=1