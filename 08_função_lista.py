# Função ZIP

lista1 = [1, 2, 3, 4, 5]
lista2 = ['Abacate', 'Maça', 'limão', 'Morango','Pera']
lista3 = [ 'R$ 2,00', ' R$ 5,00','R$ 10,00','R$ 8,80', 'R$ 10,00']

for numero, nome, valor in zip (lista1, lista2, lista3):
    print(numero, nome, valor)