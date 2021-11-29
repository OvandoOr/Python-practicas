
lista=[
[1,2,3,4],
[5,6,7,8],
[9,10,11,12]
]

print("Mi lista completa es: ")
print(lista)

valor=lista[2][3]
print("Un valor especifico de la lista es: ",str(valor))


lista[0][2]=30
print("Mi lista completa modificada es: ")
print(lista)

lista.append([13,14,15,16])
print("Mi lista con otra fila agregada es: ")
print(lista)

lista2=[]
filas=4
columnas=4
contador=10
for i in range(filas):
    datos_columna=[]
    for j in range(columnas):
        datos_columna.append(contador)
        contador=contador+1
    lista2.append(datos_columna)

print("Mi lista 2 es: ")
print(lista2)