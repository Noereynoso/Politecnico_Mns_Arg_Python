#El código que me genero la IA:
# Este código define una función que calcula el promedio de una lista de números.
# La función toma una lista como argumento y devuelve el promedio de los números en la lista.
def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.

    Parámetros:
    numeros (list): Lista de números para calcular el promedio.

    Retorna:
    float: El promedio de los números en la lista. 
    Si la lista está vacía, retorna None.
    """
    if not numeros:
        return None  # Evita la división por cero si la lista está vacía
    return sum(numeros) / len(numeros)

# Ejemplo de uso:
lista_numeros = [10, 20, 30, 40, 50]  # Lista de números para calcular el promedio
# Llama a la función y muestra el resultado
promedio = calcular_promedio(lista_numeros) 
print(f"El promedio es: {promedio}")
