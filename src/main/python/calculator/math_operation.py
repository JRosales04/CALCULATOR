"""
Módulo para realizar las operaciones
"""

import re

class MathOperation():

    """ Lleva a cabo la lógica de las operaciones
    Recibe una operación en una lista y devuelve el resultado de ésta """

    def __init__(self, expresion):
        """ Método constructor de la clase """
        self.validation_pattern = r'^(-?\d+(\.\d+)?([+\-\*/\^%]-?\d+(\.\d+)?)+)$'
        self.expresion = expresion
        self.operation = "".join(str(expr) for expr in expresion)
        self.validate_expression()
        self.result = self.calculate()

    def __str__(self):
        """ Devuelve el resultado de la operación """
        return str(self.result)

    def validate_expression(self):
        """ Compruba que la expresión que se pasa por parámetro cumple el formato válido """
        pattern = re.compile(self.validation_pattern)
        if not pattern.match(self.operation):
            raise ValueError("La expresión no cumple con el formato válido")

    def operate(self, operand1, operator, operand2):
        """ Comparación de operadores para realizar la operación indicada """
        if operator == '+':
            result = float(operand1) + float(operand2)
        elif operator == '-':
            result = float(operand1) - float(operand2)
        elif operator == '*':
            result = float(operand1) * float(operand2)
        elif operator == '/':
            if float(operand2) == 0:
                result = "ERR"
            else:
                result = float(operand1) / float(operand2)
        elif operator == '^':
            result = float(operand1) ** float(operand2)
        elif operator == '%':
            result = float(operand1) % float(operand2)
        if result != "ERR":
            numero = float(result)
            if numero.is_integer():
                return int(numero)
        return result

    def calculate(self):
        """Divide la cadena de operaciones en suboperaciones que va calculando"""
        contador = 0
        while contador < len(self.expresion) - 1:
            if contador == 0:
                operand1 = self.expresion[contador]
            contador += 2
            operand2 = self.expresion[contador]
            operator = self.expresion[contador - 1]
            operand1 = self.operate(operand1, operator, operand2)
        return operand1
