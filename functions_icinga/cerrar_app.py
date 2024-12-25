import sys
from tkinter import messagebox

def exit_app():
    message = messagebox.askyesno("Confirmar cierre", "¿Estás seguro de que deseas cerrar la aplicación?")
    
    if message:
        sys.exit(0)
    else:
        return