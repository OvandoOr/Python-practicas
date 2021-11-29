respuesta=1
while respuesta==1:
    a=int(input("numero de capitulos vistos "))
    b=int(input("tiempo que dura cada capitulo "))

    c=a*b/60

    print("el numero de horas que pasate viendo tele fueron: ")
    print(c)
    if c<2: 
        print(" tu tranqui, sigue viendo netflix :3")
        respuesta=int(input("Quieres repetir la operacion?(1.Si 0.No)"))
    else :
        print(" ya ponte a hacer otra cosa flojo >:(")
        respuesta=0