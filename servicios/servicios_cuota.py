from pathlib import Path

from db_miclub.base_datos import (
    conectar,
    listar_cuotas_de_socio,
    pagar_cuota as pagar_cuota_en_bd,
)

RUTA_DB = Path(__file__).parent.parent / "club.db"


def listar_cuotas(usuario):
    """Devuelve la lista de objetos Cuota del socio."""
    conexion = conectar(str(RUTA_DB))
    try:
        return listar_cuotas_de_socio(conexion, usuario)
    finally:
        conexion.close()


def pagar_cuota(usuario, periodo):
    """Registra el pago de la cuota de un socio para el período indicado."""
    conexion = conectar(str(RUTA_DB))
    try:
        return pagar_cuota_en_bd(conexion, usuario, periodo)
    finally:
        conexion.close()