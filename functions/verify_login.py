from tkinter import messagebox
import sqlite3
from .panel_principal import mostrar_panel_principal

def verificar_login(data):
    """Verifica el login contra la base de datos SQLite."""
    usuario = data.entry_usuario.get()
    password = data.entry_password.get()

    # Conexion a la base de datos
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE usuario=? AND password=?", (usuario, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        messagebox.showinfo("Éxito", "Login exitoso")
        data.ventana_login.withdraw()  # Oculta la ventana en lugar de destruirla
        mostrar_panel_principal(data.ventana_login)  # Pasa la raíz
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")
