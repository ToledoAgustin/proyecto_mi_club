from datetime import datetime

class Club:
    def __init__(self, nombre, descripcion, ubicacion, presidente, fecha_fundacion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        self.__presidente = presidente
        self.__fecha_fundacion = fecha_fundacion  # se espera el año como número, ej: 1995

    def get_presidente(self):
        return self.__presidente

    # --------- 1) Modificar el presidente del club ---------
    def set_presidente(self, presidente):
        presidente_anterior = self.__presidente
        self.__presidente = presidente
        print(f"Cambio de autoridades: {presidente_anterior} → {self.__presidente}")

    def get_fecha_fundacion(self):
        return self.__fecha_fundacion

    def set_fecha_fundacion(self, fecha_fundacion):
        self.__fecha_fundacion = fecha_fundacion

    # --------- 2) Calcular / mostrar antigüedad ---------
    def calcular_antiguedad(self):
        fecha_fundacion_dt = datetime.strptime(self.__fecha_fundacion, "%d/%m/%Y")
        anio_actual = datetime.now().year
        antiguedad = anio_actual - fecha_fundacion_dt.year
        return antiguedad

    def mostrar_antiguedad(self):
        antiguedad = self.calcular_antiguedad()
        print(f"El club tiene {antiguedad} años de antigüedad.")

    # --------- 3) Determinar si es institución histórica ---------
    def es_institucion_historica(self):
        if self.calcular_antiguedad() > 50:
            return True
        else:
            return False

    def mostrar_info(self):
        print(f'Nombre: {self.nombre}')
        print(f'Descripcion: {self.descripcion}')
        print(f'Ubicacion: {self.ubicacion}')
        print(f'Presidente: {self.__presidente}')
        print(f'Fecha de Fundacion: {self.__fecha_fundacion}')

        self.mostrar_antiguedad()

        if self.es_institucion_historica():
            print("Estado: ¡Este es un club histórico!")
        else:
            print("Estado: ¡No es un club histórico!")
        print("-" * 30)



club1 = Club("9 de julio Rafaela", "Club de fútbol", "Santa Fe", "Lucas Astrada", "09/07/1904")
club2 = Club("Inter Miami", "Club de la MLS", "Miami", "David Beckham", "09/12/2018")

club1.set_presidente("Juan Román Riquelme")

club1.mostrar_info()
club2.mostrar_info()