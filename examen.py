print("califiquemos a los alumnos ,dame sus matriculas y nombres")
alumno1=input("como se llama?")
matricula1=int(input("dame su matricula"))
print("la matricula",matricula1,"corresponde a el estudiante ",alumno1 )
print("cuantas sesiones de meet se dieron?")
meet=int(input(""))
print("a cuantas clases asistio?")
ASISTENCIAS=int(input(""))
if meet>ASISTENCIAS:
    print("no alcanzo el 10 porciento de la calificacion final")
elif meet>=ASISTENCIAS :
    print("alcanzo el diez porciento de tu calificacion")
print("cuantas actividades se realizaron?")    
actividades=int(input(""))
print("cuantas entrego?")
entregadas=int(input(""))
if entregadas<=actividades:
    print("alcanzo el cuarenta porciento de tu calificacion")
else:
    print("no alcanzo el cuarenta porciento")    
print("cuantos reactivos tenia el examen?")    
reactivos=int(input())
print("cuantas respondio correctamente?")
respuestas=int(input(""))
if respuestas<=reactivos:
    print("alcanzo el cincuenta porciento de su calificacion final ")
else:
    print("no alcanzo el cincuenta porciento")    
print("que porcentaje de asistencias obtuvo?")
procentaje_asistencias1=int(input(""))
print("que porcentaje de actividades obtuvo?")
porcentaje_actividades1=int(input(""))
print("que porcentaje de examen obtuvo?")
procentaje_exam1=int(input(""))
print("su calificacion final es ",procentaje_asistencias1 + porcentaje_actividades1 + procentaje_exam1,"puntos")
calif_final=procentaje_asistencias1 + procentaje_exam1 + porcentaje_actividades1 

lista_alumnos = [ alumno1, matricula1 , calif_final ]

for x in lista_alumnos:
    print (x)
print(len(lista_alumnos))

lista_alumnos.append(input())

for xx in lista_alumnos:
    print(xx)
print(len(lista_alumnos))    