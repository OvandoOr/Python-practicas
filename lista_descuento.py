import ejemplofuncion as f1

lista_1=[]
lista_2=[]
respuesta="si"

while(respuesta=="si"):
    valor=int(input("Dame un valor: "))
    lista_1.append(valor)
    respuesta=(input("Quieres agregar otro numero?"))

for i in range(len(lista_1)):
    valor=lista_1[i]*.15
    valor_desc=lista_1[i]-valor
    lista_2.append(valor_desc)

print("Lista 1")
print(lista_1)
print("Lista 2")
print(lista_2)
