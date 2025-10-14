# ITESS TICS
# TI-501
# 14/10/2025
# ANÁLISIS DE SEÑALES Y SISTEMAS DE COMUNICACIONES
# Profesor: Francisco Javier Montecillo Puente
# BRANDY AGUILAR FLORES - brandyaguilar001@gmail.com
# DESCRIPCIÓN: Este script muestra como se usan los conjuntos en Python. 
# Los conjuntos eliminan elementos duplicados, permiten ver si un elemento está o no está, 
# se pueden combinar o comparar con operaciones como unión, intersección o diferencia,
# y también se pueden crear con comprensiones de listas.


# Conjuntos (sets)
canasta = {'manzana', 'naranja', 'manzana', 'pera', 'naranja', 'banana'}
print("canasta =", canasta)  # muestra que se eliminaron los duplicados

print("'naranja' in canasta:", 'naranja' in canasta)  # True
print("'yerba' in canasta:", 'yerba' in canasta)      # False

# Veamos las operaciones para las letras únicas de dos palabras
a = set('abracadabra')
b = set('alacazam')
print("a =", a)       # letras únicas en a
print("b =", b)       # letras únicas en b
print("a - b =", a - b)   # letras en a pero no en b
print("a | b =", a | b)   # letras en a o en b
print("a & b =", a & b)   # letras en a y en b
print("a ^ b =", a ^ b)   # letras en a o b pero no en ambos

# Comprensión de listas
a = {x for x in 'abracadabra' if x not in 'abc'}
print("a =", a)  # {'r', 'd'}


