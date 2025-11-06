def contar_hasta_cero(n):
    if n <= 0: #Caso Base
        print("¡Boom!")
    else: #Caso recursivo
        print(n)
        contar_hasta_cero(n - 1) # llamada recursiva

contar_hasta_cero(5)