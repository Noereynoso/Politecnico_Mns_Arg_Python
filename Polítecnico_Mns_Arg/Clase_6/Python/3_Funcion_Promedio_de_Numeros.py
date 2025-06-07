def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.

    Parámetros:
        numeros (list): Una lista de números (int o float).

    Retorna:
        float: El promedio de los números en la lista. Si la lista está vacía, retorna 0.

    Ejemplo:
        >>> calcular_promedio([4, 8, 6])
        6.0
    """
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)