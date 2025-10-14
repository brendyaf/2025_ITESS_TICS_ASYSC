# ITESS TICS
# TI-501
# 14/10/2025
# ANÁLISIS DE SEÑALES Y SISTEMAS DE COMUNICACIONES
# Profesor: Francisco Javier Montecillo Puente
# BRANDY AGUILAR FLORES - brandyaguilar001@gmail.com
# DESCRIPCIÓN: Formateo elegante de la salida. Este script muestra cómo imprimir y formatear información en Python. 
# Incluye ejemplos de str(), repr(), zfill(), tablas con rjust() y str.format(), y 
# como mostrar datos de forma clara y ordenada.

import math
s = 'Hola mundo.'
print("str(s)")
print(str(s))
#'Hola mundo.'
print("repr(s)")
print(repr(s))
#"'Hola mundo.'"
print("str(1 / 7)")
print(str(1 / 7))
#'0.142857142857'
print("x = 10 * 3.25")
x = 10 * 3.25
print("y = 200 * 200")
y = 200 * 200
print (s = 'El valor de x es ' + repr(x) + ', y es ' + repr(y) + '...')
print(s)
# El valor de x es 32.5, y es 40000...
# El repr() de una cadena agrega apóstrofos y barras invertidas
hola = 'hola mundo\n'
print("hola = 'hola mundo\n'")
holas = repr(hola)
print(holas)
'hola mundo\n'
# El argumento de repr() puede ser cualquier objeto Python:
print("repr((x, y, ('carne', 'huevos')))")
repr((x, y, ('carne', 'huevos')))
#"(32.5, 40000, ('carne', 'huevos'))"

# Dos maneras de escribir una tabla de cuadrados y cubos:
print("Manera 1")
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
# notar el uso de 'end' en la linea anterior
    print(repr(x * x * x).rjust(4))

#1 1 1
# 2 4 8
# 3 9 27
# 4 16 64
# 5 25 125
# 6 36 216
# 7 49 343
# 8 64 512
# 9 81 729
# 10 100 1000
print("Manera 2")
for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

# 1 1 1
# 2 4 8
# 3 9 27
# 4 16 64
# 5 25 125
# 6 36 216
# 7 49 343
# 8 64 512
# 9 81 729
# 10 100 1000

# Hay otro método, str.zfill(), el cual rellena una cadena numérica a la izquierda con ceros
# Entiende signos positivos y negativos:
print("'12'.zfill(5)")
print('12'.zfill(5))
#'00012'
print("'-3.14'.zfill(7)")
print('-3.14'.zfill(7))
#'-003.14'
print('3.14159265359'.zfill(5))
#'3.14159265359'
#El uso básico del método str.format() es como esto:
print('Somos los {} quienes decimos "{}!"'.format('caballeros', 'Nop'))
# Somos los caballeros quienes decimos "Nop!"
