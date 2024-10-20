class Veiculo:
    total_veiculos = 0

    def __init__(self, modelo, marca, ano_veiculo, valor_aluguel_dia, combustivel) -> None:
        self.__modelo = modelo
        self.__marca = marca
        self.__ano_veiculo = ano_veiculo
        self.__valor_aluguel_dia = valor_aluguel_dia
        self.__combustivel = combustivel
        Veiculo.total_veiculos += 1

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def ano_veiculo(self):
        return self.__ano_veiculo

    @ano_veiculo.setter
    def ano_veiculo(self, ano_veiculo):
        self.__ano_veiculo = ano_veiculo

    @property
    def valor_aluguel_dia(self):
        return self.__valor_aluguel_dia

    @valor_aluguel_dia.setter
    def valor_aluguel_dia(self, valor_aluguel_dia):
        self.__valor_aluguel_dia = valor_aluguel_dia

    @property
    def combustivel(self):
        return self.__combustivel

    @combustivel.setter
    def combustivel(self, combustivel):
        self.__combustivel = combustivel

    def mostrar_info(self):
        return print(f"modelo: {self.modelo} marca: {self.marca} ano do veiculo: {self.ano_veiculo} valor da diaria: {self.valor_aluguel_dia} tipo de combustivel: {self.combustivel}")

    def calcular_aluguel(self, dias, desconto=0):
        valor_total = dias * self.valor_aluguel_dia

        if self.__combustivel == 'gasolina':
            valor_total *= 0.95

        if dias > 7:
            valor_total *= 0.90
        valor_total -= desconto
        return valor_total

    @classmethod
    def calcular_veiculos_cadastrados(cls):
        return cls.total_veiculos

    @classmethod
    def aplicar_aumento(cls, percentual):
        cls.valor_aluguel_dia *= (1 + percentual / 100)
