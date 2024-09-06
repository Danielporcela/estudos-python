def adicionar_itens():
    # Criando uma lista de compras inicial
    lista_compras = []

    # Número de itens que o usuário deseja adicionar
    num_itens = int(input("Quantos itens deseja adicionar à lista de compras? "))

    # Adicionar itens à lista com base na entrada do usuário
    for _ in range(num_itens):
        item = input("Digite o nome do item que deseja adicionar: ")
        lista_compras.append(item)

    # Exibir a lista de compras atualizada
    print("\nLista de Compras Inicial:", lista_compras)
    return lista_compras

def remover_itens(lista_compras):
    # Perguntar ao usuário se ele deseja remover um item, com validação
    while True:
        remover_item = input("Deseja remover algum item? (s/n): ").strip().lower()
        if remover_item in ('s', 'n'):
            break
        else:
            print("Por favor, digite um valor válido ('s' para sim ou 'n' para não).\n")

    # Se o usuário deseja remover um item
    while remover_item == 's':
        item_para_remover = input("Digite o nome do item que deseja remover (ou 'sair' para terminar): ")

        # Verificar se o usuário deseja sair do processo de remoção
        if item_para_remover.lower() == 'sair':
            print("Nenhum item adicional foi removido.")
            break

        # Verificar se o item está na lista
        if item_para_remover in lista_compras:
            lista_compras.remove(item_para_remover)
            print(f"{item_para_remover} foi removido da lista.")
            break  # Sai do loop se o item foi removido
        else:
            print(f"'{item_para_remover}' não está na lista. Por favor, tente novamente.\n")

        # Perguntar novamente se o usuário deseja remover outro item, com validação
        while True:
            remover_item = input("Deseja remover outro item? (s/n): ").strip().lower()
            if remover_item in ('s', 'n'):
                break
            else:
                print("Por favor, digite um valor válido ('s' para sim ou 'n' para não).\n")

    # Exibir a lista de compras final
    print("\nLista de Compras Final:", lista_compras)

def main():
    lista_compras = adicionar_itens()
    remover_itens(lista_compras)

if __name__ == "__main__":
    main()
