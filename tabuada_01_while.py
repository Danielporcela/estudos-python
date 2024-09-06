# Exercícios
# 1. Faça um programa, utilizando while, que mostre na tela os números de 0 a 100.

# 2. Faça um programa, utilizando while, que mostre na tela de 0 até N, em que N é o limite inserido pelo usuário.
#c = 1 

# while c < 10:   NESTE EXEMPLO  OS NUMEROS DE 1 ATE 10
#    print(c)
#    c = c + 1 
#print ('FIM')

""" n = 1
    r = 'S'
    while r == 'S':
       n = int(input('Digite um valor :'))
       r = str(input('Quer continuar ?  [S/N]'':')).upper()
    print('FIM')"""
    
     
"""n = 1
par = impar = 0

while n != 0:
    n = int(input('Digite um valor  :'))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
                  
print('Voce digitou {} numeros pares e {} numeros impares !'.format(par, impar))"""


# Desafio 1      
# 
# 1. Contagem Regressiva

"""numero = int(input("Digite um número para a contagem regressiva: "))
while numero >= 0:
    print(numero)
    numero -= 1
print("Feliz Ano Novo!")"""



# Desafio 2

# 3. Jogo da Adivinhação

"""import random

numero_secreto = random.randint(1, 10)
tentativas = 0
palpite = -1

while palpite != numero_secreto:
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    tentativas += 1

print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")"""


# Desafio 3

#4. Tabuada
#
# Peça ao usuário para digitar um número e, usando um loop while, exiba a tabuada desse número de 1 a 10.

# Desafio 4
numero = int(input("Digite um número para mostrar a tabuada: "))
contador = 1

while contador <= 10:
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1
