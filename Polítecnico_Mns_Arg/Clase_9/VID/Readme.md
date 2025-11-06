# 📦 Calculadora de Precio Final de Envío

Este programa en Python permite calcular el precio final para enviar un paquete a una de tres provincias de la Patagonia Argentina, según el peso del paquete y la provincia seleccionada por el usuario.

---

## 📝 ¿Cómo funciona el programa?

### 1. **Mostrar opciones de provincias**
El programa imprime en pantalla las tres provincias disponibles:
- 1. Santa Cruz
- 2. Chubut
- 3. Rio Negro

### 2. **Solicitar la provincia**
El usuario debe ingresar el número correspondiente a la provincia de destino.

### 3. **Validar la provincia**
Si el usuario ingresa un número que no corresponde a ninguna provincia, el programa muestra un mensaje de error y termina.

### 4. **Mostrar la provincia seleccionada**
El programa confirma la provincia elegida mostrando su nombre.

### 5. **Mostrar los rangos de peso admitidos**
Según la provincia seleccionada, se muestran los rangos de peso permitidos para el envío.

### 6. **Solicitar el peso del pedido**
El usuario ingresa el peso del paquete en kilos.

### 7. **Calcular el precio según provincia y peso**
El programa utiliza condicionales (`if`, `elif`, `else`) para determinar el precio por kilo según la provincia y el rango de peso:
- **Santa Cruz:**  
  - Menos de 5 kg: $200 por kg  
  - 5 a 10 kg: $300 por kg  
  - 10 a 15 kg: $400 por kg  
- **Chubut:**  
  - Menos de 10 kg: $350 por kg  
  - 11 a 15 kg: $390 por kg  
  - 15 a 25 kg: $420 por kg  
- **Río Negro:**  
  - Menos de 12 kg: $390 por kg  
  - 12 a 18 kg: $480 por kg  
  - 18 a 26 kg: $510 por kg  

Si el peso no corresponde a ningún rango válido, el precio será `None`.

### 8. **Mostrar el resultado**
- Si el precio fue calculado correctamente, se muestra el precio total del pedido.
- Si el peso no es válido para la provincia seleccionada, se muestra un mensaje de error.

---

## 🛠️ Conceptos de Python utilizados

- **Entrada y salida de datos:** `input()` y `print()`
- **Condicionales:** `if`, `elif`, `else`
- **Validación de datos:** para asegurar que la provincia y el peso sean válidos
- **Variables:** para almacenar la provincia, el peso y el precio
- **Cálculos matemáticos:** multiplicación para obtener el precio total

---

## 🚀 Resumen

Este programa es para practicar condicionales, validación de datos y operaciones matemáticas en Python. Simula un sistema real de cálculo de precios de envíos según destino y peso, ayudando a comprender cómo estructurar programas interactivos y útiles.

---
