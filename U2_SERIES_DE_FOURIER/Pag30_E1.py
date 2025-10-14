# ITESS TICS
# TI-501
# 14/10/2025
# ANÁLISIS DE SEÑALES Y SISTEMAS DE COMUNICACIONES
# Profesor: Francisco Javier Montecillo Puente
# BRANDY AGUILAR FLORES - brandyaguilar001@gmail.com
# DESCRIPCIÓN:La instrucción del-> elimina elementos de una lista indicando su posición 
# a diferencia del método pop() que devuelve el valor borrado.
# Se pueden borrar secciones completas de una lista, vaciarla completamente
# o eliminar la variable entera. 

#Lista
a = [-1, 1, 66.25, 333, 333, 1234.5]
print("Lista: a = ", a)

del a[0] # se borra el el primer numero de la lista
print("del a[0]:", a)
#[1, 66.25, 333, 333, 1234.5]

del a[2:4] # Se borran los números en esas posiciones
print("del a[2:4]:", a)
#[1, 66.25, 1234.5]

del a[:] #Se borran todos los numeros de la lista
print("del a[:]:", a)
#[] se vacia toda la lista

#del puede usarse también para eliminar variables:
del a
print("del a:", a)