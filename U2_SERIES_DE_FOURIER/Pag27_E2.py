# ITESS TICS
# TI-501
# ANÁLISIS DE SEÑALES Y SISTEMAS DE COMUNICACIONES
# Profesor: Francisco Javier Montecillo Puente
# BRANDY AGUILAR FLORES - brandyaguilar001@gmail.com
# DESCRIPCIÓN: Usando listas como pilas, aqui se muestra como usar listas en Python como 
# pilas, se utilizan los métodos append() para agregar elementos a la cima de la pila
# y pop() para retirar elementos de la cima.

stack = [3, 4, 5]
stack.append(6)
stack.append(7)

print("stack = [3, 4, 5]")
print("stack.append(6)")
print("stack.append(7)")
print(stack)  # [3, 4, 5, 6, 7]

print("stack.pop()")
print(stack.pop())  # 7
print(stack)      # [3, 4, 5, 6]

print("stack.pop()")
print(stack.pop())  # 6
print("stack.pop()")
print(stack.pop())  # 5
print(stack)     # [3, 4]
