# TI-501
# 14/10/2025
# ANÁLISIS DE SEÑALES Y SISTEMAS DE COMUNICACIONES
# Profesor: Francisco Javier Montecillo Puente
# BRANDY AGUILAR FLORES - brandyaguilar001@gmail.com
# DESCRIPCIÓN:para leer y escribir archivos se usa open(). Con f.read() 
# se lee todo el contenido, si devuelve una cadena vacía significa que se llegó al final. 
# Con f.readline() se leen líneas una por una, y también se puede recorrer el archivo con 
# un ciclo for.

# Abrir archivo para lectura y escritura
f = open('archivodetrabajo.txt', 'w+')  # 'w+' crea el archivo si no existe y permite leer/escribir

# Escribimos algo en el archivo
f.write("Esta es la primer linea del archivo.\n")
f.write("Segunda linea del archivo\n")
f.seek(0)  # Volvemos al inicio para leer

# Si se alcanzó el fin del archivo
print(f.read())  # Lee todo el archivo
f.seek(0)        # Regresamos al inicio otra vez

# Leer línea por línea
print(f.readline())  # Primera línea
print(f.readline())  # Segunda línea
print(f.readline())  # Fin del archivo, devuelve ''

# Leer línea por línea con for
f.seek(0)
for linea in f:
    print(linea, end='')

# Escribir una nueva línea
f.write('Esto es una prueba\n')

# Escribir una tupla convertida a texto
valor = ('la respuesta', 42)
s = str(valor)
f.write(s)

# Usar seek() para moverse en el archivo
f.seek(0)
print("\nContenido total:\n", f.read())

# Modo binario
f.close()
f = open('archivodetrabajo.txt', 'rb+')
f.write(b'0123456789abcdef')
f.seek(5)
print(f.read(1))  # b'5'
f.seek(-3, 2)
print(f.read(1))  # b'd'

f.close()


