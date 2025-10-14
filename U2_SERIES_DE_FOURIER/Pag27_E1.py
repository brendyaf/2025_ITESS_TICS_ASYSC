#ITESS tics
#TI-501
# ANÁLISIS DE SEÑALES Y SISTEMAS DE COMUNICACIONES
# Profesor: Francisco Javier Montecillo Puente
# BRANDY AGUILAR FLORES - brandyaguilar001@gmail.com
# Este script muestra cómo manipular listas en Python usando algunos de sus métodos. 
# Se realizan operaciones para contar, insertar, agregar, buscar, eliminar, invertir,
# ordenar y quitar elementos, mostrando cómo cambia la lista paso a paso.


a = [66.25, 333, 333, 1, 1234.5]
print("a = [66.25, 333, 333, 1, 1234.5]")

print("(a.count(333), a.count(66.25), a.count('x')) =", (a.count(333), a.count(66.25), a.count('x')))
#2 1 0
a.insert(2, -1)
a.append(333)
print("a.insert(2, -1)")
print("a.insert(2, -1)")
print(a)

#[66.25, 333, -1, 333, 1, 1234.5, 333]

print("a.index(333) =", a.index(333))
#1
a.remove(333)
print("a.remove(333)")
print(a)
#[66.25, -1, 333, 1, 1234.5, 333]

a.reverse()
print("a.reverse()")
print(a)
#[333, 1234.5, 1, 333, -1, 66.25]

a.sort()
print("a.sort()")
print(a)
#[-1, 1, 66.25, 333, 333, 1234.5]

a.pop()
print("a.pop()")
#1234.5

print(a)
#[-1, 1, 66.25, 333, 333]
