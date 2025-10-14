# ITESS TICS
# TI-501
# ANÁLISIS DE SEÑALES Y SISTEMAS DE COMUNICACIONES
# Profesor: Francisco Javier Montecillo Puente
# BRANDY AGUILAR FLORES - brandyaguilar001@gmail.com
# DESCRIPCIÓN: Usando listas como colas, aqui se muestra cómo usar listas y la clase deque como colas.
# Con el deque se pueden agregar elementos con append() y retirar del frente con popleft().

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry") # llega Terry
queue.append("Graham") # llega Graham
queue.popleft() # el primero en llegar ahora se va
#'Eric'
queue.popleft() # el segundo en llegar ahora se va
#'John'
queue # el resto de la cola en órden de llegada
#['Michael', 'Terry', 'Graham']
