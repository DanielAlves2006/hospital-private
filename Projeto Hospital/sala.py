from abc import ABC, abstractmethod

class Sala(ABC):
    def __init__(self, numero, capacidade):
        self.numero = numero
        self.capacidade = capacidade

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        if valor >= 1:
            self._numero = valor
        else:
            raise ValueError("O número da sala tem que ser maior ou igual a 1.")

    @property
    def capacidade(self):
        return self._capacidade

    @capacidade.setter
    def capacidade(self, valor):
        if valor > 0:
            self._capacidade = valor
        else:
            raise ValueError("A capacidade da sala tem que ser maior que zero.")

    @abstractmethod
    def detalhar_sala(self):
        pass
