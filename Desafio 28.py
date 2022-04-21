from random import randint
num = int(input(f'''-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-
Vou pensar em um número de 0 a 5. Tente adivinhar...
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Em que número eu pensei? '''))
sort = randint(0, 5)
if num == sort:
    print('Parabéns você acertou!')
else:
    print(f'Infelizmente você errou! Pensei em {sort} e não {num}.')
