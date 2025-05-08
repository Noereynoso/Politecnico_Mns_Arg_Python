# Introducción a Python

Python es un lenguaje de programación muy popular por su sencillez y versatilidad. Es ideal para principiantes y también es usado profesionalmente en ciencia de datos, desarrollo web, automatización, inteligencia artificial y mucho más.

---

## ¿Cómo se usa Python?

1. **Instala Python** desde [python.org](https://www.python.org/).
2. Escribe tu código en un archivo con extensión `.py`.
3. Ejecuta tu archivo desde la terminal o consola:
   ```bash
   python nombre_del_archivo.py

## Como Crear Un Codigo Sencillo            

        num1 = 10
        num2 = 25
        num3 = 7

        if num1 > num2 and num1 > num3:
            print("El número mayor es:", num1)
        elif num2 > num1 and num2 > num3:
            print("El número mayor es:", num2)
        elif num3 > num1 and num3 > num2:
            print("El número mayor es:", num3)
        else:
            print("Hay números iguales o todos son iguales")

        mayor = max(num1, num2, num3)
            print(f"El número mayor es: {mayor}")


## Como Crear Una Procedimiento de Saludo Sencillo

        def saludar(nombre):
            print(f"¡Hola, {nombre}!")

        saludar("Ana")

## Como Crear Una Función de suma Sencilla 
     
        def sumar(a, b):
            return a + b

        resultado = sumar(5, 3)
        print("La suma es:", resultado)

## Función para saber si un número es par o impar
        
        def es_par(numero):
            if numero % 2 == 0:
                print(f"{numero} es par")
            else:
                print(f"{numero} es impar")

        es_par(8)
        es_par(13)

## Función para calcular el área de un círculo

        def area_circulo(radio):
            pi = 3.1416
            return pi * radio * radio

        print("Área de un círculo de radio 4:", area_circulo(4))

---