Estatura = float(input("Ingrese su estatura en centimetros: "))
# La estatura es mayor a 250 o menor a 0
if Estatura <= 150:
    print("Persona de altura baja")
elif Estatura > 151 and Estatura <= 170:
    print("Persona de altura media")
elif Estatura > 171:
    print("Persona de altura alta")