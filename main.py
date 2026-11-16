from pathlib import Path

from db_miclub.base_datos import conectar, crear_tablas
from interfaz.app import ClubApp

RUTA_BASE = Path(__file__).parent / "club.db"


def main():
    conexion = conectar(str(RUTA_BASE))
    crear_tablas(conexion)
    conexion.close()

    ClubApp().mainloop()


if __name__ == "__main__":
    main()
