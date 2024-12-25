import sqlite3

# Configuración de la base de datos
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    usuario TEXT UNIQUE,
    password TEXT
)
''')

# Insertar un usuario de prueba
cursor.execute('''
INSERT OR IGNORE INTO usuarios (usuario, password) VALUES (?, ?)
''', ('admin', 'admin123'))

conn.commit()
conn.close()