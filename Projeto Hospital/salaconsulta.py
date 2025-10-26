from sala import Sala
from medico import Medico
class SalaConsulta(Sala):
    def __init__(self, numero, capacidade, medico_responsavel):
        super().__init__(numero, capacidade)
        self.medico_responsavel = medico_responsavel
        self.pacientes = []

    @property
    def medico_responsavel(self):
        return self._medico_responsavel

    @medico_responsavel.setter
    def medico_responsavel(self, valor):
        if isinstance(valor, Medico):
            self._medico_responsavel = valor
        else:
            raise TypeError("O responsável deve ser um Médico.")

    def agendar_consulta(self, paciente):
        if len(self.pacientes) < self.capacidade:
            self.pacientes.append(paciente)
        else:
            print("Capacidade da sala ultrapassada!")

    def detalhar_sala(self):
        print(f"Sala {self.numero} | Capacidade: {self.capacidade} | Médico: {self.medico_responsavel.nome}")
