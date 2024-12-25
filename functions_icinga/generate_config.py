from tkinter import messagebox

def generate_config(data):
    host_name = data.entry_host_name.get()
    ip_address = data.entry_ip.get()
    username = data.entry_user.get()
    password = data.entry_password.get()
    host_type = data.combo_type.get()
    os_type = data.combo_os.get()

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
        with open(f"CONF-ICINGA/{host_name}.conf", "w") as file:
            file.write(config_template)
        messagebox.showinfo("Éxito", f"Configuración generada exitosamente en {host_name}_config.conf")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al generar el archivo: {e}")