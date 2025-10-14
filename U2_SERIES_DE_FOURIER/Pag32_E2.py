# ITESS TICS
# TI-501
# 14/10/2025
# ANÁLISIS DE SEÑALES Y SISTEMAS DE COMUNICACIONES
# Profesor: Francisco Javier Montecillo Puente
# BRANDY AGUILAR FLORES - brandyaguilar001@gmail.com
# DESCRIPCIÓN: Este script muestra como usar diccionarios en Python: 
# guardar valores con claves únicas, acceder a ellos, borrarlos, hacer listas, 
# verificar si existen valores y crear diccionarios de varias formas.


# Crear un diccionario 
tel = {'jack': 4098, 'sape': 4139}
print("tel =", tel)
tel['guido'] = 4127 # Agregar uno nuevo
print("tel['guido']")
print(tel)
print("tel['jack'] =", tel['jack'])
del tel['sape'] # Borrar uno
print("del tel['sape']:") 
print(tel)
tel['irv'] = 4127 #Agregar otro nuevo
print("tel['irv'] = 4127")
print(tel)
print("list(tel.keys()) =", list(tel.keys()))
print("sorted(tel.keys()) =", sorted(tel.keys()))

#Verifica si estan o no
print("'guido' in tel:", 'guido' in tel)
print("'jack' not in tel:", 'jack' not in tel)

# El constructor dict() crea un diccionario directamente desde secuencias de pares clave-valor:
dic = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print("dic =", dic)

# las comprensiones de diccionarios se pueden usar para crear diccionarios desde expresiones arbitrarias 
# de clave y valor:
comp = {x: x ** 2 for x in (2, 4, 6)}
print("{x: x ** 2 for x in (2,4,6)} =", comp)

# Cuando las claves son cadenas simples, a veces resulta más fácil especificar los pares usando argumentos
# por palabra clave:
dic2 = dict(sape=4139, guido=4127, jack=4098)
print("dict(sape=4139, guido=4127, jack=4098) =", dic2)

