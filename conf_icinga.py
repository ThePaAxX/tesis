import tkinter as tk
from tkinter import ttk, messagebox
import sys

sys.path.append("./functions-icinga")

from functions_icinga import *

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

class FormConfig:
    def __init__(self):
        self.root = tk.Tk()
        self.frame = ttk.Frame(self.root, padding="10")
        self.entry_host_name = ttk.Entry(self.frame, width=25)
        self.entry_ip = ttk.Entry(self.frame, width=25)
        self.entry_user = ttk.Entry(self.frame, width=25)
        self.entry_password = ttk.Entry(self.frame, width=25, show="*")
        self.combo_type = ttk.Combobox(self.frame, values=["server"], state="readonly", width=22)
        self.combo_os = ttk.Combobox(self.frame, values=["linux", "windows"], state="readonly", width=22)
        self.btn_generate = None


data = FormConfig()

# Crear ventana principal
data.root.title("Generador de Configuración de Host")

# Crear y ubicar widgets
data.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Nombre del host
ttk.Label(data.frame, text="Nombre del Host:").grid(row=0, column=0, sticky=tk.W)
data.entry_host_name.grid(row=0, column=1, pady=5)

# Dirección IP
ttk.Label(data.frame, text="Dirección IP:").grid(row=1, column=0, sticky=tk.W)
data.entry_ip.grid(row=1, column=1, pady=5)

# Usuario
ttk.Label(data.frame, text="Usuario:").grid(row=2, column=0, sticky=tk.W)
data.entry_user.grid(row=2, column=1, pady=5)

# Contraseña
ttk.Label(data.frame, text="Contraseña:").grid(row=3, column=0, sticky=tk.W)
data.entry_password.grid(row=3, column=1, pady=5)

# Tipo
ttk.Label(data.frame, text="Tipo:").grid(row=4, column=0, sticky=tk.W)
data.combo_type.grid(row=4, column=1, pady=5)

# Sistema Operativo
ttk.Label(data.frame, text="Sistema Operativo:").grid(row=5, column=0, sticky=tk.W)
data.combo_os.grid(row=5, column=1, pady=5)

# Botón para generar
data.btn_generate = ttk.Button(data.frame, text="Generar Configuración", command= lambda: generate_config(data))
data.btn_generate.grid(row=6, column=0, columnspan=2, pady=10)

data.root.protocol("WM_DELETE_WINDOW", lambda: exit_app())

data.root.mainloop()
