# ITESS TICS
# TI-501
# 14/10/2025
# ANÁLISIS DE SEÑALES Y SISTEMAS DE COMUNICACIONES
# Profesor: Francisco Javier Montecillo Puente
# BRANDY AGUILAR FLORES - brandyaguilar001@gmail.com
# DESCRIPCIÓN:Comparando secuencias y otros tipos. Este script muestra cómo se pueden 
# comparar secuencias y otros tipos en Python usando el orden lexicográfico.
# Las secuencias del mismo tipo pueden compararse usando orden lexicográfico.


# Comparaciones entre secuencias del mismo tipo:
print("(1, 2, 3) < (1, 2, 4)")
print((1, 2, 3) < (1, 2, 4))         # True, porque 3 < 4
print("[1, 2, 3] < [1, 2, 4]")
print([1, 2, 3] < [1, 2, 4])         # True, orden lexicográfico igual 
print("(1, 2, 3, 4) < (1, 2, 4)")
print((1, 2, 3, 4) < (1, 2, 4))      # True, porque el tercer elemento 3 < 4
# Comparación entre cadenas
print("'ABC' < 'C' < 'Pascal' < 'Python'")
print('ABC' < 'C' < 'Pascal' < 'Python')
print("(1, 2) < (1, 2, -1)")
print((1, 2) < (1, 2, -1))           # True, porque la primera secuencia es más corta
# Si todos los elementos son iguales, las secuencias se consideran iguales.
print("(1, 2, 3) == (1.0, 2.0, 3.0)")
print((1, 2, 3) == (1.0, 2.0, 3.0))  # True, porque los valores son numéricamente iguales
print("(1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)")
# Cuando los elementos también son secuencias, la comparación se hace de forma recursiva.
print((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))  # True, comparación recursiva

