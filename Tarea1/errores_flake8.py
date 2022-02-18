# Este programa escoge 3 numeros al azar.
# Muestra los tres numeros y el resultado de 3 operaciones
# Se importa la libreria random
import random

# Se seleccionan los 3 numeros al azar de manera aleatoria de entre -100 y 100
num1 = random.randint(-100, 100);
num2 = random.randint(-100, 100)
num3 = random.randint(-100,100)

# Se realizan las operaciones de suma, multipicacion y promedio
suma = num1 + num2 + num3
multiplicacion = num1 * num2 * num3
promedio = (suma/3)

#Se imprimen los numeros y los resultados de sus operaciones
print("Los numeros seleccionados son:       ", num1, num2, num3)
print("La suma de los numeros es:           ", suma)
print("La multiplicacion de los numeros es: ", multiplicacion)
print("El promedio de los numeros es:       ", promedio)
