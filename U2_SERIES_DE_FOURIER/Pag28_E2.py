# ITESS TICS
# TI-501
# 13/10/2025
# ANÁLISIS DE SEÑALES Y SISTEMAS DE COMUNICACIONES
# Profesor: Francisco Javier Montecillo Puente
# BRANDY AGUILAR FLORES - brandyaguilar001@gmail.com
# DESCRIPCIÓN: Este script muestra como usar listas: Listas normales: agregar, eliminar, 
# contar, buscar y ordenar elementos.
# Pilas : append() para agregar, pop() para quitar el último.
# Colas: usar collections.deque con append() y popleft().
# Tiene ejemplos de como se usan y errores.


cuadrados = []
for x in range(10):
    cuadrados.append(x**2)
print("cuadrados = []")
print("for x in range(10): " 
"   cuadrados.append(x**2)")
print(cuadrados)
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Podemos calcular la lista de cuadrados sin ningun efecto secundario haciendo:
cuadrados = list(map(lambda x: x**2, range(10)))
print("cuadrados = list(map(lambda x: x**2, range(10)))")
print(cuadrados )

# o un equivalente:
cuadrados = [x ** 2 for x in range(10)]
print("cuadrados = [x ** 2 for x in range(10)]")
print(cuadrados)

# Esta lista de comprensión combina los elementos de dos listas si no son iguales:
print("[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]")
resultado = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(resultado) 
#[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# Es equivalente a:
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print("combs = [] "
"for x in [1, 2, 3]: "
"   for y in [3, 1, 4]:"
"       if x != y:" 
"           combs.append((x, y))")
print(combs)
#[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# Crear una nueva lista con los valores duplicados
vec = [-4, -2, 0, 2, 4]
print("vec = [-4, -2, 0, 2, 4]")
print("[x*2 for x in vec]")
print([x * 2 for x in vec])
#[-8, -4, 0, 4, 8]

# Filtrar la lista para excluir números negativos
print("[x for x in vec if x >= 0]")
print([x for x in vec if x >= 0])
#[0, 2, 4]

# Aplica una función a todos los elementos
print("[abs(x) for x in vec]")
print([abs(x) for x in vec])
#[4, 2, 0, 2, 4]

# Llama un método a cada elemento
print("frutafresca = [' banana', ' mora de Logan ', 'maracuya ']")
frutafresca = [' banana', ' mora de Logan ', 'maracuya ']
print([arma.strip() for arma in frutafresca])
#['banana', 'mora de Logan', 'maracuya']

# Crea una lista de tuplas de dos como (número, cuadrado)
print("[(x, x ** 2) for x in range(6)]")
print([(x, x ** 2) for x in range(6)])
#[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
# la tupla debe estar entre paréntesis, sino es un error

# Ejemplo de error de sintaxis: olvida los paréntesis en la tupla
# print("[x, x ** 2 for x in range(6)]")
# [x, x ** 2 for x in range(6)]
# Esto produce:
# SyntaxError: invalid syntax

# Aplanar una lista usando comprensión de listas con dos 'for'
print("vec = [[1,2,3], [4,5,6], [7,8,9]]")
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

# Las comprensiones de listas pueden contener expresiones complejas y funciones anidadas:
from math import pi
print("[str(round(pi, i)) for i in range(1, 6)]")
print([str(round(pi, i)) for i in range(1, 6)])
#['3.1', '3.14', '3.142', '3.1416', '3.14159']













