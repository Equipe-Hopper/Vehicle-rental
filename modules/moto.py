from modules.veiculos import Veiculo

class Moto(Veiculo):
    def __init__(self, modelo, marca, ano_veiculo, valor_aluguel_dia, combustivel,cilindrada):
        super().__init__(modelo, marca, ano_veiculo, valor_aluguel_dia, combustivel,cilindrada)
    
    def calcular_aluguel(self, dias, desconto=0,cilindrada=None):
        if cilindrada>200:
            pass
            
        return super().calcular_aluguel(dias, desconto)