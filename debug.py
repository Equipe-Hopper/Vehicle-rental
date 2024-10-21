from modules.sistemaAluguel import SistemaDeAluguel
from modules.moto import Moto
from modules.carro import Carro
from modules.veiculos import Veiculo

def gerar_menu():

    try:
        p1 = SistemaDeAluguel()
        while True:
            print('='*40)
            print(' '*10,'Sistema de Aluguel')
            print('1 - Alugar um veiculo')
            print('3 - Mostrar frota')
            print('4 - Calcular o total de veiculos')
            print('5 - Mostrar informaçoes do veiculo')
            print('6 - Sair')
            print('='*40)
        
            opcao = int(input('Digite sua opcao: '))

            if opcao == 6:
                break
            else:
                p1.operacao(opcao)

    except Exception as e:
        print(e)
    finally:
        print()
        print("Operaçao Finalizada")
            