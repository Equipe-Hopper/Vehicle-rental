from modules.veiculos import Veiculo

class Moto(Veiculo):
    def __init__(self, modelo, marca, ano_veiculo, valor_aluguel_dia, combustivel, cilindrada) -> None:
        super().__init__(modelo, marca, ano_veiculo, valor_aluguel_dia, combustivel)
        self.__cilindrada = cilindrada

    @property
    def cilindrada(self):
        return self.__cilindrada

    @cilindrada.setter
    def cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada

    def calcular_aluguel(self, dias, desconto=0):
        valor_total = super().calcular_aluguel(dias, desconto)

        if self.__cilindrada > 200:
            valor_total *= 1.15

        return valor_total