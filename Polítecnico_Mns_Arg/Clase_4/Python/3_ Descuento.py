precio= int(input("Ingrese el precio del producto: "))

if precio >= 12999:
    precio_final= 0.3 * precio # 35% de descuento
    print("El precio final es:", precio_final)
elif precio < 12999:  
    precio_final= 0.2 * precio # 20% de descuento
    print("El precio final es:", precio_final)
else:
    print("El precio no es valido")