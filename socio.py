from club import Club

class Socio: # socio tiene que heredar de persona.
    def __init__(self, fecha_inscripcion, estado, usuario, contrasenia):
        self.clubes = []
        self.cuotas = []
        self.socios = [] # no va 
        self.fecha_inscripcion = fecha_inscripcion
        self.estado = estado # "Activo" o "Suspendido"
        self.__usuario = usuario
        self.__contrasenia = contrasenia

    def get_usuario(self):
        return self.__usuario

    def set_usuario(self, usuario):
        self.__usuario = usuario

    def get_contrasenia(self):
        return self.__contrasenia

    def set_contrasenia(self, contrasenia):
        self.__contrasenia = contrasenia

    # 9) Actualizar contraseña 
    def cambiar_contrasenia(self, contrasenia_actual, contrasenia_nueva):
        if contrasenia_actual == self.__contrasenia:
            self.__contrasenia = contrasenia_nueva
            print("Contraseña actualizada correctamente.")
            return True
        print("La contraseña actual no coincide. No se pudo actualizar.")
        return False
    
    def verificar_acceso(self, usuario, contrasenia):
        if usuario == self.__usuario and contrasenia == self.__contrasenia:
            print("Acceso concedido.")
            return True
        print("Usuario o contraseña incorrectos.")
        return False

    # 1) Asociarse a uno o más clubes 
    def agregar_club(self, club):
        if club not in self.clubes:
            self.clubes.append(club)
            print(f"Te asociaste al club: {club.nombre}")
        else:
            print(f"Ya sos socio de: {club.nombre}")

    # 2) Dejar de pertenecer a un club determinado
    def dar_baja_club(self, club):
        if club in self.clubes:
            self.clubes.remove(club)
            print(f"Dejaste de pertenecer al club: {club.nombre}")
        else:
            print(f"No pertenecías al club: {club.nombre}")
    
    def mostrar_clubes(self):
        print("CLUBES ASOCIADOS:")
        if not self.clubes:
            print("No pertenece a ningún club.")
        else:
            for club in self.clubes:
                print(f" - {club.nombre}")

    def mostrar_club(self):
        print("=" * 30)
        print(f'Fecha Inscripcion: {self.fecha_inscripcion}')
        print(f'Estado: {self.estado}')
        print(f'Usuario: {self.__usuario}')
        print(f'Contraseña: {self.__contrasenia}')
        print("=" * 30)
    
    # 3) Generar nuevas cuotas por período
    def generar_cuota(self, periodo, monto):
        cuota = {"periodo": periodo, "monto": monto, "estado": "Pendiente"}
        self.cuotas.append(cuota)
        print(f"Se generó la cuota del período {periodo} por ${monto}.")
        return cuota

    # 4) Registrar el pago de una cuota pendiente 
    def pagar_cuota(self, periodo):
        for cuota in self.cuotas:
            if cuota["periodo"] == periodo and cuota["estado"] == "Pendiente":
                cuota["estado"] = "Pagada"
                print(f"Se registró el pago de la cuota del período {periodo}.")
                return True
        print(f"No se encontró una cuota pendiente para el período {periodo}.")
        return False

    # 5) Informar si el socio posee deudas
    def tiene_deudas(self):
        cantidad_pendientes = 0
        for cuota in self.cuotas:
            if cuota["estado"] == "Pendiente":
                cantidad_pendientes = cantidad_pendientes + 1

        if cantidad_pendientes > 0:
            print(f"El socio {self.__usuario} tiene {cantidad_pendientes} cuota(s) sin abonar.")
            return True
        else:
            print(f"El socio {self.__usuario} no posee deudas.")
            return False
    
    # 6) Mostrar cantidad de cuotas pendientes 
    def cantidad_cuotas_pendientes(self):
        cantidad = 0
        for cuota in self.cuotas:
            if cuota["estado"] == "Pendiente":
                cantidad = cantidad + 1

        print(f"Cuotas pendientes: {cantidad}")
        return cantidad
    
    def mostrar_cuotas(self):
        print("CUOTAS:")
        if not self.cuotas:
            print("No tiene cuotas generadas.")
        else:
            for cuota in self.cuotas:
                print(f" - Período: {cuota['periodo']} - Monto: ${cuota['monto']} - Estado: {cuota['estado']}")
    
    # 7) Suspender un socio activo 
    def suspender(self):
        if self.estado == "Activo":
            self.estado = "Suspendido"
            print(f"El socio {self.__usuario} fue suspendido.")
        else:
            print(f"El socio ya se encuentra en estado: {self.estado}")
        
    # 8) Reactivar un socio suspendido
    def reactivar(self):
        if self.estado == "Suspendido":
            self.estado = "Activo"
            print(f"El socio {self.__usuario} fue reactivado.")
        else:
            print(f"El socio no está suspendido (estado actual: {self.estado}).")  
    
    def mostrar_datos(self):
        print("=" * 30)
        print(f"Fecha Inscripción: {self.fecha_inscripcion}")
        print(f"Estado: {self.estado}")
        print(f"Usuario: {self.__usuario}")
        print("=" * 30)


socio1 = Socio("09/12/2018", "Activo", "PepeArgento2006", "holamundo123")

club_1 = Club("De Caño", "Club de fútbol amateur", "Buenos Aires", "Ana Pérez", 1995)
club_2 = Club("Náutico Sur", "Club de Futsal", "Rosario", "Marcos López", 2001)

# 1) y 2) clubes
socio1.agregar_club(club_1)
socio1.agregar_club(club_2)
socio1.mostrar_clubes()
socio1.dar_baja_club(club_2)
socio1.mostrar_clubes()
# 3), 4), 5), 6) cuotas
socio1.generar_cuota("Agosto 2026", 15000)
socio1.generar_cuota("Septiembre 2026", 15000)
socio1.mostrar_cuotas()
socio1.tiene_deudas()
socio1.cantidad_cuotas_pendientes()
socio1.pagar_cuota("Agosto 2026")
socio1.tiene_deudas()
socio1.cantidad_cuotas_pendientes()
# 7) y 8) estado
socio1.suspender()
socio1.reactivar()

# 9) y 10) acceso
socio1.verificar_acceso("PepeArgento2006", "holamundo123")
socio1.verificar_acceso("PepeArgento2006", "clave_erronea")
socio1.cambiar_contrasenia("holamundo123", "nuevaClave456")
socio1.verificar_acceso("PepeArgento2006", "nuevaClave456")

socio1.mostrar_datos()