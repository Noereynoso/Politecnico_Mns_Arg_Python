def factorial(n):
    if n == 0 or n == 1:  # Caso base
        return 1
    else:  # Caso recursivo
        return n * factorial(n - 1)  # Llamada recursiva