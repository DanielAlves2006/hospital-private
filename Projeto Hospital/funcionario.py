from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, salario):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.salario = salario

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
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        try:
            valor = float(valor)
        except ValueError:
            raise ValueError("O salário precisa ser um número.")
        if valor > 850:
            self._salario = valor
        else:
            raise ValueError("O salário tem que ser maior que 850.")

    def apresentar_informacoes(self):
        print(f"Funcionário: {self.nome}, Cargo: {self.cargo}, Salário: {self.salario:.2f}")

    def aplicar_aumento(self, percentagem):
        self._salario += self._salario * (percentagem / 100)
