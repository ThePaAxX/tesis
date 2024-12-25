import tkinter as tk
from tkinter import messagebox
import sys

def confirmar_cierre():
    respuesta = messagebox.askyesno("Confirmar cierre", "¿Estás seguro de que deseas cerrar la aplicación?")
    if respuesta:  # Si el usuario selecciona "Sí"
        
        print('CIERRE EXITOSO')
        sys.exit(1)