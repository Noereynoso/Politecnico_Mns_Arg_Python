nota = int(input("Ingrese su nota 0 a 100: "))
# La nota es mayor a 100 o menor a 0
    
if nota >= 90 and nota <= 100:
    print("A")  
elif nota >= 80 and nota <= 89:
    print("B")
elif nota >= 70 and nota <= 79:
    print("C")
elif nota >= 60 and nota <= 69:
    print("D")
elif nota < 60:
    print("F")
else:
    print("Nota no valida")
# La nota no es valida
