from persona import Persona

class Socio(Persona):
    def __init__(self, nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad,
                 fecha_inscripcion, estado, usuario, contrasenia):
        super().__init__(nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad)
        self.clubes = []
        self.cuotas = []
        self.fecha_inscripcion = fecha_inscripcion
        self.estado = estado  # "Activo" o "Suspendido"
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

    def agregar_club(self, club):
        if club not in self.clubes:
            self.clubes.append(club)
            print(f"Te asociaste al club: {club.nombre}")
        else:
            print(f"Ya sos socio de: {club.nombre}")

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

    def generar_cuota(self, periodo, monto):
        cuota = {"periodo": periodo, "monto": monto, "estado": "Pendiente"}
        self.cuotas.append(cuota)
        print(f"Se generó la cuota del período {periodo} por ${monto}.")
        return cuota

    def pagar_cuota(self, periodo):
        for cuota in self.cuotas:
            if cuota["periodo"] == periodo and cuota["estado"] == "Pendiente":
                cuota["estado"] = "Pagada"
                print(f"Se registró el pago de la cuota del período {periodo}.")
                return True
        print(f"No se encontró una cuota pendiente para el período {periodo}.")
        return False

    def tiene_deudas(self):
        cantidad_pendientes = sum(1 for c in self.cuotas if c["estado"] == "Pendiente")
        if cantidad_pendientes > 0:
            print(f"El socio {self.__usuario} tiene {cantidad_pendientes} cuota(s) sin abonar.")
            return True
        else:
            print(f"El socio {self.__usuario} no posee deudas.")
            return False

    def cantidad_cuotas_pendientes(self):
        cantidad = sum(1 for c in self.cuotas if c["estado"] == "Pendiente")
        print(f"Cuotas pendientes: {cantidad}")
        return cantidad

    def mostrar_cuotas(self):
        print("CUOTAS:")
        if not self.cuotas:
            print("No tiene cuotas generadas.")
        else:
            for cuota in self.cuotas:
                print(f" - Período: {cuota['periodo']} - Monto: ${cuota['monto']} - Estado: {cuota['estado']}")

    def suspender(self):
        if self.estado == "Activo":
            self.estado = "Suspendido"
            print(f"El socio {self.__usuario} fue suspendido.")
        else:
            print(f"El socio ya se encuentra en estado: {self.estado}")

    def reactivar(self):
        if self.estado == "Suspendido":
            self.estado = "Activo"
            print(f"El socio {self.__usuario} fue reactivado.")
        else:
            print(f"El socio no está suspendido (estado actual: {self.estado}).")

    def mostrar_datos(self):
        super().mostrar_datos()
        print("=" * 30)
        print(f"Fecha Inscripción: {self.fecha_inscripcion}")
        print(f"Estado: {self.estado}")
        print(f"Usuario: {self.__usuario}")
        print("=" * 30)

socio1 = Socio("Matias Galarza Borja", 2, "DNI", 49903017, "Argentina", "23/02/2026", "Activo", "MatiCABJ", "MATIAS2011")


socio1.mostrar_clubes()
# socio1.dar_baja_club(club_2)
socio1.mostrar_clubes()

socio1.generar_cuota("Agosto 2026", 15000)
socio1.generar_cuota("Septiembre 2026", 15000)
socio1.mostrar_cuotas()
socio1.tiene_deudas()
socio1.cantidad_cuotas_pendientes()
socio1.pagar_cuota("Agosto 2026")
socio1.tiene_deudas()
socio1.cantidad_cuotas_pendientes()

socio1.suspender()
socio1.reactivar()

socio1.verificar_acceso("PepeArgento2006", "holamundo123")
socio1.verificar_acceso("PepeArgento2006", "clave_erronea")
socio1.cambiar_contrasenia("holamundo123", "nuevaClave456")
socio1.verificar_acceso("PepeArgento2006", "nuevaClave456")

socio1.mostrar_datos()