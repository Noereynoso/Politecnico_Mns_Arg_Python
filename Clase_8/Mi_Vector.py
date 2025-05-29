"""Crear un vector con 4 notas de un alumno y mostrar el 
promedio por pantalla. """

notas = [6, 7]

# Calcular el promedio
suma = 0
for nota in notas:
    suma += nota
promedio = suma / len(notas)
print(f"El promedio de las notas es: {promedio:.2f}")
# Mostrar el promedio por pantalla
