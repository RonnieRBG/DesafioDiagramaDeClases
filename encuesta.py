from pregunta import Pregunta
from listado_respuestas import ListadoRespuestas

class Encuesta:
    def __init__(self, nombre: str, preguntas: list):
        self.nombre = nombre
        self.__preguntas = [Pregunta(**p) for p in preguntas]
        self.__listados_respuestas = []

    def mostrar_encuesta(self):
        print(f"--- Encuesta: {self.nombre} ---")
        for p in self.__preguntas:
            p.mostrar_pregunta()

    def agregar_respuesta(self, listado: ListadoRespuestas):
        self.__listados_respuestas.append(listado)

class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre: str, preguntas: list, edad_minima: int, edad_maxima: int):
        super().__init__(nombre, preguntas)
        self.__edad_minima = edad_minima
        self.__edad_maxima = edad_maxima

    def agregar_respuesta(self, listado: ListadoRespuestas):
        if self.__edad_minima <= listado.usuario.edad <= self.__edad_maxima:
            super().agregar_respuesta(listado)

class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre: str, preguntas: list, regiones: list):
        super().__init__(nombre, preguntas)
        self.__regiones = regiones

    def agregar_respuesta(self, listado: ListadoRespuestas):
        if listado.usuario.region in self.__regiones:
            super().agregar_respuesta(listado)