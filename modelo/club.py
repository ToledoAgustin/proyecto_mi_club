from datetime import datetime

class Club:
    def __init__(self, nombre, descripcion, ubicacion, presidente, fecha_fundacion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        self.__presidente = presidente
        self.__fecha_fundacion = fecha_fundacion 

    def get_presidente(self):
        return self.__presidente

    # --------- 1) Modificar el presidente del club ---------
    def set_presidente(self, presidente):
        presidente_anterior = self.__presidente
        self.__presidente = presidente
        return f'Cambio de autoridades: {presidente_anterior} → {self.__presidente}'

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
        return f'El club tiene {antiguedad} años de antigüedad.'

    # --------- 3) Determinar si es institución histórica ---------
    def es_institucion_historica(self):
        if self.calcular_antiguedad() > 50:
            return True
        return False

    def mostrar_info(self):
        return (f'Nombre: {self.nombre}, Descripcion: {self.descripcion}, Ubicacion: {self.ubicacion}, '
                f'Presidente: {self.__presidente}, Fecha de Fundacion: {self.__fecha_fundacion}, '
                f'{self.mostrar_antiguedad()}, Institución histórica: {self.es_institucion_historica()}')