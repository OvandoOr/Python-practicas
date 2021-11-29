lista_1=[]


repeticiones_lista=int(input("Cuantos valores quieres en tu lista? "))

for i in range(repeticiones_lista):
    valor=input("Dame un valor: ")
    lista_1.append(valor)

for j in range(repeticiones_lista):
    for k in range(repeticiones_lista):
        if(lista_1[j]==lista_1[k] and k!=j):
            lista_1[k]=""
            
print("Los valores de la lista son: ")
for l in range(repeticiones_lista):
    if(lista_1[l]!=""):
        print(lista_1[l])


#lista_1=["","mundo","adios","hola"]
#j=1 k=0
#if("mundo"=="" and 1!=2)
#   lista_1[j]=""              eliminamos "hola"
