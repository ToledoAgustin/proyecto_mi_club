from club import Club
from socio import Socio

class ClubCategoria(Club):
    def __init__(self, nombre, descripcion, ubicacion, presidente, fecha_fundacion):
        super().__init__(nombre, descripcion, ubicacion, presidente, fecha_fundacion)
        self.__socios = []
        self.actividades = []

    def set_socios(self, socios):
        self.__socios = socios

    def get_socios(self):
        return self.__socios

    # --------- 1) Registrar nuevos socios ---------
    def agregar_socio(self, socio):
        self.__socios.append(socio)
        print(f"Socio '{socio.get_usuario()}' registrado con éxito.")
#antes de agregar al socio que verifique si ya estaba.

    def mostrar_socios(self):
        print("· Lista de Socios:")
        if not self.__socios:
            print("No hay socios registrados.")
        else:
            for socio in self.__socios:
                print(f"- Socio: {socio.get_usuario()} (Estado: {socio.estado})")

    # --------- 2) Eliminar socios ---------
    def eliminar_socio(self, socio):
        if socio in self.__socios:
            self.__socios.remove(socio)
            print(f"Socio '{socio.get_usuario()}' eliminado con éxito.")
        else:
            print(f"El socio '{socio.get_usuario()}' no se encontró.")

    # --------- 3) Búsqueda de un socio ---------
    def buscar_socio(self, usuario_buscado):
        for socio in self.__socios:
            if socio.get_usuario() == usuario_buscado:
                print(f"¡Socio encontrado! {socio.get_usuario()} está registrado en esta categoría.")
                return socio
        print(f"No se encontró ningún socio con el usuario '{usuario_buscado}'.")
        return None

    # --------- 4) Cantidad total de socios ---------
    def cantidad_socio(self):
        cantidad = len(self.__socios)
        print(f"Cantidad total de socios: {cantidad}")
        return cantidad

    # --------- 5) Agregar nuevas actividades ---------
    def actividad_nueva(self, actividad):
        self.actividades.append(actividad)
        print(f"Actividad '{actividad}' agregada con éxito.")

    # --------- 6) Eliminar actividades ---------
    def eliminar_actividad(self, actividad):
        if actividad in self.actividades:
            self.actividades.remove(actividad)
            print(f"Actividad '{actividad}' eliminada con éxito.")
        else:
            print(f"La actividad '{actividad}' no se encontró.")

    # --------- 7) Mostrar actividades ---------
    def mostrar_actividades(self):
        print("· Lista de Actividades:")
        if not self.actividades:
            print("No hay actividades registradas.")
        else:
            for actividad in self.actividades:
                print(f"- {actividad}")

    # --------- 8) Porcentaje de socios activos ---------
    def porcentaje_socios_activos(self):
        total = len(self.__socios)
        if total == 0:
            print("No hay socios registrados para calcular el porcentaje.")
            return 0

        cantidad_activos = 0
        for socio in self.__socios:
            if socio.estado == "Activo":
                cantidad_activos = cantidad_activos + 1

        porcentaje = (cantidad_activos / total) * 100
        print(f"El {porcentaje:.2f}% de los socios se encuentra activo.")
        return porcentaje



mi_club = ClubCategoria("Futsal", "Microestadio 40x20", "Amancio Alcorta 2334", "Bubu", "09/12/2018")

# Actividades
mi_club.mostrar_actividades()
mi_club.actividad_nueva("Torneo de penales")
mi_club.actividad_nueva("Handball")
mi_club.mostrar_actividades()

    
socio1 = Socio("Changote Fernández", 28, "DNI", "40123456", "Argentina", "01/01/2020", "Activo", "Changote", "clave1")
socio2 = Socio("Facundo López", 24, "DNI", "41234567", "Argentina", "01/02/2020", "Activo", "Facu", "clave2")
socio3 = Socio("Bubu Martínez", 35, "DNI", "35123456", "Argentina", "01/03/2020", "Suspendido", "Bubu", "clave3")

mi_club.agregar_socio(socio1)
mi_club.agregar_socio(socio2)
mi_club.agregar_socio(socio3)

mi_club.mostrar_socios()
mi_club.cantidad_socio()

mi_club.eliminar_socio(socio1)
mi_club.mostrar_socios()

mi_club.buscar_socio("Facu")
mi_club.buscar_socio("Changote")

mi_club.porcentaje_socios_activos()

mi_club.eliminar_actividad("Handball")
mi_club.mostrar_actividades() 