# ITESS TICS
# TI-501
# 14/10/2025
# ANÁLISIS DE SEÑALES Y SISTEMAS DE COMUNICACIONES
# Profesor: Francisco Javier Montecillo Puente
# BRANDY AGUILAR FLORES - brandyaguilar001@gmail.com
# DESCRIPCIÓN: Este script muestra diferentes técnicas de iteración en Python, usando estructuras como listas y diccionarios.
# Se explican ejemplos prácticos de cómo recorrer diccionarios con sus claves y valores, obtener índices al iterar listas, emparejar elementos
# de dos secuencias, recorrer elementos en orden inverso u ordenado, y cómo modificar listas mientras se recorre una copia de ellas


# Cuando iteramos sobre diccionarios, se pueden obtener al mismo tiempo la clave y su valor 
# correspondiente usando el
# método items().
print("Iteración sobre diccionarios:")
caballeros = {'gallahad': 'el puro', 'robin': 'el valiente'}
print("caballeros = {'gallahad': 'el puro', 'robin': 'el valiente'}")
print("for k, v in caballeros.items(): print(k, v)")
for k, v in caballeros.items():
    print(k, v)

#gallahad el puro
#robin el valiente

# Cuando se itera sobre una secuencia, se puede obtener el índice de posición junto a su 
# valor correspondiente usando la función enumerate().
print("Iteracuón sobre una secuencia:")
print("for i, v in enumerate(['ta', 'te', 'ti']):print(i, v)")
for i, v in enumerate(['ta', 'te', 'ti']):
    print(i, v)
#0 ta
#1 te
#2 ti

# Para iterar sobre dos o más secuencias al mismo tiempo, los valores pueden emparejarse con 
# la función zip().
print("Iteración sobre dos o más secuencias al mismo tiempo:")
preguntas = ['nombre', 'objetivo', 'color favorito']
print("preguntas = ['nombre', 'objetivo', 'color favorito']")
respuestas = ['lancelot', 'el santo grial', 'azul']
print ("respuestas = ['lancelot', 'el santo grial', 'azul']")
print("for p, r in zip(preguntas, respuestas): print('Cual es tu {0}? {1}.'.format(p, r))")
for p, r in zip(preguntas, respuestas):
    print('Cual es tu {0}? {1}.'.format(p, r))

#Cual es tu nombre? lancelot.
#Cual es tu objetivo? el santo grial.
#Cual es tu color favorito? azul.

# Para iterar sobre una secuencia en orden inverso, se especifica primero la secuencia al derecho 
# y luego se llama a la función reversed().
print("Iteración sobre una secuencia en orden inverso:")
print("for i in reversed(range(1, 10, 2)): print(i)")
for i in reversed(range(1, 10, 2)):
    print(i)
#9
#7
#5
#3
#1

# Para iterar sobre una secuencia ordenada, se utiliza la función sorted() la cual devuelve una 
# nueva lista ordenada dejando a la original intacta.
print("Iteración sobre una secuencia ordenada:")
canasta = ['manzana', 'naranja', 'manzana', 'pera', 'naranja', 'banana']
print("canasta = ['manzana', 'naranja', 'manzana', 'pera', 'naranja', 'banana']")
print("for f in sorted(set(canasta)): print(f)")
for f in sorted(set(canasta)):
    print(f)

# banana
# manzana
# naranja
# pera

# Ciclar sobre una secuencia no hace implícitamente una copia. La notación de rebanadas es 
# especialmente conveniente para esto:
print("Ciclar sobre una secuencia no hace implícitamente una copia:")
print("palabras = ['gato', 'ventana', 'defenestrar']")
palabras = ['gato', 'ventana', 'defenestrar']
print("for p in palabras[:]: # ciclar sobre una copia de la lista entera if len(p) > 6: palabras.insert(0, p)")
for p in palabras[:]: # ciclar sobre una copia de la lista entera
    if len(p) > 6:
        palabras.insert(0, p)

print(palabras)
#['defenestrar', 'gato', 'ventana', 'defenestrar']
