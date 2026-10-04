from alternativa import Alternativa

class Pregunta:
    def __init__(self, enunciado: str, ayuda: str, requerida: bool, alternativas: list):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerida = requerida
        self.__alternativas = [Alternativa(**alt) for alt in alternativas]

    @property
    def alternativas(self):
        return self.__alternativas

    def mostrar_pregunta(self):
        print(self.enunciado)
        if self.ayuda:
            print(f"Ayuda: {self.ayuda}")
        for alt in self.__alternativas:
            alt.mostrar_alternativa()