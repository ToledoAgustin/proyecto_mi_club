# from modelo.persona import Persona
# from modelo.socio import Socio
# from modelo.club import Club
# from modelo.cuota import Cuota
# from modelo.actividad import Actividad

# # ----------------------------------------------------------------
# # Pruebas de Persona
# # ----------------------------------------------------------------
# print("=== PERSONA ===")
# persona1 = Persona("Maxi Jackson", 10, "DNI", "12345678", "Peru")
# print(persona1.mostrar_datos())

# persona2 = Persona("Santi Pérez", 15, "DNI", "", "Uruguay")
# print(persona2.mostrar_datos())


# # ----------------------------------------------------------------
# # Pruebas de Club
# # ----------------------------------------------------------------
# print("=== CLUB ===")
# club1 = Club("9 de julio Rafaela", "Club de fútbol", "Santa Fe", "Lucas Astrada", "09/07/1904")
# club2 = Club("Inter Miami", "Club de la MLS", "Miami", "David Beckham", "09/12/2018")

# print(club1.set_presidente("Juan Román Riquelme"))
# print(club1.mostrar_info())
# print(club2.mostrar_info())


# # ----------------------------------------------------------------
# # Pruebas de Socio (ya con club1 y club2 creados arriba)
# # ----------------------------------------------------------------
# print("=== SOCIO ===")
# socio1 = Socio("Matias Galarza Borja", 20, "DNI", "49903017", "Argentina", "23/02/2026", "Activo", "MatiCABJ", "MATIAS2011")

# print(socio1.agregar_club(club1))
# print(socio1.agregar_club(club2))
# print(socio1.mostrar_clubes())

# print(socio1.dar_baja_club(club2))
# print(socio1.mostrar_clubes())

# print(socio1.generar_cuota("Agosto 2026", 15000))
# print(socio1.generar_cuota("Septiembre 2026", 15000))
# print(socio1.mostrar_cuotas())
# print(socio1.tiene_deudas())
# print(socio1.cantidad_cuotas_pendientes())

# print(socio1.pagar_cuota("Agosto 2026"))
# print(socio1.tiene_deudas())
# print(socio1.cantidad_cuotas_pendientes())

# print(socio1.suspender())
# print(socio1.reactivar())

# print(socio1.verificar_acceso("MatiCABJ", "MATIAS2011"))
# print(socio1.verificar_acceso("MatiCABJ", "clave_erronea"))
# print(socio1.cambiar_contrasenia("MATIAS2011", "nuevaClave456"))
# print(socio1.verificar_acceso("MatiCABJ", "nuevaClave456"))

# print(socio1.mostrar_datos())
# print(socio1.es_administrador())


# # ----------------------------------------------------------------
# # Pruebas de Cuota
# # ----------------------------------------------------------------
# print("=== CUOTA ===")

# # Cuota vencida (fecha pasada, sin pagar)
# cuota1 = Cuota("Pendiente", "25/09/2026", "Septiembre 2026")
# print(cuota1.mostrar_cuota())
# print("¿Está vencida?", cuota1.esta_vencida())
# print(cuota1.dias_para_vencimiento())
# print(cuota1.actualizar_estado())
# print(cuota1.mostrar_cuota())


# # Cuota que aún no vence
# cuota2 = Cuota("Pendiente", "30/12/2026", "Diciembre 2026")
# print(cuota2.mostrar_cuota())
# print("¿Está vencida?", cuota2.esta_vencida())
# print(cuota2.dias_para_vencimiento())
# print(cuota2.actualizar_estado())
# print(cuota2.mostrar_cuota())


# # Registrar pago y renovar
# print(cuota2.registrar_pago())
# print(cuota2.mostrar_cuota())
# print(cuota2.renovar("Enero 2027", "31/01/2027"))
# print(cuota2.mostrar_cuota())


# # ----------------------------------------------------------------
# # Pruebas de Actividad
# # ----------------------------------------------------------------
# print("=== ACTIVIDAD ===")
# actividad1 = Actividad("Fútbol infantil", "Martes y Jueves", "18:00 - 19:30")
# print(actividad1.mostrar_info())

import sqlite3
from datetime import date
from pathlib import Path

from db_miclub.base_datos import (
    anotar_socio_actividad,
    asociar_socio_club,
    buscar_socio_por_usuario,
    conectar,
    crear_tablas,
    desanotar_socio_actividad,
    guardar_actividad,
    guardar_club,
    guardar_cuota,
    guardar_socio,
    listar_actividades_de_socio,
)
from modelo.actividad import Actividad
from modelo.club import Club
from modelo.cuota import Cuota
from modelo.socio import Socio
from servicios.servicio_autenticacion import autenticar
from servicios.servicios_cuota import listar_cuotas, pagar_cuota
from servicios.servicios_socios import (
    listar_clubes_de_socio,
    listar_socios,
    obtener_socio,
    reactivar_socio,
    registrar_socio,
    suspender_socio,
)

RUTA = Path(__file__).parent / "club.db"

# Si la base previa existe, la borra para que las pruebas arranquen limpias
if RUTA.exists():
    RUTA.unlink()

conexion = conectar(str(RUTA))
crear_tablas(conexion)

# ── Socios ----------------------------------------------------------

bubu = Socio("bubuzela_bubu", 24, "dni", 42890413, "argentino", date(2026, 1, 1), "Activo", "socio", "bubu124", "bubu0707")
guardar_socio(conexion, bubu)

messi = Socio("lionel_messi", 38, "dni", 33000001, "argentino", date(2026, 1, 5), "Activo", "socio", "messi10", "campeon2022")
guardar_socio(conexion, messi)

shakira = Socio("shakira_mebarak", 49, "dni", 33000002, "colombiana", date(2026, 1, 10), "Activo", "socio", "shaki77", "waka2010")
guardar_socio(conexion, shakira)

maradona = Socio("diego_maradona", 60, "dni", 33000003, "argentino", date(2026, 1, 15), "Suspendido", "socio", "diego10", "manodedios")
guardar_socio(conexion, maradona)

tini = Socio("tini_stoessel", 29, "dni", 33000004, "argentino", date(2026, 2, 1), "Activo", "admin", "tini_adm", "tini2026")
guardar_socio(conexion, tini)

bichota = Socio("karol_g", 35, "dni", 33000005, "colombiana", date(2026, 2, 10), "Activo", "admin", "karol_adm", "bichota01")
guardar_socio(conexion, bichota)

cr7 = Socio("cristiano_ronaldo", 41, "dni", 33000006, "portugues", date(2026, 2, 20), "Activo", "socio", "cr7siuu", "elbicho7")
guardar_socio(conexion, cr7)

carlito = Socio("carlito_bala", 30, "dni", 38456721, "argentino", date(2026, 2, 15), "Activo", "socio", "carlito99", "bala1234")
guardar_socio(conexion, carlito)

print("8 socios guardados.")

# ── Cuotas ----------------------------------------------------------

cuota1 = Cuota("Pendiente", date(2026, 10, 10), "Octubre 2026")
guardar_cuota(conexion, bubu, cuota1)

cuota2 = Cuota("Pendiente", date(2026, 10, 10), "Octubre 2026")
guardar_cuota(conexion, carlito, cuota2)

cuota4 = Cuota("Pendiente", date(2026, 10, 10), "Octubre 2026")
guardar_cuota(conexion, carlito, cuota4)

cuota5 = Cuota("Pagada", date(2026, 10, 10), "Octubre 2026")
guardar_cuota(conexion, messi, cuota5)

cuota6 = Cuota("Vencida", date(2026, 9, 10), "Septiembre 2026")
guardar_cuota(conexion, shakira, cuota6)

cuota7 = Cuota("Pendiente", date(2026, 11, 10), "Noviembre 2026")
guardar_cuota(conexion, shakira, cuota7)

cuota8 = Cuota("Vencida", date(2026, 8, 10), "Agosto 2026")
guardar_cuota(conexion, maradona, cuota8)

cuota9 = Cuota("Pagada", date(2026, 10, 10), "Octubre 2026")
guardar_cuota(conexion, cr7, cuota9)

cuota10 = Cuota("Pagada", date(2026, 9, 10), "Septiembre 2026")
guardar_cuota(conexion, cr7, cuota10)

print("Cuotas guardadas.")

# ── Clubes y asociaciones -------------------------------------------

club = Club("9 de julio Rafaela", "Club de fútbol", "Santa Fe", "Lucas Astrada", "09/07/1904")
guardar_club(conexion, club)

club2 = Club("Atlético de Rafaela", "Club de fútbol", "Santa Fe", "Pedro Gómez", "12/05/1907")
guardar_club(conexion, club2)

club3 = Club("Racing de Avellaneda", "Club de fútbol", "Buenos Aires", "Diego Milito", "25/03/1903")
guardar_club(conexion, club3)

club4 = Club("Club Atlético Colón", "Club de fútbol", "Santa Fe", "Germán Lerche", "05/05/1905")
guardar_club(conexion, club4)

club5 = Club("Club Atlético Newell's Old Boys", "Club de fútbol", "Santa Fe", "Ignacio Boero", "03/11/1903")
guardar_club(conexion, club5)

club6 = Club("Club Atlético Belgrano", "Club de fútbol", "Córdoba", "Jorge Franceschi", "19/03/1905")
guardar_club(conexion, club6)

asociar_socio_club(conexion, "bubu124", "9 de julio Rafaela")
asociar_socio_club(conexion, "carlito99", "Atlético de Rafaela")
asociar_socio_club(conexion, "messi10", "Racing de Avellaneda")
asociar_socio_club(conexion, "messi10", "Club Atlético Newell's Old Boys")
asociar_socio_club(conexion, "shaki77", "Club Atlético Colón")
asociar_socio_club(conexion, "diego10", "Club Atlético Belgrano")
asociar_socio_club(conexion, "diego10", "Racing de Avellaneda")
asociar_socio_club(conexion, "cr7siuu", "9 de julio Rafaela")
asociar_socio_club(conexion, "cr7siuu", "Atlético de Rafaela")
asociar_socio_club(conexion, "cr7siuu", "Club Atlético Colón")

print("Clubes y asociaciones guardados.")

# ── Actividades -----------------------------------------------------

actividades = [
    Actividad("Fútbol", "Martes", "18:00"),
    Actividad("Natación", "Jueves", "10:00"),
    Actividad("Básquet", "Lunes", "19:00"),
    Actividad("Tenis", "Miércoles", "17:00"),
    Actividad("Vóley", "Viernes", "20:00"),
    Actividad("Yoga", "Sábado", "09:00"),
    Actividad("Gimnasio", "Lunes", "08:00"),
    Actividad("Rugby", "Domingo", "16:00"),
]
for act in actividades:
    guardar_actividad(conexion, act)

anotar_socio_actividad(conexion, "bubu124", "Fútbol")
anotar_socio_actividad(conexion, "bubu124", "Natación")
anotar_socio_actividad(conexion, "messi10", "Fútbol")
anotar_socio_actividad(conexion, "messi10", "Tenis")
anotar_socio_actividad(conexion, "shaki77", "Yoga")
anotar_socio_actividad(conexion, "diego10", "Fútbol")
anotar_socio_actividad(conexion, "diego10", "Básquet")
anotar_socio_actividad(conexion, "cr7siuu", "Fútbol")
anotar_socio_actividad(conexion, "cr7siuu", "Gimnasio")
anotar_socio_actividad(conexion, "cr7siuu", "Natación")
desanotar_socio_actividad(conexion, "bubu124", "Natación")

# Cerramos la conexión de carga antes de probar los servicios
conexion.close()
print("Base de prueba creada.\n")

# ── Pruebas de servicios (UC-01 a UC-07) ────────────────────────────

# UC-01: Autenticación
socio = autenticar("bubu124", "bubu0707")
assert socio is not None and socio.rol == "socio"
assert autenticar("bubu124", "clave_mala") is None
assert autenticar("usuario_fantasma", "bubu0707") is None
print("UC-01 autenticación: OK")

# UC-02: Datos y clubes del socio
assert obtener_socio("bubu124") is not None
clubes = listar_clubes_de_socio("bubu124")
assert len(clubes) == 1 and clubes[0].nombre == "9 de julio Rafaela"
assert listar_clubes_de_socio("tini_adm") == []
print("UC-02 datos y clubes: OK")

# UC-03: Listar cuotas
assert len(listar_cuotas("bubu124")) == 1
print("UC-03 listar cuotas: OK")

# UC-04: Pagar cuota
assert "pagada" in pagar_cuota("bubu124", "Octubre 2026").lower()
print("UC-04 pagar cuota: OK")

# UC-05: Listar socios
assert len(listar_socios()) == 8
print("UC-05 listar socios: OK")

# UC-06: Registrar socio (con 10 parámetros) y validar duplicado
registrar_socio(
    "Nuevo Socio", "20", "DNI", "99999999", "Argentina",
    date.today(), "Activo", "socio", "nuevo", "clave999"
)
assert obtener_socio("nuevo") is not None
try:
    registrar_socio(
        "Otro", "20", "DNI", "88888888", "Argentina",
        date.today(), "Activo", "socio", "nuevo", "x"
    )
    raise AssertionError("No debería permitir un usuario repetido")
except (ValueError, sqlite3.IntegrityError):
    pass
print("UC-06 registrar socio: OK")

# UC-07: Suspender y reactivar
assert "suspendido" in suspender_socio("bubu124").lower()
assert obtener_socio("bubu124").estado == "Suspendido"
assert "suspendido" in suspender_socio("bubu124").lower()
assert "reactivado" in reactivar_socio("bubu124").lower()
assert obtener_socio("bubu124").estado == "Activo"
assert "reactivación" in reactivar_socio("bubu124")
print("UC-07 suspender/reactivar: OK")

print("\nTodas las pruebas de servicios pasaron.")