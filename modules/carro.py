from modules.veiculos import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo, marca, ano_veiculo, valor_aluguel_dia, combustivel, ar_condicionado, cambio) -> None:
        super().__init__(modelo, marca, ano_veiculo, valor_aluguel_dia, combustivel)
        self.__ar_condicionado = ar_condicionado
        self.__cambio = cambio

    @property
    def ar_condicionado(self):
        return self.__ar_condicionado

    @ar_condicionado.setter
    def ar_condicionado(self, ar_condicionado):
        self.__ar_condicionado = ar_condicionado

    @property
    def cambio(self):
        return self.__cambio

    @cambio.setter
    def cambio(self, cambio):
        self.__cambio = cambio

    def calcular_aluguel(self, dias, desconto=0):
        valor_total = super().calcular_aluguel(dias, desconto)

        if self.__ar_condicionado:
            valor_total *= 1.10

        if self.__cambio == 'automático':
            valor_total *= 1.05

        return valor_total
