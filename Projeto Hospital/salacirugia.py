from sala import Sala
class SalaCirurgia(Sala):
    def __init__(self, numero, capacidade):
        super().__init__(numero, capacidade)
        self.equipamentos = []

    def adicionar_equipamento(self, equipamento):
        self.equipamentos.append(equipamento)

    def detalhar_sala(self):
        print(f"Sala Cirurgia {self.numero} | Capacidade: {self.capacidade}")
        print("Equipamentos:")
        for equi in self.equipamentos:
            print(f" - {equi}")