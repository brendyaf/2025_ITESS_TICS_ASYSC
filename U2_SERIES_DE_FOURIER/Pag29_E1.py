# ITESS TICS
# TI-501
# ANÁLISIS DE SEÑALES Y SISTEMAS DE COMUNICACIONES
# Profesor: Francisco Javier Montecillo Puente
# BRANDY AGUILAR FLORES - brandyaguilar001@gmail.com
# DESCRIPCIÓN: TEMA:Listas por comprensión anidadas. Hace que la expresión de una comprensión 
# de listas sea otra comprensión de listas. Mantiene ejemplos de comprensión anidada, bucles tradicionales
#  y zip() para que se vea lo equivalente.

# matriz de 3x4 implementada como una lista de tres listas de largo 4:
matriz = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],]

#La siguiente comprensión de lista transpondrá las filas y columnas:
[[fila[i] for fila in matriz] for i in range(4)]
#[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# La lista de comprensión anidada se evalua en el contexto del for:
transpuesta = []
for i in range(4):
    transpuesta.append([fila[i] for fila in matriz])
transpuesta
#[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

#Es lo mismo que:
transpuesta = []
for i in range(4):
# las siguientes 3 lineas hacen la comprensión de listas anidada
    fila_transpuesta = []
for fila in matriz:
    fila_transpuesta.append(fila[i])
transpuesta.append(fila_transpuesta)
transpuesta
#[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

#La función zip() haría un buen trabajo para este caso de uso:
list(zip(*matriz))
#[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]




