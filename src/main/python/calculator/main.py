"""
Módulo main que ejecuta el programa
"""

from manager import Manager

if __name__ == "__main__":
    # Creamos la app
    app = Manager()
    # Ajustamos el tamaño
    app.geometry("300x350")
    # La actualizamos permanentemente
    app.mainloop()