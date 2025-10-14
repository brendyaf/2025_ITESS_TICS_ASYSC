# dir_funciones.py
# Autor: (tu nombre)
# Descripción: ejemplos de uso de la función dir() en Python

import sys
import fibo.py
import builtins

# 1️ Usando dir() en un módulo
print("Nombres en el módulo fibo:")
print(dir(fib))
print("\nNombres en el módulo sys:")
print(dir(sys))

# 2️ dir() sin argumentos: nombres definidos actualmente
a = [1, 2, 3, 4, 5]
fib = fibo.fib  # asignando la función a un nombre local
print("\nNombres definidos actualmente:")
print(dir())

# 3️ dir() en el módulo builtins: funciones y variables integradas
print("\nNombres en el módulo builtins (funciones y constantes integradas):")
print(dir(builtins))
