num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

# Verificamos cual es el mayor de los tres numeros

mayor = max(num1,num2,num3)
print(f" el numero mayor es:{mayor}")

 #Otra forma de hacerlo
if num1 > num2 and num1 > num3:
    print("El numero mayor es:", num1)
elif num2 > num1 and num2 > num3:
    print("El numero mayor es:", num2)
elif num3 > num1 and num3 > num2:
    print("El numero mayor es:", num3)
elif num1 == num2 and num1 > num3:
    print("El numero mayor es:", num1)
elif num1 == num3 and num1 > num2:
    print("El numero mayor es:", num1)
else:
    print("Los numeros son iguales")

