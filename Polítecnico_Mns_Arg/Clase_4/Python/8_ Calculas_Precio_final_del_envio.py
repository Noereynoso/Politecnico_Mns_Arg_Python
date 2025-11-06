#Calcular precio final del envío

#Una empresa de transporte ofrece su servicio para enviar paquetes a tres #provincias de la Patagonia Argentina. 
#Cuando un cliente quiere enviar un paquete, puede elegir por distintos tipos de #pesos Ej: (paquete de 15 kg a 20 kg). 
#El cliente contrata el servicio de transporte eligiendo una provincia como destino y un peso de paquete. 
#Se necesita realizar un algoritmo para saber el precio final a pagar. 
#En la siguiente tabla se muestran los destinos con cada peso admitido y su #precio correspondiente.

        # Mostrar opciones de provincias.
print("1. Santa Cruz")
print("2. Chubut")
print("3. Rio Negro")

#Silicitar la provincia
Provincia_de_Envio = int(input("Ingrese la provincia deseada: "))

# Validar la provincia señelada por el usuario
if Provincia_de_Envio not in [1, 2, 3]:
    # Si la provincia no es valida, mostrar un mensaje y salir del programa
    print("Provincia no válida. Por favor, intente de nuevo.")
    exit()
# Mostrar la provincia seleccionada
if Provincia_de_Envio == 1:
    print("Provincia seleccionada: Santa Cruz")
elif Provincia_de_Envio == 2:
    print("Provincia seleccionada: Chubut")
elif Provincia_de_Envio == 3:
    print("Provincia seleccionada: Rio Negro")
    
#Opciones de pesos
if Provincia_de_Envio == 1:
    print("Pesos admitidos: menos de 5 kg,")
    print("entre 5 kg y 10 kg, entre 10 kg y 15 kg")
elif Provincia_de_Envio == 2:
    print("Pesos admitidos: menos de 10 kg,")
    print("entre 11 kg y 15 kg, entre 15 kg y 25 kg")
elif Provincia_de_Envio == 3:
    print("Pesos admitidos: menos de 12 kg,")
    print("entre 12 kg y 18 kg, entre 18 kg y 26 kg")

#Solicitar el peso del pedido al usuario
Pedido = float(input("Ingrese el peso del pedido en kilos: "))

# Calcular el precio según la provincia y el peso

# Santa Cruz
if Provincia_de_Envio == 1:
    if Pedido < 5:
        Precio = 200 * Pedido
    elif Pedido >= 5 and Pedido <= 10:
        Precio = 300 * Pedido
    elif Pedido > 10 and Pedido <= 15:
        Precio = 400 * Pedido
    else:
        Precio = None

# Chubut       
elif Provincia_de_Envio == 2: 
    if Pedido < 10:
            Precio = 350 * Pedido
    elif Pedido > 11 and Pedido <= 15:
            Precio = 390 * Pedido
    elif Pedido > 15 and Pedido <= 25:
            Precio = 420 * Pedido
    else:
            Precio = None
# Rio Negro  
elif Provincia_de_Envio == 3: 
    if Pedido < 12:
            Precio = 390 * Pedido
    elif Pedido > 12 and Pedido <= 18:
            Precio = 480 * Pedido
    elif Pedido > 18 and Pedido <= 26:
            Precio = 510 * Pedido
    else:
            Precio = None

# Mostrar el resultado
if Precio is not None: # El is not none se refiere
    print()
    print(f"El precio total de pedido es: ${Precio:.2f}")
    print()
    print("Si necesita hacer un otro envio selecciona de nuevo la provincia y el peso.")

else:
    print("Coloca un peso, o el peso del pedido no es valido para esta provincia. Intente de nuevo.")

    