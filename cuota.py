from datetime import datetime

class Cuota:
    def __init__(self, estado, fecha_de_vencimiento, periodo):
        self.__estado = estado
        self.fecha_de_vencimiento = fecha_de_vencimiento
        self.periodo = periodo

    def get_estado (self):
        return self.__estado

    def set_estado (self, estado):
        self.__estado = estado

    # 1) Registrar una cuota como pagada 
    def registrar_pago(self):
        self.__estado = "Pagada"
        print(f"La cuota del período {self.periodo} fue registrada como pagada.")

    # 2) Determinar si una cuota está vencida 
    def esta_vencida(self):
        fecha_vencimiento = datetime.strptime(self.fecha_de_vencimiento, "%d/%m/%Y").date()
        fecha_actual = datetime.now().date()

        if self.__estado != "Pagada" and fecha_actual > fecha_vencimiento:
            return "Sí"
        else:
            return "No"
        
    # 3) Actualizar automáticamente el estado de la cuota 
    def actualizar_estado(self):
        if self.__estado == "Pagada":
            print(f"La cuota del período {self.periodo} ya está pagada, no se actualiza.")
            return
    
        if self.esta_vencida():
            self.__estado = "Vencida"
            print(f"La cuota del período {self.periodo} pasó a estado Vencida.")
        else:
            self.__estado = "Pendiente"
            print(f"La cuota del período {self.periodo} sigue en estado Pendiente.")
    
    # 4) Informar cuántos días faltan para el vencimiento
    def dias_para_vencimiento(self):
        fecha_vencimiento = datetime.strptime(self.fecha_de_vencimiento, "%d/%m/%Y").date()
        fecha_actual = datetime.now().date()
        diferencia = fecha_vencimiento - fecha_actual
        dias = diferencia.days

        if dias > 0:
            print(f"Faltan {dias} día(s) para el vencimiento de la cuota del período {self.periodo}.")
        elif dias == 0:
            print(f"La cuota del período {self.periodo} vence hoy.")
        else:
            print(f"La cuota del período {self.periodo} venció hace {abs(dias)} día(s).") # abs :valor absoluto
        return dias
    
    # 5) Renovar la cuota para un nuevo período
    def renovar(self, nuevo_periodo, nueva_fecha_vencimiento):
        self.periodo = nuevo_periodo
        self.fecha_de_vencimiento = nueva_fecha_vencimiento
        self.__estado = "Pendiente"
        print(f"La cuota fue renovada para el período {nuevo_periodo}, vence el {nueva_fecha_vencimiento}.")

    def mostrar_cuota(self):
        print("=" * 30)
        print(f"Período: {self.periodo}")
        print(f"Fecha de vencimiento: {self.fecha_de_vencimiento}")
        print(f"Estado: {self.__estado}")
        print("=" * 30)


# Cuota vencida (fecha pasada, sin pagar)
cuota1 = Cuota("Pendiente", "01/01/2026", "Enero 2026")
cuota1.mostrar_cuota()
print("¿Está vencida?", cuota1.esta_vencida())
cuota1.dias_para_vencimiento()
cuota1.actualizar_estado()
cuota1.mostrar_cuota()
print()
# Cuota que aún no vence
cuota2 = Cuota("Pendiente", "31/12/2026", "Diciembre 2026")
cuota2.mostrar_cuota()
print("¿Está vencida?", cuota2.esta_vencida())
cuota2.dias_para_vencimiento()
cuota2.actualizar_estado()
cuota2.mostrar_cuota()
print()
# Registrar pago y renovar
cuota2.registrar_pago()
cuota2.mostrar_cuota()
cuota2.renovar("Enero 2027", "31/01/2027")
cuota2.mostrar_cuota()