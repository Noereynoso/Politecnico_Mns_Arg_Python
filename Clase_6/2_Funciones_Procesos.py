#DIFERENCIA ENTRE UN PROSESO Y UNA FUNCION
#Una funcion es un bloque de codigo que se puede reutilizar y que puede recibir argumentos y devolver un valor
#Un proceso es una instancia de un programa en ejecucion, que tiene su propio espacio de memoria y recursos del sistema
#Un proceso puede contener varias funciones, y cada funcion puede ser llamada por diferentes procesos
#Un proceso puede ejecutarse en paralelo con otros procesos, mientras que una funcion se ejecuta de manera secuencial dentro de un proceso

functions = {
    'suma': lambda x, y: x + y,
    'resta': lambda x, y: x - y,
    'multiplicacion': lambda x, y: x * y,
    'division': lambda x, y: x / y,
}

def calcular(funcion, x, y):
    if funcion in functions:
        return functions[funcion](x, y)
    else:
        raise ValueError(f"La funcion {funcion} no esta definida.")

def main():
    print("Bienvenido a la calculadora de funciones.")
    print("Funciones disponibles: suma, resta, multiplicacion, division")
    funcion = input("Ingrese la funcion que desea utilizar: ")
    x = float(input("Ingrese el primer numero: "))
    y = float(input("Ingrese el segundo numero: "))
    
    try:
        resultado = calcular(funcion, x, y)
        print(f"El resultado de {funcion}({x}, {y}) es: {resultado}")
    except ValueError as e:
        print(e)
    except ZeroDivisionError:
        print("Error: Division por cero no es permitida.")
        