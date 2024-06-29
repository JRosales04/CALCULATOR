"""
Módulo que almacena las constantes del proyecto
"""

import string

# Tamaño de la matriz de widgets
FILAS = 6
COLUMNAS = 4

# Longitud de número máxima
LONGITUD_MAXIMA = 15

BACKGROUND = "#084050"

# Lista de dígitos numéricos
digitos_numericos = list(string.digits)
DIGITOS = digitos_numericos + ["."]

# Lista de operadores
OPERADORES = ["+", "-", "*", "/", "^", "%"]

# Tamaño de los widgets
TAMAÑO_BOTON = (1,1)
TAMAÑO_ETIQUETA = (10,2)

# Listas de tuplas para las posiciones de los botones
POSICIONES_NUMEROS = [(5,1), (4,0), (4,1), (4,2), (3,0), (3,1), (3,2), (2,0), (2,1), (2,2), (5,0)]
POSICIONES_OPERADORES = [(2,3), (3,3), (4,3), (5,3), (1,0), (1,1)]
POSICION_IGUAL = (5,2)
POSICION_BORRADOR_SIMPLE = (1,3)
POSICION_BORRADOR_COMPLETO = (1,2)

# Estilo para el formato de la interfaz
FORMATO_LETRA = ("Consolas", 15)
PADDING = 2