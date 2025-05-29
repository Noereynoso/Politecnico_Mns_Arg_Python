#Contenidos por clases:

# Clase 1: Tipos de Datos y Entrada de Información (Input)
# Clase 2: Condicionales simples, compuestos y multiples
# Clase 3: Ciclos Mientras y Para
# Clase 4: Condiciona multiple Con En caso y Menús
# Clase 5: Funciones en Python (con retorno)
# Clase 6: Procedimientos (sin retorno) y repaso general

#2 #Python - Condicionales:

# 1. Condicional clasificación de nota:

# Escribir un programa que pida al usuario una nota (entre 0 y 10) 
# y muestre un mensaje indicando si la nota es "Aprobado" (mayor o igual a 6) 
# o "Desaprobado" (menor a 6).

nota = float(input("ingrese una nota entre 0 y 10: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 2. Par o Impar:
# Escribir un programa que pida al usuario un número entero y
# muestre un mensaje indicando si el número es par o impar.

numero = int(input("Ingrese un número entero: "))
if numero % 2 == 0: #El operador % devuelve el resto de la división entre dos números.
    print("El número es par.")
else:
    print("El número es impar.")
    
# 3. Mayor de Tres Numeros:
# Escribir un programa que pida al usuario tres números y muestre el mayor de ellos.

num1 = float(input("ingrese un número: "))
num2 = float(input("ingrese otro número: "))
num3 = float(input("ingrese otro número: "))

mayor = max (num1, num2, num3) #La función max() devuelve el valor máximo de los argumentos dados.
print(f"El número mayor es: {mayor}")   

# 4. Acceso según la edad:
# Escribir un programa que pida al usuario su edad y muestre 
# un mensaje indicando si puede acceder a un evento (mayor o igual a 18) o no (menor a 18).

edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Puede ingresar al evento")
else:
    print("No puede ingresar al evento, por ser menor de edad")   
    
# 5. Menú de Opciones: (Condicionales múltiples)
# Escribir un programa que muestre un menú con tres opciones y pida al 
# usuario que elija una opción.
# Dependiendo de la opción elegida, mostrar un mensaje diferente.

Menu = int(input("Seleccione una Opción:\n1. Bebidas 1\n2. comida 2\n3. Postre 3\n"))
if Menu == 1:
        print("Usted ha elegido Bebidas")
elif Menu == 2:
        print("Usted ha elegido Comida")
        
elif Menu == 3:
        print("Usted ha elegido Postre")
else:
        print("La Opción no es válida. Por favor, ingrese un número entero.")

# Hacer un programa de Menu, que el usuario pida su bebida despues su comida y luego el postre.

def menu():
    try:
        # Selección de bebida
        print()
        print("Seleccione una Bebida:\n1. Agua\n2. Jugo\n3. Gaseosa\n")
        Menu = int(input("Ingrese su opción: "))
        if Menu == 1:
            bebida = "Agua"
        elif Menu == 2:
            bebida = "Jugo"
        elif Menu == 3:
            bebida = "Gaseosa"
        else:
            print("La Opción no es valida, elija una Bebida.")
            return
        # Selección de comida
        print()
        print("Seleccione una Comida:\n1. Hamburguesa\n2. Pizza\n3. Ensalada\n")
        Menu = int(input("Ingrese su opción: "))
        if Menu == 1:
            comida = "Hamburguesa"
        elif Menu == 2:
            comida = "Pizza"
        elif Menu == 3:
            comida = "Ensalada"
        else:
            print("La Opción no es valida, elija una Comida.")
            return
        # Selección de postre
        print()
        print("Seleccione un Postre:\n1. Helado\n2. Pastel\n3. Fruta\n")
        Menu = int(input("Ingrese su Postre: "))
        if Menu == 1:
            postre = "Helado"
        elif Menu == 2:
            postre = "Pastel"
        elif Menu == 3:
            postre = "Fruta"
        else:
            print("La Opción no es valida, elija un Postre.")
            return
        
        # Mostrar el pedido completo
        print("\nSu pedido es:")
        print(f"Bebida: {bebida}")
        print(f"Comida: {comida}")
        print(f"Postre: {postre}")
        # Confirmar el pedido
        confirmacion = input("¿Desea confirmar su pedido? (s/n): ").lower()
        if confirmacion == 's':
            print("Su pedido ha sido confirmado.")
        else:
            print("Su pedido ha sido cancelado.")
            
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")
# Llamar a la función para ejecutar el menú
menu()

# Python - Repetición:
# 1. Ingresa la contraseña:
# Hcer un programa para que el usuario genere una contraseña, despues le pida verificar.
# una ves que verifique la contraseña correctamente, que le muestre un mensaje de bienvenida.


contrasenia1= input("Genere una contraseña: ").loer()
 
contrasenia2= input("Verifique la contraseña: ")

if contrasenia1 == contrasenia2:
    print("Acceso Autorizado")
else:
    print("Contraseña incorrecta, vuelva a intentarlo")
    contrasenia2= int(input("Verifique la contraseña: "))
    print("Contraseña correcta, Bienvenido")


# 2. uma acumulada hasta número negativo 
# Hacer un conteo  acumulado hasta llegar a numeros negativos.

def suma_acumulada():
    suma = 0
    while True:
        try:
            numero = int(input("Ingrese un numero (negativo para salir): "))
            if numero < 0:
                break
            suma += numero
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")
            continue
    print(f"La suma acumulada es: {suma}")
    
# Llamar a la función para ejecutar la suma acumulada
suma_acumulada()