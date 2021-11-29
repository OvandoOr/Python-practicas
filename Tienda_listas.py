nombres_productos=[]
costos_productos=[]
respuesta="si"
#cantidad=int(input("Cuantos productos quieres? "))

#for i in range(cantidad):
while(respuesta=="si"):
    nombre=input("Dame el nombre del producto ")
    nombres_productos.append(nombre)
    respuesta=input("Quieres comprar otro producto?(si,no) ")

print("Los productos son los siguientes:")
#for i in range(cantidad):
for i in range(len(nombres_productos)):
    print(nombres_productos[i]+" y el costo es "+str(costos_productos[i]))