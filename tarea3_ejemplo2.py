num_alumnos=int(input("Escribe numero de alumnos"))
variable=""

for i in range(num_alumnos):
    nom=input("Nombre del alumno: ")
    cal=int(input("Ingresa la calificacion "))
    while cal<0 or cal>10:
        cal=int(input("Introduce la calificacion "))
    print("listo")
    print(nom," obtuvo la calificacion de ",cal)




#2. Calcular la calificación de N alumnos primero pidiendo la camtidad de alumnos 
# a la que se les pedirá la nota,luego introduciendo su nombre, 
# calificación teórica (60%) y su calificación practica (40%) 
# por cada alumno (recomiendo el uso de un for) . 
# Mostrarlo por pantalla su nombre y calificación final. 
# En caso de que se envíen calificaciones que no estén en el rango del 
# 0 a 10 vuelvan a pedir calificación. 