class SistemaDeAluguel:
    def __init__(self):
        self.frota = []

    def adicionar_veiculo(self, veiculo):
        self.frota.append(veiculo)

    def mostrar_frota(self):
        for veiculo in self.frota:
            veiculo.mostrar_info()

    def calcular_total_veiculos(self):
        return len(self.frota)
    
    

