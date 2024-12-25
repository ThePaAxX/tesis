import requests
from tkinter import messagebox
import tkinter as tk
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def obtener_indices(panel):
    """Obtiene y muestra solo los nombres de los índices del servidor Wazuh Indexer."""
    url = "https://10.27.20.189:9200/_cat/indices?v"
    auth = ("jarellano", "Pass1010.,")
    try:
        response = requests.get(url, auth=auth, verify=False)
        if response.status_code == 200:
            indices_data = response.text.splitlines()  # Dividir por líneas
            indices = []

            # Saltar la primera línea (encabezados) y extraer la columna de nombres
            for line in indices_data[1:]:
                parts = line.split()  # Dividir cada línea en columnas
                if len(parts) > 2:  # Asegurarse de que haya suficientes columnas
                    indices.append(parts[2])  # La tercera columna es el nombre del índice

            indices.sort()
            
            # Mostrar los nombres en el cuadro de texto
            panel.text_area.delete(1.0, tk.END)  # Limpiar el cuadro de texto
            panel.text_area.insert(tk.END, "\n".join(indices))  # Mostrar los nombres de los índices
        else:
            messagebox.showerror("Error", f"Error al obtener índices: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo conectar al servidor: {e}")