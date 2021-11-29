AREA_1 = "area1"
AREA_2 = "area2"
AREA_3 = "area3"

while True:

    # pide cantidad
    print("Ingrese el monto: ")
    amount = float(input())

    # pide tipo de producto
    print("Ingresa el tipo de producto")
    tipoDeProducto = input()

    # pide area
    while True:
        print("Ingrese el area de la tienda: ")
        area = input()
        areaIsvalid = (area == AREA_1 or area == AREA_2 or area == AREA_3)
        if areaIsvalid:
            break
        else:
            print("Por favor ingrese  un area valida")

    #pide matricula
    while True:
        print("Ingresa matricula: ")
        matricula = input()
        matriculaHasEnoughSize = len(matricula)  == 10
        if matriculaHasEnoughSize:
            break
        else:
            print("Ingresa una matricula valida")

    #hace descuento
    if area == AREA_1:
        percent = float(matricula[8] + matricula[9])/100
    elif area == AREA_2:
        percent = float(matricula[7] + matricula[8])/100
    elif area == AREA_3:
        percent = float(matricula[9])/100

    #aplica descuento
    total = amount - (amount * percent)
    print("Se aplico un descuento de: " + str(percent * 100) + "%")
    print("En total es: " + str(total) + "$")
    if total > 2000:
        print("Se ha ganado un regalo...")

    print("¿Desea comprar otra cosa? si/no")
    if input() == "no":
        break
