import requests
from tkinter import messagebox
import json

def obtener_logs(index, tiempo_dato=False):
    """Obtener logs del servidor Wazuh."""
    
    url = f"https://10.27.20.189:9200/{index}/_search?scroll=1m"
    auth = ("jarellano", "Pass1010.,")  # Credenciales básicas
    headers = {"Content-Type": "application/json"}
    
    if tiempo_dato:
        data = {
            "query": {
                "range": {
                    "@timestamp": {
                        "gte": "now-1m",
                        "lte": "now"
                    }
                }
            },
            "size": 100
        }
    else:
        data = {
            "query": {
                "match_all": {}
            },
            "size": 100
        }
    
    
    try:
        response = requests.get(url, auth=auth, headers=headers, json=data, verify=False)
        if response.status_code == 200:
            logs = response.json()
            with open(f"JSON/{index}.json", "w", encoding="utf-8") as file:
                json.dump(logs, file, indent=4, ensure_ascii=False)
            messagebox.showinfo("Éxito", f"Logs guardados en 'JSON/{index}.json'")
        else:
            messagebox.showerror("Error", f"Error al obtener logs: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo conectar al servidor: {e}")