"""
Módulo que maneja el funcionamiento de la interfaz,
visual y lógicamente
"""

import tkinter as tk
import string
from constants import style
from math_operation import MathOperation

class Screen(tk.Frame):

    def __init__(self, parent, controller):
        """Constructor de la clase"""
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.buttons = []
        self.text_label = ""
        self.operation = []
        self.init_widgets()

    def init_widgets(self):
        """Método que inicializa los widgets"""
        self.init_label()
        self.init_buttons()
        self.configure_grid()

    def init_buttons(self):
        """Método que inicializa los botones funcionales"""
        self.init_numbers()
        self.init_operators()
        self.init_clear()
        self.init_equal()

    def init_label(self):
        """Inicializa la etiqueta de texto"""
        # Crear la etiqueta grande
        self.etiqueta = tk.Label(self, text=self.text_label, font=("Arial", 20), width=style.TAMAÑO_ETIQUETA[0],
                           height=style.TAMAÑO_ETIQUETA[1], bg="white", fg="black")
        # Configurar la etiqueta en la cuadrícula
        self.etiqueta.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)
        # Configurar la fila 0 para que se expanda
        self.grid_rowconfigure(0, weight=1)
        # Configurar las columnas para que se expandan
        for col in range(style.COLUMNAS):
            self.grid_columnconfigure(col, weight=1)

    def init_numbers(self):
        """Inicializa los botones para los números"""
        for i in range(len(style.DIGITOS)):
            button = tk.Button(self, text=style.DIGITOS[i], relief="flat", width=style.TAMAÑO_BOTON[0],
                               height=style.TAMAÑO_BOTON[1], command=lambda t=style.DIGITOS[i]: self.write_label(t))
            button.grid(row=style.POSICIONES_NUMEROS[i][0], column=style.POSICIONES_NUMEROS[i][1],
                        sticky="nsew", padx=2, pady=2)
            self.buttons.append(button)

    def init_operators(self):
        """Inicializa los botones para los números"""
        for i in range(len(style.OPERADORES)):
            button = tk.Button(self, text=style.OPERADORES[i], relief="flat", width=style.TAMAÑO_BOTON[0],
                               height=style.TAMAÑO_BOTON[1], command=lambda t=style.OPERADORES[i]: self.define_operation(t))
            button.grid(row=style.POSICIONES_OPERADORES[i][0], column=style.POSICIONES_OPERADORES[i][1],
                        sticky="nsew", padx=2, pady=2)
            self.buttons.append(button)

    def init_clear(self):
        """Inicializa el boton CE"""
        button = tk.Button(self, text="CE", relief="flat", width=style.TAMAÑO_BOTON[0],
                           height=style.TAMAÑO_BOTON[1], command=lambda:self.erase_label())
        button.grid(row=style.POSICION_BORRADOR[0], column=style.POSICION_BORRADOR[1],
                    sticky="nsew", padx=2, pady=2)
        self.buttons.append(button)

    def init_equal(self):
        """Inicializa el boton ="""
        button = tk.Button(self, text="=", relief="flat", width=1, height=1,
                           command=lambda: self.end_operation())
        button.grid(row=style.POSICION_IGUAL[0], column=style.POSICION_IGUAL[1],
                    sticky="nsew", padx=2, pady=2)
        self.buttons.append(button)

    def write_label(self, number):
        """Realiza la función de escribir el número pulsado en la etiqueta"""
        if len(self.text_label) != style.LONGITUD_MAXIMA:
            self.text_label += str(number)
            self.etiqueta.config(text=self.text_label)

    def erase_label(self):
        """Borra el texto de la etiqueta al completo"""
        self.text_label = ""
        self.etiqueta.config(text="")
        self.operation = []
        print(self.operation)

    def define_operation(self, operator):
        """Construye la operación a realizar conforme se pulsan los botones"""
        texto = self.etiqueta.cget("text")
        if texto != "":
            self.operation.append(texto)
            self.operation.append(operator)
        self.text_label = ""
        print(self.operation)

    def end_operation(self):
        """Finaliza la operación a realizar cuando se pulsa '='"""
        last_number = self.text_label
        try:
            self.operation.append(int(last_number))
        except ValueError:
            return False
        print(self.operation)
        self.operate()
        self.erase_label()

    def operate(self):
        return MathOperation(self.operation)

    def configure_grid(self):
        """Configura las columnas para que los botones se expandan (6 filas)"""
        for row in range(style.FILAS):
            self.grid_rowconfigure(row, weight=1)