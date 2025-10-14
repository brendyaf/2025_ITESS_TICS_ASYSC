# ITESS TICS
# TI-501
# 14/10/2025
# ANÁLISIS DE SEÑALES Y SISTEMAS DE COMUNICACIONES
# Profesor: Francisco Javier Montecillo Puente
# BRANDY AGUILAR FLORES - brandyaguilar001@gmail.com
# DESCRIPCIÓN: Python incluye una biblioteca estándar de módulos, que permite acceder a 
# funcionalidades que no están en el núcleo del lenguaje, como operaciones del sistema operativo 
# o herramientas integradas. El módulo sys es uno de los más importantes, presente en todos los intérpretes

# Las variables sys.ps1 y sys.ps2 definen las cadenas usadas como cursores primarios y secundarios:
import sys

# Mostrar los prompts actuales del intérprete 
print("Prompt primario (sys.ps1):", getattr(sys, 'ps1', 'No definido'))
print("Prompt secundario (sys.ps2):", getattr(sys, 'ps2', 'No definido'))

sys.ps1 = 'C> '  

# Mostrar la ruta actual de búsqueda de módulos
print("\nRutas de búsqueda de módulos (sys.path):")
for ruta in sys.path:
    print(ruta)


# Se puede modificar la ruta usando las operaciones estándar de listas:
print("sys.path.append('/ufs/guido/lib/python')")
sys.path.append('/ufs/guido/lib/python') 
print("for ruta in sys.path: print(ruta)")
for ruta in sys.path:
    print(ruta)

