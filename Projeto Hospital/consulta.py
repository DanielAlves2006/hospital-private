
class Consulta:
    def __init__(self, medico, paciente, data, tipo):
        self.medico = medico
        self.paciente = paciente
        self.data = data
        self.tipo = tipo

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, Tipo):
        if Tipo:
            self._tipo = Tipo
        else:
            raise ValueError("O tipo da consulta deve ser válido.")

    def exibir_detalhes(self):
        print(f"Consulta {self.tipo} no dia {self.data} - Médico: {self.medico.nome}, Paciente: {self.paciente.nome}")

        

   
        
      
        
        
    
