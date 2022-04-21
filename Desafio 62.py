print('Gerador de PA')
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
mais = 10
cont = 0
while mais > 0:
    total = cont + mais
    while cont < total:
        mult = cont*r
        cont += 1
        PA = n + mult
        print(f'{PA}', end=' -> ')
    print('PAUSA')
    mais = int(input('\nQuantos termos a mais? '))
print(f'Progressão finalizada com {cont} termos mostrados!')
