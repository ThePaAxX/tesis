import json
import pandas as pd
from tkinter import messagebox

def convert_csv_alerts(index):
    try:
        # Cargar el archivo JSON
        with open(f'JSON/{index}.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Extraer los datos relevantes de 'hits.hits'
        hits = data["hits"]["hits"]

        # Aplanar los datos relevantes de cada registro
        flattened_data = []
        for hit in hits:
            source = hit["_source"]
            flattened_data.append(
                {
                    "agent_id":      source["agent"]["id"],
                    "agent_name":    source["agent"]["name"],
                    "nivel_critico": source["rule"]["level"],
                    "descripcion":   source["rule"]["description"],
                    "location":      source["location"],
                    "tiempo":        source["timestamp"],
                    
                }
            )

        # Convertir la lista de diccionarios a DataFrame
        df = pd.DataFrame(flattened_data)

        # Exportar a CSV
        df.to_csv(f'CSV/{index}.csv', index=False, encoding='utf-8')

        messagebox.showinfo("Éxito", f"Archivo CSV guardado en 'CSV/{index}.csv'")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo generar el archivo CSV: {e}")
