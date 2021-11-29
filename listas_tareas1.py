lista_1=[]


repeticiones_lista=int(input("Cuantos valores quieres en tu lista? "))

for i in range(repeticiones_lista):
    cont_repeticiones=0
    valor=input("Dame un valor: ")
    for j in range(len(lista_1)):
        if(lista_1[j]==valor):
            cont_repeticiones=1
    if(cont_repeticiones<1):
        lista_1.append(valor)
            
print("Los valores de la lista son: ")
for l in range(len(lista_1)):
    print(lista_1[l])


#lista_1=["","mundo","adios","hola"]
#j=1 k=0
#if("mundo"=="" and 1!=2)
#   lista_1[j]=""              eliminamos "hola"
