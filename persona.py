class Persona:
    def __init__(self, nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad):
        self.nombre_completo = nombre_completo
        self.edad = edad
        self.__tipo_identificacion = tipo_identificacion
        self.__identificacion = identificacion
        self.__nacionalidad = nacionalidad

    def get_tipo_identificacion(self):
        return self.__tipo_identificacion

    def set_tipo_identificacion(self, tipo_identificacion):
        self.__tipo_identificacion = tipo_identificacion
    
    def get_identificacion(self):
        return self.__identificacion

    def set_identificacion(self, identificacion):
        self.__identificacion = identificacion

    def get_nacionalidad(self):
        return self.__nacionalidad

    def set_nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad

    def mostrar_datos(self):
        print(f'Nombre completo: {self.nombre_completo}')
        print(f'Edad: {self.edad}')
        print(f'Tipo de ID: {self.__tipo_identificacion}')
        print(f'Nacionalidad: {self.__nacionalidad}')
        print(f'Estado legal: {self.es_mayor_de_edad()}')
        print(f'Validación: {self.validar_identificacion()}')
        print("-" * 30)


    # --- Métodos de las consignas ---

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return "Es mayor de edad."
        else:
            return "Es menor de edad." # que la edad sea entre el rango de 1 a 110 años. y que tire un error al poner negativo
# hacer otro metodo que me valide que la edad no sea negativa ni pasando los 110 y despues que a ese metodo lo use en el otro metodo de mayor de edad, osea que cada uno tenga su propio metodo
    def validar_identificacion(self):
        if self.__identificacion == "":#saber si el dni tiene 7 y 8 digitos y que no me permita poner letras, que sea un valor numerico
            return "Identificacion Inválida (está vacía)"
        else:
            return "Identificacion Válida"
        

persona1 = Persona("Maxi Jackson", 10, "DNI", "uuf9e409", "Peru")
persona1.mostrar_datos()
persona2 = Persona("Santi Pérez", 15, "DNI", "", "Uruguay")
persona2.mostrar_datos()