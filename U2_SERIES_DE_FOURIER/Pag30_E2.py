# ITESS TICS
# TI-501
# ANÁLISIS DE SEÑALES Y SISTEMAS DE COMUNICACIONES
# Profesor: Francisco Javier Montecillo Puente
# BRANDY AGUILAR FLORES - brandyaguilar001@gmail.com
# DESCRIPCIÓN: Tuplas y secuencias, las tuplas son secuencias inmutables de elementos.
# En este script smuestra que se pueden guardar listas dentro, y sque se pueden separar 
# en varias variables. También explica cómo hacer tuplas vacías o con un solo valor.

# Una tupla consiste de un número de valores separados por comas
print("t = 12345, 54321, 'hola!'")
t = 12345, 54321, 'hola!'
print(t[0])
#12345
print(t)
#(12345, 54321, 'hola!')

# Las tuplas pueden anidarse:
print("u = t, (1, 2, 3, 4, 5)")
u = t, (1, 2, 3, 4, 5)
print(u)
#((12345, 54321, 'hola!'), (1, 2, 3, 4, 5))

# Las tuplas son inmutables:
#t[0] = 88888
#Traceback (most recent call last):
#File "<stdin>", line 1, in <module>
#TypeError: 'tuple' object does not support item assignment

# pero pueden contener objetos mutables:
print("v = ([1, 2, 3], [3, 2, 1]")
v = ([1, 2, 3], [3, 2, 1])
print(v)
#([1, 2, 3], [3, 2, 1])

# Las tuplas vacías se construyen mediante un par de paréntesis vacío; una tupla con un ítem se construye
# poniendo una coma a continuación del valor.
print("Tuplas vacías")

vacia = ()
singleton = 'hola', # <-- notar la coma al final
print("vacia = ()")
print("len(vacia) =", len(vacia))  # 0

print("singleton = 'hola',")
print("len(singleton) =", len(singleton))  # 1
print("singleton =", singleton)  # ('hola',)

# Crear una tupla de varios elementos
t = 12345, 54321, 'hola!'
print("t = 12345, 54321, hola!")

# La operación inversa: desempacar una tupla
x, y, z = t
print("x, y, z = t")
print("x =", x)
print("y =", y)
print("z =", z)