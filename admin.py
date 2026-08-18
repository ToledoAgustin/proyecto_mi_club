from club import Club # modificar para que herede de club categoria la lista de __socios
from socio import Socio

class Administrador:
    def __init__(self, nombre, usuario, contrasenia):
        self.nombre = nombre
        self.__usuario = usuario
        self.__contrasenia = contrasenia

    def get_usuario (self):
        return self.__usuario

    def set_usuario (self, usuario):
        self.__usuario = usuario

    def get_contrasenia (self):
        return self.__contrasenia
    
    def set_contrasenia (self, contrasenia):
        self.__contrasenia = contrasenia

    # 1) Registrar nuevos socios en un club 
    def registrar_socio(self, club, socio):
        if socio not in club.socios: # esta linea hay que modificar 
            club.socios.append(socio)
            socio.agregar_club(club)
            print(f"El administrador {self.nombre} registró a {socio.get_usuario()} en el club {club.nombre}.")
        else:
            print(f"{socio.get_usuario()} ya está registrado en el club {club.nombre}.")

    # 2) Suspender socios (incumplimiento o deudas) 
    def suspender_socio(self, socio):
        print(f"El administrador {self.nombre} suspende al socio {socio.get_usuario()}.")
        socio.suspender()

    # 3) Reactivar socios previamente suspendidos 
    def reactivar_socio(self, socio):
        print(f"El administrador {self.nombre} reactiva al socio {socio.get_usuario()}.")
        socio.reactivar()

    # 4) Listado completo de socios de un club
    def listar_socios_club(self, club):
        print(f"SOCIOS DEL CLUB {club.nombre}:")
        if not club.socios:
            print("El club no tiene socios registrados.")
        else:
            for socio in club.socios:
                print(f" - {socio.get_usuario()} (Estado: {socio.estado})")

    # 5) Verificar credenciales de acceso del administrador
    def verificar_acceso(self, usuario, contrasenia):
        if usuario == self.__usuario and contrasenia == self.__contrasenia:
            print("Acceso concedido.")
            return True
        else:
            print("Usuario o contraseña incorrectos.")
            return False

admin1 = Administrador("Laura Gómez", "adminLaura", "clave123")
club_1 = Club("De Caño", "Club de fútbol amateur", "Buenos Aires", "Ana Pérez", 1995)
socio1 = Socio("09/12/2018", "Activo", "PepeArgento2006", "holamundo123")
socio2 = Socio("15/03/2019", "Activo", "MaríaFlores", "clave456")
# 1) Registrar socios en el club
admin1.registrar_socio(club_1, socio1)
admin1.registrar_socio(club_1, socio2)
# 4) Listar socios del club
admin1.listar_socios_club(club_1)
# 2) Suspender un socio
admin1.suspender_socio(socio1)
admin1.listar_socios_club(club_1)
# 3) Reactivar un socio
admin1.reactivar_socio(socio1)
admin1.listar_socios_club(club_1)
# 5) Verificar acceso del administrador
admin1.verificar_acceso("adminLaura", "clave123")
admin1.verificar_acceso("adminLaura", "clave_erronea")