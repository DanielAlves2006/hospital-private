from enfermeiro import Enfermeiro
from administracao import Administrativo
class EnfermeiroChefe(Enfermeiro, Administrativo):
    def __init__(self, nome, idade, salario_base, turno, setor, bonus_chefe):
        Enfermeiro.__init__(self, nome, idade, salario_base, turno)
        Administrativo.__init__(self, nome, idade, salario_base, setor)
        self.bonus_chefe = bonus_chefe

    @property
    def bonus_chefe(self):
        return self._bonus_chefe

    @bonus_chefe.setter
    def bonus_chefe(self, valor):
        if valor > 20:
            self._bonus_chefe = valor
        else:
            raise ValueError("O bônus tem que ser maior que 20.")

    def calcular_pagamento(self):
        return Enfermeiro.calcular_pagamento(self) + self.bonus_chefe

    def exibir_informacoes(self):
        print(f"Enfermeiro Chefe: {self.nome}, Turno: {self.turno}, Setor: {self.setor}, Pacientes: {len(self.pacientes)}")
