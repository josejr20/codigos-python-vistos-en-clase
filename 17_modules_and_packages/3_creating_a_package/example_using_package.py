# Importar módulos desde paquetes ha sido soportado desde Python 1.0.
#
# Nota:
# Desde Python 3.3, una carpeta sin __init__.py puede funcionar como
# namespace package implícito. Sin embargo, si module_a.py y module_b.py
# están en la misma carpeta my_package, este ejemplo representa más bien
# un paquete simple con módulos.

from my_package.module_a import function_a
from my_package.module_b import function_b

print(function_a())  # Salida: Funcion A del modulo a
print(function_b())  # Salida: Funcion B del modulo b