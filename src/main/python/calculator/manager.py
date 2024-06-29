"""
Módulo que gestiona la aplicación y el frame que aparece
"""

import tkinter as tk
from constants import style
from screen import Screen

class Manager(tk.Tk):

    """ Clase generadora de la interfaz """

    def __init__(self, *args, **kwargs):
        """ Método constructor de la clase
        Hereda de la clase tk.Tk """
        super().__init__(*args, **kwargs)
        self.title("Calculator")

        # Contenedor principal
        self.container = tk.Frame(self)
        self.container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Inicializar el frame Screen
        self.screen = Screen(self.container, self)
        self.screen.grid(row=0, column=0, sticky="nsew")

        # Mostrar el frame Screen al iniciar
        self.show_screen()

    def show_screen(self):
        """ Muestra la pantalla """
        self.screen.tkraise()