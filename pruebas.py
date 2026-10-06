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
from base_datos.base_datos import conectar, crear_tablas, guardar_socio, buscar_socio_por_usuario, guardar_cuota, listar_cuotas_de_socio, guardar_club, guardar_actividad, anotar_socio_actividad, listar_actividades_de_socio, desanotar_socio_actividad
from modelo.socio import Socio
from modelo.cuota import Cuota
from modelo.club import Club
from modelo.actividad import Actividad

RUTA = Path(__file__).parent / "club.db"

# Si la base previa existe, la borra para que las pruebas arranquen limpias
if RUTA.exists():
    RUTA.unlink()

conexion = conectar(str(RUTA))
crear_tablas(conexion)

bubu = Socio("bubuzela_bubu", 24, "dni", 42890413, "argentino", date(2026, 1, 1), "activo", "bubu124", "bubu0707", "socio")
guardar_socio(conexion, bubu)
print("Socio guardado.")

cuota1 = Cuota("Pendiente", date(2026, 10, 10), "Octubre 2026")
cuota1.socio_id = "bubu124" 
guardar_cuota(conexion, bubu, cuota1)
print("Cuota guardada.")

carlito = Socio("carlito_bala", 30, "dni", 38456721, "argentino", date(2026, 2, 15), "activo", "carlito99", "bala1234", "socio")
guardar_socio(conexion, carlito)
print("Socio guardado.")

cuota2 = Cuota("Pendiente", date(2026, 10, 10), "Octubre 2026")
guardar_cuota(conexion, carlito, cuota2)
print("Cuota guardada.")

socio_buscado = buscar_socio_por_usuario(conexion, "bubu124")
print("Socio encontrado:", socio_buscado)

club = Club("9 de julio Rafaela", "Club de fútbol", "Santa Fe", "Lucas Astrada", "09/07/1904")
guardar_club(conexion, club)
print("Club guardado.")

actividad1 = Actividad("Fútbol", "Martes", "18:00")
actividad2 = Actividad("Natación", "Jueves", "10:00")
guardar_actividad(conexion, actividad1)
guardar_actividad(conexion, actividad2)
print("Actividades guardadas.")

anotar_socio_actividad(conexion, "bubu124", "Fútbol")
anotar_socio_actividad(conexion, "bubu124", "Natación")

actividades_bubu = listar_actividades_de_socio(conexion, "bubu124")


desanotar_socio_actividad(conexion, "bubu124", "Natación")


conexion.close()

