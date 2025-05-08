#1- Validación de entrada de usuario: 

# Solicitar al usuario que ingrese un número entre 1 y 100, y validar la entrada.

while True:
    try:
        usuario = int(input("Ingrese un número entre 1 y 100: "))
        if 1 <= usuario <= 100:
            print("Entrada válida:", usuario)
            print("¡¡Puede pasar!!")
            break  # Salir del bucle si la entrada es válida
        else:
            print("Este número no esta en la lista. Por favor, intente nuevamente.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")