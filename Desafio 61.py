print('Gerador de PA')
n1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
cont = 0
while cont < 10:
    mult = cont*r
    cont += 1
    PA = n1 + mult
    print(f'{PA}', end=' -> ')
print(' ACABOU!')
