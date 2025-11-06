nota = int(input("Ingrese su nota 0 a 10: "))
# La nota es mayor a 10 o menor a 0
if nota >= 0 and nota <=5:
    print("Suspenso")
elif nota == 6:
    print("Aprobado")
elif nota == 7:
    print("Buena")
elif nota == 8:
    print("Notable")
elif nota >=9 and nota <=10:
    print("Sobresaliente")