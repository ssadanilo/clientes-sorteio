# Importando funções
from modulos.funcoes import (cadastrar_cliente, sortear_cliente)

# Menu com Loop While
def menu_principal():
    while True:
        opcao = input(
            '\nESCOLHA UMA OPÇÃO' 
            '\n1. Cadastrar'
            '\n2. Sortear'
            '\n3. Sair'
            '\n--> '
        )
        if opcao == '1':
            cadastrar_cliente()
        elif opcao == '2':
            sortear_cliente()
        elif opcao == '3':
            print('Fim do programa')
            break
        else:
            print('Opção inválida. Tente novamente')    

        