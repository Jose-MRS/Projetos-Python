'''
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
'''
lista_compras = []
import os
while True:
    opcao_usuario = input("Selecione uma opção [i]inserir [a]apagar [l]lista ").lower()

    if opcao_usuario == "i":
        nome_produto  = input("Digite o nome do produto: ")
        lista_compras.append(nome_produto)
    elif opcao_usuario == "a" and len(lista_compras) > 0:
        indice_apagar = input("Qual indice você deseja apagar? ")
        try:
           indice_apagar_int = int(indice_apagar)
           del lista_compras[indice_apagar_int]
        except IndexError:
               print('Esse valor está fora da lista')
        except ValueError:
            print("Por favor digite um número no indice!")           
    elif opcao_usuario == "a" and len(lista_compras) < 1:
        print("Não há produtos para retirar")
    elif opcao_usuario == "l" and len(lista_compras) > 0:
        os.system('cls')
        print('LISTA DE COMPRAS')
        for indice, produto in enumerate(lista_compras):
            print(indice, produto)
    elif opcao_usuario == "l" and len(lista_compras) < 1:
        print('Não há produtos para serem listados')
    else:
        print("Por favor digite uma das opçoes!")