from modelo.persona import Persona


class Socio(Persona):
    def __init__(self, nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad,
                fecha_inscripcion, estado, usuario, contrasenia, rol):
        super().__init__(nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad)
        self.clubes = []
        self.cuotas = []
        self.fecha_inscripcion = fecha_inscripcion
        self.estado = estado  # "Activo" o "Suspendido"
        self.rol = rol  # True = socio con rol de administrador
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

    def es_administrador(self):
        if self.rol == "admin":
            return True

    def cambiar_contrasenia(self, contrasenia_actual, contrasenia_nueva):
        if contrasenia_actual == self.__contrasenia:
            self.__contrasenia = contrasenia_nueva
            return True
        return False

    def verificar_acceso(self, usuario, contrasenia):
        if usuario == self.__usuario and contrasenia == self.__contrasenia:
            return True
        return False

    def agregar_club(self, club):
        if club not in self.clubes:
            self.clubes.append(club)
            return True
        return False

    def dar_baja_club(self, club):
        if club in self.clubes:
            self.clubes.remove(club)
            return True
        return False

    def mostrar_clubes(self):
        if not self.clubes:
            return 'No pertenece a ningún club.'
        resultado = ""
        for club in self.clubes:
            resultado += f' - {club.nombre}'
        return resultado

    def generar_cuota(self, periodo, monto):
        cuota = {"periodo": periodo, "monto": monto, "estado": "Pendiente"}
        self.cuotas.append(cuota)
        return f' Se generó la cuota del período {periodo} por ${monto}.'

    def pagar_cuota(self, periodo):
        for cuota in self.cuotas:
            if cuota["periodo"] == periodo and cuota["estado"] == "Pendiente":
                cuota["estado"] = "Pagada"
                return True
        return False

    def cantidad_cuotas_pendientes(self):
        cantidad_pendientes = 0
        for i in self.cuotas:
            if i["estado"] == "Pendiente":
                cantidad_pendientes += 1
        return cantidad_pendientes

    def tiene_deudas(self):
        if self.cantidad_cuotas_pendientes() > 0:
            return f' El socio {self.__usuario} tiene {self.cantidad_cuotas_pendientes()} cuota(s) sin abonar.'
        else:
            return f' El socio {self.__usuario} no posee deudas.'

    def mostrar_cuotas(self):
        if not self.cuotas:
            return 'No tiene cuotas generadas.'
        resultado = ""
        for cuota in self.cuotas:
            resultado += f" Período: {cuota['periodo']} - Monto: ${cuota['monto']} - Estado: {cuota['estado']}\n"
        return resultado

    def suspender(self):
        if self.estado == "Activo":
            self.estado = "Suspendido"
            return True
        return False

    def reactivar(self):
        if self.estado == "Suspendido":
            self.estado = "Activo"
            return True
        return False

    def mostrar_datos(self):
        return (f'{super().mostrar_datos()}, Fecha Inscripción: {self.fecha_inscripcion}, '
                f'Estado: {self.estado}, Usuario: {self.get_usuario()}, '
                f'Admin: {self.es_admin}')