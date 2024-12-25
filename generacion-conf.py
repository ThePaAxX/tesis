import tkinter as tk
from tkinter import ttk, messagebox

def generate_config():
    host_name = entry_host_name.get()
    ip_address = entry_ip.get()
    username = entry_user.get()
    password = entry_password.get()
    host_type = combo_type.get()
    os_type = combo_os.get()

    if not host_name or not ip_address or not username or not password or not host_type or not os_type:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return

    config_template = f"""
object Host "{host_name}" {{

    import "generic-host"
    import "notification_template_ciberseguridad"

    address = "{ip_address}"
    vars.addresses = ["{ip_address}"]
    vars.username = "{username}"
    vars.password = "{password}"
    check_command = "hostalive"
    display_name = "{host_name}"
    vars.type = "{host_type}"
    vars.os = "{os_type}"
    vars.linux_ssh = true
    vars.location = "1"
    vars.location_code = "1"
    vars.severity = "baja"

    // templates::template_groups
    groups = ["ciberseguridad","server","linux"]

    // templates::template_os
    vars.os = "{os_type}"
    vars.linux = true
    
    // templates::template_protocols
    // templates::template_ssh
    vars.linux_ssh_username = "admin_emtec"
    vars.linux_ssh_password = "3mt3c.4dm"
    
    // templates::template_ssh_linux
    vars.linux_ssh = true
    vars.linux_cpu = true
    vars.linux_disk = true
    vars.linux_load = true
    vars.linux_procs = true
    vars.linux_uptime = true
    vars.linux_users = true
    vars.linux_mem = true
    vars.linux_swap = true

    // templates::thresholds
    vars.hostalive_check_interval = 5m
    vars.hostalive_max_check_attempts = 3
    vars.hostalive_retry_interval = 1m
    vars.disk_warning = "20%"
    vars.disk_critical = "10%"
    vars.disk_check_interval = 5m
    vars.disk_max_check_attempts = 3
    vars.disk_retry_interval = 1m
    vars.cpu_warning = "20%"
    vars.cpu_critical = "25%"
    vars.cpu_check_interval = 5m
    vars.cpu_max_check_attempts = 3
    vars.cpu_retry_interval = 1m
    vars.uptime_warning = "20"
    vars.uptime_critical = "10"
    vars.uptime_check_interval = 5m
    vars.uptime_max_check_attempts = 3
    vars.uptime_retry_interval = 1m
    vars.mem_warning = "20%"
    vars.mem_critical = "10%"
    vars.mem_check_interval = 5m
    vars.mem_max_check_attempts = 3
    vars.mem_retry_interval = 1m
    vars.eventlog_warning = 1
    vars.eventlog_critical = 3
    vars.eventlog_check_interval = 5m
    vars.eventlog_max_check_attempts = 3
    vars.eventlog_retry_interval = 1m
    vars.process_warning = 2
    vars.process_critical = 2
    vars.process_check_interval = 5m
    vars.process_max_check_attempts = 3
    vars.process_retry_interval = 1m


    // template_notificator
    vars.location = "1"
    vars.severity = "Baja"
    vars.notificator.driver.configuration.priority = "Baja"
    vars.impact = "Bajo"
    vars.notificator.driver.configuration.impact = "Bajo"
    vars.notificator.driver.configuration.emails_to_notify = [ "monitoreo@emtecgroup.net" ]
    // Variables para activacion de eg-notify y desactivacion de eg-notificator
    vars.notificator.driver.enabled = false
    vars.eg_notifications.enabled = true
    vars.driver = "MESDP"


    // templates::template_variables
    vars.procs_warning=350
    vars.mem_warning=10
    vars.mem_critical=5
    vars.linux_swap=false

}}
"""

    try:
        with open(f"{host_name}_config.conf", "w") as file:
            file.write(config_template)
        messagebox.showinfo("Éxito", f"Configuración generada exitosamente en {host_name}_config.conf")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al generar el archivo: {e}")

# Crear ventana principal
root = tk.Tk()
root.title("Generador de Configuración de Host")

# Crear y ubicar widgets
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Nombre del host
ttk.Label(frame, text="Nombre del Host:").grid(row=0, column=0, sticky=tk.W)
entry_host_name = ttk.Entry(frame, width=25)
entry_host_name.grid(row=0, column=1, pady=5)

# Dirección IP
ttk.Label(frame, text="Dirección IP:").grid(row=1, column=0, sticky=tk.W)
entry_ip = ttk.Entry(frame, width=25)
entry_ip.grid(row=1, column=1, pady=5)

# Usuario
ttk.Label(frame, text="Usuario:").grid(row=2, column=0, sticky=tk.W)
entry_user = ttk.Entry(frame, width=25)
entry_user.grid(row=2, column=1, pady=5)

# Contraseña
ttk.Label(frame, text="Contraseña:").grid(row=3, column=0, sticky=tk.W)
entry_password = ttk.Entry(frame, width=25, show="*")
entry_password.grid(row=3, column=1, pady=5)

# Tipo
ttk.Label(frame, text="Tipo:").grid(row=4, column=0, sticky=tk.W)
combo_type = ttk.Combobox(frame, values=["server"], state="readonly", width=22)
combo_type.grid(row=4, column=1, pady=5)

# Sistema Operativo
ttk.Label(frame, text="Sistema Operativo:").grid(row=5, column=0, sticky=tk.W)
combo_os = ttk.Combobox(frame, values=["linux", "windows"], state="readonly", width=22)
combo_os.grid(row=5, column=1, pady=5)

# Botón para generar
btn_generate = ttk.Button(frame, text="Generar Configuración", command=generate_config)
btn_generate.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
