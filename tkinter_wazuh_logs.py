import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import requests
import json
import pandas as pd
import sys

print("---------------------------------------------")
print("---------------------------------------------")
print("███████╗███╗---███╗████████╗███████╗ █████╗--")
print("██╔════╝████╗-████║╚══██╔══╝██╔════╝██╔══██╗-")
print("█████╗--██╔████╔██║---██║---█████╗  ██║--╚═╝-")
print("██╔══╝--██║╚██╔╝██║---██║---██╔══╝--██║--██╗-")
print("███████╗██║-╚═╝ ██║---██║---███████╗╚█████╔╝-")
print("╚══════╝╚═╝-----╚═╝---╚═╝---╚══════╝-╚════╝--")
print("--------------------EMTEC--------------------")
print("---------------------------------------------")

print("Comments to: jarellano@soc.cl & ccordero@soc.cl\nversion 1.0\n")

sys.path.append("./functions")

from functions              import *

ventana_login = tk.Tk()
ventana_login.title("Login")
ventana_login.geometry("400x250")
ventana_login.configure(bg="#f0f0f0")

# Guarda la referencia para compartirla con otras funciones
class Data:
    
    root = ventana_login
    ventana_login = ventana_login
    entry_usuario = None
    entry_password = None
    

data = Data()

style = ttk.Style()
style.configure("TLabel", font=("Arial", 12), background="#f0f0f0")
style.configure("TButton", font=("Arial", 10))

# Widgets de la ventana de login
ttk.Label(data.ventana_login, text="Usuario:").grid(row=0, column=0, padx=10, pady=10, sticky="W")
data.entry_usuario = ttk.Entry(data.ventana_login, width=30)
data.entry_usuario.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(data.ventana_login, text="Contraseña:").grid(row=1, column=0, padx=10, pady=10, sticky="W")
data.entry_password = ttk.Entry(data.ventana_login, show="*", width=30)
data.entry_password.grid(row=1, column=1, padx=10, pady=10)

btn_login = ttk.Button(data.ventana_login, text="Login", command=lambda: verificar_login(data))
btn_login.grid(row=2, column=0, columnspan=2, pady=20)

data.root.protocol("WM_DELETE_WINDOW", lambda: confirmar_cierre())


ventana_login.mainloop()