"""
Módulo para realizar las operaciones
"""

import regex as re
import math

class MathOperation():

    def __init__(self, expresion):
        self.validation_pattern = r'-?\d+(?:,\d+)?(?:[\+\-\*/\^%](-?\d+(?:,\d+)?))|√-?\d+(?:,\d+)?'
        self.expresion = expresion