lista=[]
filas=4
columnas=2
for i in range(filas):
    datos_columna=[]
    for j in range(columnas):
        print("Dame un valor para la fila " ,str(i), " y para la columna ",str(j)," en la matriz: ")
        valor=int(input())
        datos_columna.append(valor)
    lista.append(datos_columna)

print("Mi lista es: ")
print(lista)

print("Mi lista separada por guiones es: ")
for i in range(2):
    for j in range(columnas):
        print(lista[i][j],end=" ")

print()

print("Mi lista separada por guiones es: ")
for columnas1 in lista:
    for datos in columnas1:
        print(datos,end=" ")
    print()
