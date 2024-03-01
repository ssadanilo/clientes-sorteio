# Importando biblioteca linhas
from modulos.biblioteca import (clientes, linhas)

# Importando a função choice da biblioteca random
from random import choice

# Função para cadastrar clientes
def cadastrar_cliente():
    print('Cadastro de Cliente')
    nome = input('Nome: ')
    cpf = input('CPF: ')
    telefone = input('Telefone: ')
    endereco = input('Endereço: ')
    cliente = {
        'Nome': nome,
        'CPF': cpf,
        'Telefone': telefone,
        'Endereço': endereco
    }
    clientes.append(cliente)
    print(f'Cliente {nome} - CPF: {cpf} - Tel: {telefone} - Endereço: {endereco} cadastrado com Sucesso!')

# Função para sortear um cliente
def sortear_cliente():
    if len(clientes) == 0:
        print('Nenhum cliente cadastrado')
    else:
        cliente_sorteado = choice(clientes)
        print(f'{linhas}')
        print('Cliente Sorteado')
        for chave, valor in cliente_sorteado.items():
            print(f'{chave}: {valor}')



    


