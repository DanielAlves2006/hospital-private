from pessoa import Pessoa
class Paciente(Pessoa):
    def __init__(self, nome, idade, numero_utente):
        super().__init__(nome, idade)
        self.numero_utente = numero_utente    
        self.historico = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, name):
        if name:
            self._nome = name
        else:
            raise ValueError("O campo do nome não pode estar vazio.")

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if valor > 0:
            self._idade = valor
        else:
            raise ValueError("A idade da pessoa tem que ser maior que 0.")


    @property
    def numero_utente(self):
        return self._numero_utente

    @numero_utente.setter
    def numero_utente(self, valor):
        if valor:
            self._numero_utente = valor
        else:
            raise ValueError("O número de utente não pode estar vazio.")

    def adicionar_registro(self, descricao):
        self.historico.append(descricao)

    def mostrar_historico(self):
        print(f"Histórico de {self.nome}:")
        for registro in self.historico:
            print(f" - {registro}")

    def exibir_informacoes(self):
        print(f"Paciente: {self.nome}, Idade: {self.idade}, Nº Utente: {self.numero_utente}")
        
    def atender_paciente(self):
        print(f" O Paciente: {self.nome} vai ser atendido pelo medico ou enfermeiro")
        