
#Menu de Opções:

#Crie um programa que exiba um menu de opções para o usuário. O programa deve continuar exibindo o menu até que o usuário escolha a opção de sair. 

#Implemente um sistema simples de opções como "1. Dizer Olá", "2. Mostrar Data", "3. Sair", etc.

import datetime

def menu_de_opcoes():
    opcao = 0

    while opcao != 3:
        print("\nMenu de Opções:")
        print("1. Dizer Olá")
        print("2. Mostrar Data Atual")
        print("3. Sair")
        
        # Solicita ao usuário que insira uma opção
        opcao = int(input("Escolha uma opção: "))

        # Executa a ação correspondente à opção selecionada
        if opcao == 1:
            print("Olá! Espero que você esteja tendo um ótimo dia.")
        elif opcao == 2:
            data_atual = datetime.datetime.now()
            print("Data e Hora Atual:", data_atual.strftime("%d/%m/%Y %H:%M:%S"))
        elif opcao == 3:
            print("Saindo do programa. Até logo!")
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Chama a função do menu de opções
menu_de_opcoes()


