from funcionario import Funcionario
from paciente import Paciente
class Enfermeiro(Funcionario):
    def __init__(self, nome, idade, salario_base, turno):
        super().__init__(nome, idade, "Enfermeiro", salario_base)
        self.turno = turno
        self.pacientes = []

    @property
    def turno(self):
        return self._turno

    @turno.setter
    def turno(self, dia):
        if dia.lower() in ["dia", "noite"]:
            self._turno = dia.lower()
        else:
            raise ValueError("O turno só pode ser 'dia' ou 'noite'.")

    def adicionar_paciente(self, paciente):
        if isinstance(paciente, Paciente):
            self.pacientes.append(paciente)

    def listar_pacientes(self):
        print(f"Pacientes sob o cuidado de {self.nome}:")
        for p in self.pacientes:
            print(f" - {p.nome}")

    def calcular_pagamento(self):
        adicional = 200 if self.turno == "noite" else 100
        return self.salario + adicional

    def exibir_informacoes(self):
        print(f"Enfermeiro: {self.nome}, Turno: {self.turno}, Pacientes: {len(self.pacientes)}")
