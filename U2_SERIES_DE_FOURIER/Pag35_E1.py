# ITESS TICS
# TI-501
# 14/10/2025
# ANÁLISIS DE SEÑALES Y SISTEMAS DE COMUNICACIONES
# Profesor: Francisco Javier Montecillo Puente
# BRANDY AGUILAR FLORES - brandyaguilar001@gmail.com
# DESCRIPCIÓN:Uso de operadores lógicos para obtener el primer valor no vacío.
# Las condiciones usadas en las instrucciones while e if pueden contener cualquier operador, no sólo comparaciones.
# Los operadores de comparación in y not in verifican si un valor está o no.
# Los operadores booleanos and y or son los llamados operadores cortocircuito: sus argumentos se evalúan de izquierda a
# derecha, y la evaluación se detiene en el momento en que se determina su resultado.

#Es posible asignar el resultado de una comparación u otra expresión booleana a una variable:
cadena1, cadena2, cadena3 = '', 'Trondheim', 'Paso Hammer'
non_nulo = cadena1 or cadena2 or cadena3

print(non_nulo)  # Muestra: Trondheim