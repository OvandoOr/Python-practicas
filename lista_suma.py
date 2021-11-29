lista_1=[]
respuesta=1

while(respuesta):
    valor=int(input("Dame un valor: "))
    lista_1.append(valor)
    respuesta=int(input("Quieres agregar otro numero?"))

sumatoria=0
for i in range(len(lista_1)):
    sumatoria=sumatoria+lista_1[i]

print("El valor de la sumatoria es: ",str(sumatoria))
