contrasenia1= input("Genere una contraseña: ").lower()

contrasenia2= input("Verifique la contraseña: ")

if contrasenia1 == contrasenia2:
    print("Acceso Autorizado")
else:
    print("Contraseña incorrecta... ")
    contrasenia2= input("Verifique la contraseña: ")
    print("Contraseña correcta, Bienvenido")
