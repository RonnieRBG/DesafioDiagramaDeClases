from listado_respuestas import ListadoRespuestas

class Usuario:
    def __init__(self, correo: str, edad: int, region: int):
        self.correo = correo
        self.edad = edad
        self.region = region

    def contestar_encuesta(self, encuesta, respuestas: list):
        listado = ListadoRespuestas(self, respuestas)
        encuesta.agregar_respuesta(listado)