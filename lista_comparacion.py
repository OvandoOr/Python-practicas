lista_1=[]
lista_2=[]
respuesta="si"
while(respuesta=="si"):
    valor=int(input("Dame un valor para lista 1: "))
    lista_1.append(valor)
    respuesta=(input("Quieres agregar otro numero?"))


respuesta="si"
while(respuesta=="si"):
    valor=int(input("Dame un valor para lista 2: "))
    lista_2.append(valor)
    respuesta=(input("Quieres agregar otro numero?"))

for i in range(len(lista_1)):
    for j in range(len(lista_2)):
        if(lista_1[i]==lista_2[j]):
            print("Se repiten en el valor", lista_1[i])
            print("En el index de la lista_1: ", str(i), " y de la lista_2: ", str(j))


#lista_1["hola","mundo","adios"]
#lista_2["nada","adios","nada2"]
#i=2 j=1
#if("adios"=="adios"):
#Se repiten en el index de la lista 1: 2 y de la lista 2: 1