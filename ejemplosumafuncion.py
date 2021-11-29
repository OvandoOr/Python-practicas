import ejemplofuncion as f1
#matricula 202009100150
Total=int(input("Escribe el valor del producto "))
area=input("Escribe el nombre del area para darte un descuento. ")
if(area=="electronicos"):
    c=f1.descuento(Total,50)
if(area=="carnes"):
    c=f1.descuento(Total,15)
if(area=="panes"):
    c=f1.descuento(Total,25)


print("El valor final de la compra es: ")
print(c)





