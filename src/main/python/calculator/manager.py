"""
Módulo que gestiona el funcionamiento
lógico y físico de la aplicación
"""

import tkinter as tk
from constants import style
from screen import *

class Manager(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Calculator")
        container = tk.Frame(self)
        container.pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        container.configure(background = style.BACKGROUND)
        container.grid_columnconfigure(0, weight = 1)
        container.grid_rowconfigure(0, weight = 1)

        # Guardamos los frames en un diccionario para tenerlos a mano
        self.frames = {}
        for F in (Screen, Home):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = tk.NSEW)
        self.show_frame(Screen)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()