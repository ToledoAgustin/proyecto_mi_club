"""Punto de entrada del sistema del club.

Cómo correrlo (desde la carpeta del proyecto):
    python main.py

Primero cargá los datos de ejemplo:
    python datos_prueba.py

Usuarios de prueba:
    socio: isaias / clave12333
    admin: admin / admin12333
"""
from pathlib import Path

from base_datos.base_datos import conectar, crear_tablas
from interfaz.app import ClubApp

RUTA_BASE = Path(__file__).parent / "club.db"


def main():
    conexion = conectar(str(RUTA_BASE))
    crear_tablas(conexion)
    conexion.close()

    ClubApp().mainloop()


if __name__ == "__main__":
    main()