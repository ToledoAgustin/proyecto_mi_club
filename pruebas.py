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


from datetime import date
from pathlib import Path
from db_miclub.base_datos import conectar, crear_tablas, guardar_socio, buscar_socio_por_usuario, guardar_cuota, listar_cuotas_de_socio, guardar_club, guardar_actividad, anotar_socio_actividad, listar_actividades_de_socio, desanotar_socio_actividad, asociar_socio_club, listar_clubes_de_socio
from modelo.socio import Socio
from modelo.cuota import Cuota
from modelo.club import Club
from modelo.actividad import Actividad
from servicios.servicio_autenticacion import autenticar
from servicios.servicios_socios import listar_socios, listar_clubes_de_socio, registrar_socio, suspender_socio, reactivar_socio


RUTA = Path(__file__).parent / "club.db"

# Si la base previa existe, la borra para que las pruebas arranquen limpias
if RUTA.exists():
    RUTA.unlink()

conexion = conectar(str(RUTA))
crear_tablas(conexion)


# ── Socios ----------------------------------------------------------

bubu = Socio("bubuzela_bubu", 24, "dni", 42890413, "argentino", date(2026, 1, 1), "activo", "socio","bubu124", "bubu0707")
guardar_socio(conexion, bubu)
print("Socio guardado.")

messi = Socio("lionel_messi", 38, "dni", 33000001, "argentino", date(2026, 1, 5), "activo", "socio", "messi10", "campeon2022")
guardar_socio(conexion, messi)
print("Socio guardado.")

shakira = Socio("shakira_mebarak", 49, "dni", 33000002, "colombiana", date(2026, 1, 10), "activo", "socio", "shaki77", "waka2010")
guardar_socio(conexion, shakira)
print("Socio guardado.")

maradona = Socio("diego_maradona", 60, "dni", 33000003, "argentino", date(2026, 1, 15), "suspendido", "socio", "diego10", "manodedios")
guardar_socio(conexion, maradona)
print("Socio guardado.")

tini = Socio("tini_stoessel", 29, "dni", 33000004, "argentino", date(2026, 2, 1), "activo", "admin", "tini_adm", "tini2026")
guardar_socio(conexion, tini)
print("Admin guardado.")

bichota = Socio("karol_g", 35, "dni", 33000005, "colombiana", date(2026, 2, 10), "activo", "admin", "karol_adm", "bichota01")
guardar_socio(conexion, bichota)
print("Admin guardado.")

cr7 = Socio("cristiano_ronaldo", 41, "dni", 33000006, "portugues", date(2026, 2, 20), "activo", "socio", "cr7siuu", "elbicho7")
guardar_socio(conexion, cr7)
print("Socio guardado.")

carlito = Socio("carlito_bala", 30, "dni", 38456721, "argentino", date(2026, 2, 15), "activo","socio","carlito99", "bala1234")
guardar_socio(conexion, carlito)
print("Socio guardado.")

# ── Cuotas ----------------------------------------------------------

cuota1 = Cuota("Pendiente", date(2026, 10, 10), "Octubre 2026")
cuota1.socio_id = "bubu124" 
guardar_cuota(conexion, bubu, cuota1)
print("Cuota guardada.")

cuota2 = Cuota("Pendiente", date(2026, 10, 10), "Octubre 2026")
guardar_cuota(conexion, carlito, cuota2)
print("Cuota guardada.")

cuota4 = Cuota("Pendiente", date(2026, 10, 10), "Octubre 2026")
guardar_cuota(conexion, carlito, cuota4)
print("Cuota guardada.")

cuota5 = Cuota("Pagada", date(2026, 10, 10), "Octubre 2026")
guardar_cuota(conexion, messi, cuota5)
print("Cuota guardada.")

cuota6 = Cuota("Vencida", date(2026, 9, 10), "Septiembre 2026")
guardar_cuota(conexion, shakira, cuota6)
print("Cuota guardada.")

cuota7 = Cuota("Pendiente", date(2026, 11, 10), "Noviembre 2026")
guardar_cuota(conexion, shakira, cuota7)
print("Cuota guardada.")

cuota8 = Cuota("Vencida", date(2026, 8, 10), "Agosto 2026")
guardar_cuota(conexion, maradona, cuota8)
print("Cuota guardada.")

cuota9 = Cuota("Pagada", date(2026, 10, 10), "Octubre 2026")
guardar_cuota(conexion, cr7, cuota9)
print("Cuota guardada.")

cuota10 = Cuota("Pagada", date(2026, 9, 10), "Septiembre 2026")
guardar_cuota(conexion, cr7, cuota10)
print("Cuota guardada.")

# ── Socio Buscado ----------------------------------------------------------

socio_buscado = buscar_socio_por_usuario(conexion, "bubu124")
print("Socio encontrado:", socio_buscado)

# ── Clubes ----------------------------------------------------------

club = Club("9 de julio Rafaela", "Club de fútbol", "Santa Fe", "Lucas Astrada", "09/07/1904")
guardar_club(conexion, club)
print("Club guardado.")

club2 = Club("Atlético de Rafaela", "Club de fútbol", "Santa Fe", "Pedro Gómez", "12/05/1907")
guardar_club(conexion, club2)
print("Club 2 guardado.")

club3 = Club("Racing de Avellaneda", "Club de fútbol", "Buenos Aires", "Diego Milito", "25/03/1903")
guardar_club(conexion, club3)
print("Club 3 guardado.")

club4 = Club("Club Atlético Colón", "Club de fútbol", "Santa Fe", "Germán Lerche", "05/05/1905")
guardar_club(conexion, club4)
print("Club 4 guardado.")

club5 = Club("Club Atlético Newell's Old Boys", "Club de fútbol", "Santa Fe", "Ignacio Boero", "03/11/1903")
guardar_club(conexion, club5)
print("Club 5 guardado.")

club6 = Club("Club Atlético Belgrano", "Club de fútbol", "Córdoba", "Jorge Franceschi", "19/03/1905")
guardar_club(conexion, club6)
print("Club 6 guardado.")

# ── Actividades ----------------------------------------------------------

actividad1 = Actividad("Fútbol", "Martes", "18:00")
actividad2 = Actividad("Natación", "Jueves", "10:00")
actividad3 = Actividad("Básquet", "Lunes", "19:00")
actividad4 = Actividad("Tenis", "Miércoles", "17:00")
actividad5 = Actividad("Vóley", "Viernes", "20:00")
actividad6 = Actividad("Yoga", "Sábado", "09:00")
actividad7 = Actividad("Gimnasio", "Lunes", "08:00")
actividad8 = Actividad("Rugby", "Domingo", "16:00")

guardar_actividad(conexion, actividad1)
guardar_actividad(conexion, actividad2)
guardar_actividad(conexion, actividad3)
guardar_actividad(conexion, actividad4)
guardar_actividad(conexion, actividad5)
guardar_actividad(conexion, actividad6)
guardar_actividad(conexion, actividad7)
guardar_actividad(conexion, actividad8)
print("Actividades guardadas.")

# ── Anota socios a actividades ----------------------------------------------------------

anotar_socio_actividad(conexion, "bubu124", "Fútbol")
anotar_socio_actividad(conexion, "bubu124", "Natación")

anotar_socio_actividad(conexion, "messi10", "Fútbol")
anotar_socio_actividad(conexion, "messi10", "Tenis")

anotar_socio_actividad(conexion, "shaki77", "Yoga")
anotar_socio_actividad(conexion, "shaki77", "Pilates")

anotar_socio_actividad(conexion, "diego10", "Fútbol")
anotar_socio_actividad(conexion, "diego10", "Básquet")

anotar_socio_actividad(conexion, "cr7siuu", "Fútbol")
anotar_socio_actividad(conexion, "cr7siuu", "Gimnasio")
anotar_socio_actividad(conexion, "cr7siuu", "Natación")

actividades_bubu = listar_actividades_de_socio(conexion, "bubu124")
print("Actividades de bubu:", actividades_bubu)

actividades_messi = listar_actividades_de_socio(conexion, "messi10")
print("Actividades de messi:", actividades_messi)

actividades_shakira = listar_actividades_de_socio(conexion, "shaki77")
print("Actividades de shakira:", actividades_shakira)

actividades_maradona = listar_actividades_de_socio(conexion, "diego10")
print("Actividades de maradona:", actividades_maradona)

actividades_cr7 = listar_actividades_de_socio(conexion, "cr7siuu")
print("Actividades de cr7:", actividades_cr7)


desanotar_socio_actividad(conexion, "bubu124", "Natación")

# ── Pruebas ----------------------------------------------------------

# Prueba 1: Login exitoso
socio_ok = autenticar("bubu124", "bubu0707")
if socio_ok is not None:
    print(f"OK - Login exitoso. Usuario: {socio_ok.get_usuario()}")
else:
    print("ERROR - Debería haber permitido el login con datos correctos")

# Prueba 2: Contraseña incorrecta
socio_fallido_clave = autenticar("bubu124", "clave_mala")
if socio_fallido_clave is None:
    print("OK - Rechazó la contraseña incorrecta")
else:
    print("ERROR - Permitió ingresar con contraseña incorrecta")

# Prueba 3: Usuario inexistente
socio_fallido_user = autenticar("usuario_fantasma", "bubu0707")
if socio_fallido_user is None:
    print("OK - Rechazó el usuario inexistente")
else:
    print("ERROR - Permitió ingresar con un usuario inexistente")

asociar_socio_club(conexion, "bubu124", "9 de julio Rafaela")
clubes = listar_clubes_de_socio("bubu124")
print("Clubes de bubu:")
for club in clubes:
    print(club.nombre)

asociar_socio_club(conexion, "carlito99", "Atlético de Rafaela")
clubes = listar_clubes_de_socio("carlito99")
print("Clubes de carlito:")
for club in clubes:
    print(club.nombre)


asociar_socio_club(conexion, "messi10", "Racing de Avellaneda")
asociar_socio_club(conexion, "messi10", "Club Atlético Newell's Old Boys")
clubes = listar_clubes_de_socio("messi10")
print("Clubes de messi:")
for club in clubes:
    print(club.nombre)

asociar_socio_club(conexion, "shaki77", "Club Atlético Colón")
clubes = listar_clubes_de_socio("shaki77")
print("Clubes de shakira:")
for club in clubes:
    print(club.nombre)

asociar_socio_club(conexion, "diego10", "Club Atlético Belgrano")
asociar_socio_club(conexion, "diego10", "Racing de Avellaneda")
clubes = listar_clubes_de_socio("diego10")
print("Clubes de maradona:")
for club in clubes:
    print(club.nombre)

asociar_socio_club(conexion, "cr7siuu", "9 de julio Rafaela")
asociar_socio_club(conexion, "cr7siuu", "Atlético de Rafaela")
asociar_socio_club(conexion, "cr7siuu", "Club Atlético Colón")
clubes = listar_clubes_de_socio("cr7siuu")
print("Clubes de cr7:")
for club in clubes:
    print(club.nombre)

print(suspender_socio("bubu124"))
print(reactivar_socio("bubu124"))
print(len(listar_socios()))
conexion.close()
