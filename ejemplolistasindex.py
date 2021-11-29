lista1=[90,60,30,50,60]
lista2=[120,20,40,60]
print("Mi primera lista es: ")
print(lista1)

print("Se encuentra el valor: ")
print(lista1[4:])

print("Se encuentra el valor: ")
print(lista1[:4])

lista3=lista2+lista1
print("Matriz concatenada: ")
print(lista3)

lista3[3]=55

print("Matriz concatenada corregida: ")
print(lista3)

lista3_ordenada_menorMayor=sorted(lista3)

print("Matriz concatenada de menor a mayor: ")
print(lista3_ordenada_menorMayor)

lista3_ordenada_MayorMenor=sorted(lista3,reverse=True)

print("Matriz concatenada de mayor a menor: ")
print(lista3_ordenada_MayorMenor)
