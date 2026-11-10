from datetime import date
from pathlib import Path

from db_miclub.base_datos import (
    actualizar_estado_socio,
    buscar_socio_por_usuario,
    conectar,
    guardar_socio,
    listar_clubes_de_socio as listar_clubes_en_bd,
    listar_socios as listar_socios_en_bd,
)
from modelo.socio import Socio

RUTA_DB = Path(__file__).parent.parent / "club.db"

def listar_socios():
    conexion = conectar(str(RUTA_DB))
    try:
        return listar_socios_en_bd(conexion)
    finally:
        conexion.close()

def listar_clubes_de_socio(usuario):
    conexion = conectar(str(RUTA_DB))
    try:
        return listar_clubes_en_bd(conexion, usuario)
    finally:
        conexion.close()

def registrar_socio(nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad,
                fecha_inscripcion, estado,rol, usuario, contrasenia):
    # 1. Limpiar los tres textos
    nombre = nombre.strip()
    usuario = usuario.strip()
    identificacion = identificacion.strip()

    # 2. Obligatorios
    if not nombre or not usuario or not contrasenia or not identificacion:
        raise ValueError("Completá todos los campos obligatorios.")
    
  # 3. Edad como número
    try:
        edad = int(edad)
    except (TypeError, ValueError):
        raise ValueError("La edad debe ser un número entero.")

    # 4. Edad negativa
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")

    # 5. Armar el Socio
    socio = Socio(
        nombre,
        edad,
        (tipo_identificacion or "").strip() or None,
        identificacion,
        (nacionalidad or "").strip() or None,
        date.today(),
        "Activo",
        "socio",
        usuario,
        contrasenia,
    )

    # 6. Validar la identificación con el modelo
    if not socio.verificar_identificacion():
        raise ValueError("La identificación no puede estar vacía.")

    # 7. Recién ahora la base de datos
    conexion = conectar(str(RUTA_DB))
    try:
        guardar_socio(conexion, socio)
    finally:
        conexion.close()
    return socio

def suspender_socio(usuario):
    conexion = conectar(str(RUTA_DB))
    try:
        socio = buscar_socio_por_usuario(conexion, usuario)
        if socio is None:
            return "El socio no existe."
        if socio.estado == "Activo":
            actualizar_estado_socio(conexion, usuario, "Suspendido")
            return f"El socio {usuario} fue suspendido."
        return "El socio ya se encuentra suspendido."
    finally:
        conexion.close()

def reactivar_socio(usuario):
    conexion = conectar(str(RUTA_DB))
    try:
        socio = buscar_socio_por_usuario(conexion, usuario)
        if socio is None:
            return "El socio no existe."
        if socio.estado == "Suspendido":
            actualizar_estado_socio(conexion, usuario, "Activo")
            return f"El socio {usuario} fue reactivado."
        return "El socio no necesita reactivación."
    finally:
        conexion.close()