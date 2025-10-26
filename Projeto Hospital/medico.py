from funcionario import Funcionario
from paciente import Paciente

class Medico(Funcionario):
    def __init__(self, nome, idade, salario_base, especialidade, ):
        super().__init__(nome, idade, salario_base)
        self.especialidade = especialidade        
        self.pacientes = []

    @property
    def especialidade(self):
        return self._especialidade

    @especialidade.setter
    def especialidade(self, esp):
        if esp:
            self._especialidade = esp
        else:
            raise ValueError("A especialidade não pode estar vazia.")

    def adicionar_paciente(self, paciente):
        if isinstance(paciente, Paciente):
            self.pacientes.append(paciente)
        else:
            raise TypeError("Somente objetos do tipo Paciente podem ser adicionados.")

    def listar_pacientes(self):
        print(f"Pacientes atendidos pelo Dr. {self.nome}:")
        for pac in self.pacientes:
            print(f" - {pac.nome}")

    def calcular_pagamento(self):
        valor_por_paciente = 50
        return self.salario + (len(self.pacientes) * valor_por_paciente)

    def exibir_informacoes(self):
        print(f"Médico: {self.nome}, Especialidade: {self.especialidade}, Pacientes: {len(self.pacientes)}")
