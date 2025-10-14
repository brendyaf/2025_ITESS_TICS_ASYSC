# ITESS TICS
# TI-501
# 14/10/2025
# ANÁLISIS DE SEÑALES Y SISTEMAS DE COMUNICACIONES
# Profesor: Francisco Javier Montecillo Puente
# BRANDY AGUILAR FLORES - brandyaguilar001@gmail.com
# DESCRIPCIÓN:Modulos. Este script contiene funciones para mostrar o devolver la 
# serie Fibonacci, además contiene el contenido para el interprete.

#crear un archivo llamado fibo.py en el directorio actual, con el siguiente contenido:
# Listo: fibo.py

#Ahora entrá al intérprete de Python e importá este módulo con la siguiente orden:
import fibo
# Esto no mete los nombres de las funciones definidas en fibo directamente en el espacio 
# de nombres actual; sólo mete ahí el nombre del módulo, fibo. Usando el nombre del módulo
# podés acceder a las funciones:
fibo.fib(1000)
#1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
fibo.fib2(100)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
fibo.__name__
#'fibo'
fib = fibo.fib
fib(500)
#1 1 2 3 5 8 13 21 34 55 89 144 233 377