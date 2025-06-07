"""6. Ingreso de contraseña
Situación:
    El programa debe pedir al usuario que ingrese una contraseña.
    Solo se permite acceder si la contraseña ingresada es "python123".
    Si es incorrecta, debe pedirla nuevamente hasta que sea correcta.
    Al ingresar la correcta, mostrar "Acceso autorizado"."""
   
password = input("Ingrese el password: ")
intentos = 3
 
while password != "python123":
    print("Contraseña incorrecta...")
    password = input("Ingrese el password: ")
print("Acceso autorizado")    

"""1. Clasificación de nota
Situación: Ingresar una nota del 0 al 10 y mostrar si el estudiante está:
    ● Desaprobado (0 a 5)
    ● Aprobado (6 a 8)
    ● Sobresaliente (9 o 10)"""
    
nota = int(input("Ingrese la nota obtenida(del 0 al 10): "))  

if nota >= 0 and nota <=5:
    print("Desaprobado...")  
elif nota >=6 and nota <=8:
    print("Aprobado...")
elif nota >=9 and nota <=10:
    print("Sobresaliente...")
    