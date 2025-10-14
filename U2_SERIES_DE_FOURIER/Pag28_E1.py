# ITESS TICS
# TI-501
# ANÁLISIS DE SEÑALES Y SISTEMAS DE COMUNICACIONES
# Profesor: Francisco Javier Montecillo Puente
# BRANDY AGUILAR FLORES - brandyaguilar001@gmail.com
# DESCRIPCIÓN: Usando listas como colas, aqui se muestra cómo usar listas y la clase deque como colas.
# Con el deque se pueden agregar elementos con append() y retirar del frente con popleft().

from collections import deque
queue = deque(["Eric", "John", "Michael"])
print("queue = deque(['Eric', 'John', 'Michael'])")
print(deque)

queue.append("Terry") # llega Terry
print("queue.append('Terry')")
queue.append("Graham") # llega Graham
print("queue.append('Graham')")
print(queue)

 # el primero en llegar ahora se va
print("queue.popleft()")
print(queue.popleft()) 
#'Eric'
print("queue.popleft()")
print(queue.popleft()) # el segundo en llegar ahora se va
#'John'
print(queue) # el resto de la cola en órden de llegada
#['Michael', 'Terry', 'Graham']
