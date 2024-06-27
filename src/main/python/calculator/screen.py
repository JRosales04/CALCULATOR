"""
Módulo que maneja el funcionamiento de la interfaz,
visual y lógicamente
"""

import tkinter as tk
import string
from constants import style

class Screen(tk.Frame):

    def __init__(self, parent, controller):
        """Constructor de la clase"""
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.buttons = []
        self.text_label = ""
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
                           height=style.TAMAÑO_BOTON[1], command=lambda t=style.DIGITOS[i]: self.write(t))
            button.grid(row=style.POSICIONES_NUMEROS[i][0], column=style.POSICIONES_NUMEROS[i][1],
                        sticky="nsew", padx=2, pady=2)
            self.buttons.append(button)

    def init_operators(self):
        """Inicializa los botones para los números"""
        for i in range(len(style.OPERADORES)):
            button = tk.Button(self, text=style.OPERADORES[i], relief="flat", width=style.TAMAÑO_BOTON[0],
                           height=style.TAMAÑO_BOTON[1], command=None)
            button.grid(row=style.POSICIONES_OPERADORES[i][0], column=style.POSICIONES_OPERADORES[i][1],
                        sticky="nsew", padx=2, pady=2)
            self.buttons.append(button)

    def init_clear(self):
        """Inicializa el boton CE"""
        button = tk.Button(self, text="CE", relief="flat", width=style.TAMAÑO_BOTON[0],
                           height=style.TAMAÑO_BOTON[1], command=lambda:self.erase())
        button.grid(row=style.POSICION_BORRADOR[0], column=style.POSICION_BORRADOR[1],
                    sticky="nsew", padx=2, pady=2)
        self.buttons.append(button)

    def init_equal(self):
        """Inicializa el boton ="""
        button = tk.Button(self, text="=", relief="flat", width=1, height=1, command=None)
        button.grid(row=style.POSICION_IGUAL[0], column=style.POSICION_IGUAL[1],
                    sticky="nsew", padx=2, pady=2)
        self.buttons.append(button)

    def write(self, text):
        """Realiza la función de escribir en la etiqueta al pulsar un botón"""
        if len(self.text_label) != style.LONGITUD_MAXIMA:
            self.text_label += str(text)
            self.etiqueta.config(text=self.text_label)

    def erase(self):
        """Borra el texto de la etiqueta al completo"""
        self.etiqueta.config(text="")
        self.text_label = ""

    def configure_grid(self):
        """Configura las columnas para que los botones se expandan (6 filas)"""
        for row in range(style.FILAS):
            self.grid_rowconfigure(row, weight=1)