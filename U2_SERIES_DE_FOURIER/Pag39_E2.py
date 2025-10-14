# ITESS TICS
# TI-501
# 14/10/2025
# ANÁLISIS DE SEÑALES Y SISTEMAS DE COMUNICACIONES
# Profesor: Francisco Javier Montecillo Puente
# BRANDY AGUILAR FLORES - brandyaguilar001@gmail.com
# DESCRIPCIÓN: ejemplos de uso de la función dir() en Python

import sys
import fibo
import builtins

# La función integrada dir() se usa para encontrar qué nombres define un módulo.
# Devuelve una lista ordenada decadenas:
print("dir(fibo)")
print(dir(fibo))
print("dir(sys)")
print(dir(sys))

# Sin argumentos, dir() lista los nombres que tenés actualmente definidos:
a = [1, 2, 3, 4, 5]
print("a = [1, 2, 3, 4, 5]")
print("fib = fibo.fib")
fib = fibo.fib 
print("\nNombres definidos actualmente:")
print(dir())

# dir() no lista los nombres de las funciones y variables integradas. Si queeres
# una lista de esos, están definidos en el módulo estándar builtins:
print("\nNombres en el módulo builtins:")
print(dir(builtins))
