from pathlib import Path

from db_miclub.base_datos import buscar_socio_por_usuario, conectar

RUTA_DB = Path(__file__).parent.parent / "club.db"


def autenticar(usuario, contrasenia):
    """Autentica a un socio por usuario y contraseña. Devuelve el Socio o None."""
    conexion = conectar(str(RUTA_DB))
    try:
        socio = buscar_socio_por_usuario(conexion, usuario)
    finally:
        conexion.close()

    if socio is None:
        return None

    if socio.verificar_acceso(usuario, contrasenia):
        return socio

    return None