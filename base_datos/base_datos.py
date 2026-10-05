import sqlite3
from datetime import date
from modelo.cuota import Cuota
from modelo.socio import Socio

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
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cuotas (
            id                          INTEGER PRIMARY KEY AUTOINCREMENT,
            socio_id                    INTEGER NOT NULL,
            estado                      TEXT DEFAULT 'Pendiente',
            fecha_de_vencimiento        DATE,
            periodo                     TEXT,
            FOREIGN KEY (socio_id) REFERENCES socios(id)
        )
    """)

    def crear_tablas(conexion):
        cursor = conexion.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS clubes (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre          TEXT NOT NULL UNIQUE,
            descripcion     TEXT,
            ubicacion       TEXT,
            presidente      TEXT,
            fecha_fundacion TEXT
        )
    """)

                   

    conexion.commit()

def guardar_socio(conexion, socio):
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO socios (nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad, fecha_inscripcion, estado, rol, usuario, contrasenia)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        socio.nombre_completo,
        socio.edad,
        socio.get_tipo_identificacion(),
        socio.get_identificacion(),
        socio.get_nacionalidad(),
        socio.fecha_inscripcion.isoformat() if hasattr(socio.fecha_inscripcion, 'isoformat') else str(socio.fecha_inscripcion),
        socio.estado,
        socio.rol,
        socio.get_usuario(),
        socio.get_contrasenia(),
    ))
    conexion.commit()

def buscar_socio_por_usuario(conexion, usuario):
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT id, nombre_completo, edad, tipo_identificacion, identificacion, 
               nacionalidad, fecha_inscripcion, estado, usuario, contrasenia, rol 
        FROM socios 
        WHERE usuario = ?
    """, (usuario,))
    fila = cursor.fetchone()
    if fila is None:
        return  objeto_socio()
    
def objeto_socio(fila):
    (_id, nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad, fecha_inscripcion,     estado, usuario, contrasenia, rol) = fila
    return  Socio(nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad, fecha_inscripcion,estado, usuario, contrasenia, rol)

def guardar_cuota(conexion, socio, cuota):
    cursor = conexion.cursor()
    # Busca al socio por su ID numérico o por su usuario
    cursor.execute("SELECT id FROM socios WHERE usuario = ?", (socio.get_usuario(),))
    fila = cursor.fetchone()
    
    if fila is None:
        raise ValueError("El socio no existe")
    
    socio_id_real = fila[0]
    cursor.execute("""
        INSERT INTO cuotas (socio_id, estado, fecha_de_vencimiento, periodo)
        VALUES (?, ?, ?, ?)
    """, (
        socio_id_real,
        cuota.get_estado(),
        cuota.fecha_de_vencimiento,
        cuota.periodo
    ))
    conexion.commit()

def listar_cuotas_de_socio(conexion, usuario):
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM socios WHERE usuario = ?", (usuario,))
    fila = cursor.fetchone()
    if fila is None:
        return []
    socio_id = fila[0]

    cursor.execute(
        "SELECT estado, fecha_de_vencimiento, periodo FROM cuotas WHERE socio_id = ?",
        (socio_id,)
    )
    cuotas = []
    for estado, fecha_vencimiento, periodo in cursor.fetchall():
        fecha_obj = date.fromisoformat(fecha_vencimiento) if isinstance(fecha_vencimiento, str) else fecha_vencimiento
        cuota = Cuota(estado, fecha_obj, periodo)
        cuotas.append(cuota)
    return cuotas