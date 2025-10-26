from funcionario import Funcionario
class Administrativo(Funcionario):
    def __init__(self, nome, idade, salario_base, setor):
        super().__init__(nome, idade, "Administrativo", salario_base)
        self.setor = setor
        self.horas_trabalhadas = 0

    @property
    def setor(self):
        return self._setor

    @setor.setter
    def setor(self, valor):
        if valor:
            self._setor = valor
        else:
            raise ValueError("O setor não pode estar vazio.")

    def registrar_horas(self, horas):
        if horas > 0:
            self.horas_trabalhadas += horas

    def calcular_pagamento(self):
        valor_por_hora = 25
        return self.salario + (self.horas_trabalhadas * valor_por_hora)

    def exibir_informacoes(self):
        print(f"Administrativo: {self.nome}, Setor: {self.setor}, Horas: {self.horas_trabalhadas}")

