class Veiculo:
    total_veiculos = 0

    def __init__(self,modelo,marca,ano_veiculo,valor_aluguel_dia,combustivel) ->None:
        self.__modelo = modelo
        self.__marca = marca
        self.__ano_veiculo = ano_veiculo
        self.__valor_aluguel_dia = valor_aluguel_dia
        self.__combustivel = combustivel
        Veiculo.total_veiculos+=1

    @property
    def modelo(self):
        return self.__modelo
    @modelo.setter
    def modelo(self,modelo):
        self.__modelo = modelo

    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self,marca):
        self.__marca = marca
    
    @property
    def ano_veiculo(self):
        return self.__ano_veiculo
    @ano_veiculo.setter
    def ano_veiculo(self,ano_veiculo):
        self.__ano_veiculo = ano_veiculo
    
    @property
    def valor_aluguel_dia(self):
        return self.__valor_aluguel_dia
    @valor_aluguel_dia.setter
    def valor_aluguel_dia(self,valor_aluguel_dia):
        self.__valor_aluguel_dia = valor_aluguel_dia

    @property
    def combustivel(self):
        return self.__combustivel
    @combustivel.setter
    def combustivel(self,combustivel):
        self.__combustivel = combustivel
    
    def mostrar_info(self):
        return print(f"modelo: {self.modelo} marca: {self.marca} ano do veiculo: {self.ano_veiculo} valor da diaria: {self.valor_aluguel_dia} tipo de combustivel: {self.combustivel}")
        