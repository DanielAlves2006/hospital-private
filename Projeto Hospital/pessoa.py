from abc import ABC, abstractmethod

@abstractmethod
class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

   