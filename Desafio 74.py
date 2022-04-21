from random import randint
randint(1, 10)
conjunto = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
crescente = sorted(conjunto)
print(f'Os valores sorteados foram: ', end='')
for n in conjunto:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {crescente[4]}.')
print(f'O menor valor sorteado foi {crescente[0]}.')
