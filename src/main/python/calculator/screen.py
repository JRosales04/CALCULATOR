"""
Módulo que maneja el funcionamiento de la interfaz,
visual y lógicamente
"""

import tkinter as tk
from constants import style

class Screen(tk.Frame):

    def __init__(self, parent, controller):
        """Constructor de la clase"""
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.buttons = []
        self.init_widgets()

    def init_widgets(self):
        """Método que inicializa los widgets"""
        self.init_label()
        self.init_buttons()

    def init_label(self):
        """Inicializa la etiqueta de texto"""
        # Crear la etiqueta grande
        self.etiqueta = tk.Label(self, text="", font=("Arial", 20), width=10, height=1, bg="white", fg="black")
        # Configurar la etiqueta en la cuadrícula
        self.etiqueta.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)
        # Configurar la fila 0 para que se expanda
        self.grid_rowconfigure(0, weight=1)
        # Configurar las columnas para que se expandan
        for col in range(4):
            self.grid_columnconfigure(col, weight=1)

    def init_buttons(self):
        """Inicializa los botones"""
        # Crear una matriz de botones de 4x6 (24 botones en total)
        contador = 0
        for i in range(6):
            for j in range(4):
                button = tk.Button(self, text=str(contador), relief="flat", width=1, height=1)
                button.grid(row=i + 1, column=j, sticky="nsew", padx=2, pady=2)
                contador += 1

        # Configurar las filas 1 a 6 para que se expandan
        for row in range(1, 7):
            self.grid_rowconfigure(row, weight=1)