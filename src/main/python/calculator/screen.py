"""
Módulo que maneja el funcionamiento de la interfaz,
visual y lógicamente
"""

# Importación de módulos
import tkinter as tk
from constants import style
from math_operation import MathOperation

class Screen(tk.Frame):

    """ Maneja la interfaz de la calculadora
    Hereda de la clase tk.Frame """

    def __init__(self, parent, controller):
        """ Método constructor de la clase """
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.buttons = []
        self.text_label = ""
        self.operation = []
        self.init_widgets()

    def init_widgets(self):
        """ Inicializa los widgets y los posiciona en la pantalla """
        self.init_label()
        self.init_buttons()
        self.configure_grid()

    def init_label(self):
        """ Inicializa la etiqueta donde aparecerán los números """
        self.etiqueta = tk.Label(self,
                                 text=self.text_label,
                                 font=style.FORMATO_LETRA,
                                 width=style.TAMAÑO_ETIQUETA[0],
                                 height=style.TAMAÑO_ETIQUETA[1],
                                 bg="white",
                                 fg="black")
        self.etiqueta.grid(row=0,
                           column=0,
                           columnspan=4,
                           sticky="nsew",
                           padx=style.PADDING,
                           pady=style.PADDING)
        self.grid_rowconfigure(0, weight=1)
        for col in range(style.COLUMNAS):
            self.grid_columnconfigure(col, weight=1)

    def init_buttons(self):
        """ Inicializa el conjunto de botones funcionales """
        self.init_numbers()
        self.init_operators()
        self.init_clear()
        self.init_eraser()
        self.init_equal()

    def init_numbers(self):
        """ Inicializa los botones de los dígitos """
        for i in range(len(style.DIGITOS)):
            button = tk.Button(self,
                               text=style.DIGITOS[i],
                               font=style.FORMATO_LETRA,
                               relief="flat",
                               width=style.TAMAÑO_BOTON[0],
                               height=style.TAMAÑO_BOTON[1],
                               command=lambda t=style.DIGITOS[i]: self.write_label(t))
            button.grid(row=style.POSICIONES_NUMEROS[i][0],
                        column=style.POSICIONES_NUMEROS[i][1],
                        sticky="nsew",
                        padx=style.PADDING,
                        pady=style.PADDING)
            self.buttons.append(button)

    def init_operators(self):
        """ Inicializa los botones de los operadores """
        for i in range(len(style.OPERADORES)):
            button = tk.Button(self,
                               text=style.OPERADORES[i],
                               font=style.FORMATO_LETRA,
                               relief="flat",
                               width=style.TAMAÑO_BOTON[0],
                               height=style.TAMAÑO_BOTON[1],
                               command=lambda t=style.OPERADORES[i]: self.define_operation(t))
            button.grid(row=style.POSICIONES_OPERADORES[i][0],
                        column=style.POSICIONES_OPERADORES[i][1],
                        sticky="nsew",
                        padx=style.PADDING,
                        pady=style.PADDING)
            self.buttons.append(button)

    def init_clear(self):
        """ Inicializa el boton de borrar el texto de la etiqueta """
        button = tk.Button(self,
                           text="CE",
                           font=style.FORMATO_LETRA,
                           relief="flat",
                           width=style.TAMAÑO_BOTON[0],
                           height=style.TAMAÑO_BOTON[1],
                           command=lambda:self.erase_label())
        button.grid(row=style.POSICION_BORRADOR_COMPLETO[0],
                    column=style.POSICION_BORRADOR_COMPLETO[1],
                    sticky="nsew",
                    padx=style.PADDING,
                    pady=style.PADDING)
        self.buttons.append(button)

    def init_eraser(self):
        """ Inicializa el boton de borrado simple """
        button = tk.Button(self,
                           text="⌫",
                           font=style.FORMATO_LETRA,
                           relief="flat",
                           width=style.TAMAÑO_BOTON[0],
                           height=style.TAMAÑO_BOTON[1],
                           command=lambda: self.erase_number())
        button.grid(row=style.POSICION_BORRADOR_SIMPLE[0],
                    column=style.POSICION_BORRADOR_SIMPLE[1],
                    sticky="nsew",
                    padx=style.PADDING,
                    pady=style.PADDING)
        self.buttons.append(button)

    def init_equal(self):
        """ Inicializa el boton del simbolo = """
        button = tk.Button(self,
                           text="=",
                           font=style.FORMATO_LETRA,
                           relief="flat",
                           width=1,
                           height=1,
                           command=lambda: self.calculate())
        button.grid(row=style.POSICION_IGUAL[0],
                    column=style.POSICION_IGUAL[1],
                    sticky="nsew",
                    padx=style.PADDING,
                    pady=style.PADDING)
        self.buttons.append(button)

    def write_label(self, number):
        """ Método para escribir en la etiqueta """
        if len(self.text_label) != style.LONGITUD_MAXIMA:
            self.text_label += str(number)
            self.etiqueta.config(text=self.text_label)

    def erase_label(self):
        """ Método para borrar el texto de la etiqueta al completo """
        self.text_label = ""
        self.etiqueta.config(text="")
        self.operation = []

    def erase_number(self):
        """ Método para borrar el último número escrito en la etiqueta """
        texto = self.etiqueta.cget("text")
        if len(texto) == 0:
            self.etiqueta.config(text=texto)
        else:
            self.etiqueta.config(text=texto[:-1])
            self.text_label = self.text_label[:-1]

    def define_operation(self, operator):
        """ Método para armar la operación a realizar """
        texto = self.etiqueta.cget("text")
        if texto != "":
            self.operation.append(texto)
            self.operation.append(operator)
        self.text_label = ""

    def calculate(self):
        """ Método para calcular la operación a realizar y mostrarla en la etiqueta """
        last_number = self.text_label
        if last_number != "":
            self.operation.append(last_number)
        try:
            result = MathOperation(self.operation)
            self.text_label = str(result)
            self.etiqueta.config(text=self.text_label)
        except ValueError as exception:
            self.text_label = str(exception)
            self.etiqueta.config(text=self.text_label)

    def configure_grid(self):
        """ Método para ordenar los botones en la pantalla """
        for row in range(style.FILAS):
            self.grid_rowconfigure(row, weight=1)
