from random import randint
computador = randint(1, 10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
tentativa = int(input('Tente adivinhar: '))
cont = 0
while tentativa != computador:
    if tentativa < computador:
        tentativa = int(input(' MAIS...Tente novamente.\n Qual seu palpite? '))
        cont += 1
    if tentativa > computador:
        tentativa = int(input(' MENOS... Tente novamente:.\n Qual seu palpite? '))
        cont += 1
print(f'Parabéns você acertou! Com {cont} tentativas.')
