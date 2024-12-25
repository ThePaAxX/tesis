import tkinter as tk
from tkinter import ttk
from .obtener_logs import obtener_logs
from .obtener_indices import obtener_indices
from .csv_alerts import convert_csv_alerts
from .csv_vulne import convert_csv_vulne
from .cierre import confirmar_cierre


class PanelPrincipal:
    def __init__(self, root):
        self.ventana_principal = tk.Toplevel(root)  # Crea una nueva ventana secundaria
        self.entry_index = ttk.Entry(self.ventana_principal, width=40)
        self.btn_logs = ttk.Button(self.ventana_principal, text="Obtener Logs", command=lambda: obtener_logs(self.entry_index.get(), self.check_datos.get()))
        self.btn_indices = ttk.Button(self.ventana_principal, text="Mostrar Índices", command=lambda: obtener_indices(panel))
        self.text_area = tk.Text(self.ventana_principal, wrap=tk.WORD, width=80, height=20, font=("Courier", 10))
        self.btn_json_to_csv_alerts = ttk.Button(self.ventana_principal, text="JSON a CSV Alerts", command=lambda: convert_csv_alerts(self.entry_index.get()))
        self.btn_json_to_csv_vulne = ttk.Button(self.ventana_principal, text="JSON a CSV Vulnerabilidades", command=lambda: convert_csv_vulne(self.entry_index.get()))
        
        self.check_datos = tk.BooleanVar()
        self.btn_check_datos = tk.Checkbutton(self.ventana_principal, text="Ultimos Datos (1 Minuto)", variable=self.check_datos)
        
        self.ventana_principal.protocol("WM_DELETE_WINDOW", lambda: confirmar_cierre())

panel = None

def mostrar_panel_principal(root):
    """Muestra el panel principal tras un login exitoso."""
    global panel
    panel = PanelPrincipal(root)  # Pasa la ventana raíz existente
    panel.ventana_principal.title("Panel Principal")

    # Configurar el tamaño de la ventana
    panel.ventana_principal.geometry("800x600")  # Ancho x Alto
    panel.ventana_principal.configure(bg="#f0f0f0")

    # Estilo de las etiquetas y botones
    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 12), background="#f0f0f0")
    style.configure("TButton", font=("Arial", 10))

    # Widgets del panel principal
    ttk.Label(panel.ventana_principal, text="Index:").grid(row=0, column=0, padx=20, pady=10, sticky="W")
    panel.entry_index.grid(row=0, column=1, padx=20, pady=10)

    panel.btn_logs.grid(row=1, column=0, padx=10, pady=10)
    panel.btn_indices.grid(row=1, column=1, padx=10, pady=10)
    panel.btn_json_to_csv_alerts.grid(row=2, column=0, padx=10, pady=10)
    panel.btn_json_to_csv_vulne.grid(row=2, column=1, padx=10, pady=10)
    panel.btn_check_datos.place(x=610, y=12)

    panel.text_area.grid(row=5, column=0, columnspan=2, padx=20, pady=10)
    panel.text_area.configure(state="normal")
    
    
    
