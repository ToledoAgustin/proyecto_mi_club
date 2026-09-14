import sqlite3

def conectar(ruta):
    conexion = sqlite3.connect(ruta)
    return conexion

def crear_tablas(conexion):
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS socios (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_completo     TEXT NOT NULL,
            edad                INTEGER,
            tipo_identificacion TEXT,
            identificacion      TEXT,
            nacionalidad        TEXT,
            fecha_inscripcion   TEXT,
            estado              TEXT DEFAULT 'Activo',
            rol                 TEXT DEFAULT 'socio',
            usuario             TEXT UNIQUE NOT NULL,
            contrasenia         TEXT NOT NULL
    """)
    conexion.commit()

def guardar_socio(conexion, socio):
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO socios (nombre_completo, edad, tipo_identificacion,identificacion, nacionalidad, fecha_inscripcion,estado, rol, usuario, contrasenia)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        socio.nombre_completo,
        socio.edad,
        socio.get_tipo_identificacion(),
        socio.get_identificacion(),
        socio.get_nacionalidad(),
        socio.fecha_inscripcion.isoformat(),
        socio.estado,
        socio.rol,
        socio.get_usuario(),
        socio.get_contrasenia(),
    ))
    conexion.commit()