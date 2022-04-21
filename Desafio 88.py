from random import randint
from random import sample
con = cont = 0
jogo = list()
jogos = list()
print('-'*20)
print('JOGA NA MEGA SENA'.center(20))
print('-'*20)
nj = int(input('Quantos jogos você quer que eu sorteie? '))
print(('-'*5), f'SORTEANDO {nj} JOGOS', ('-' * 5))
for cont in range(1, nj+1):
    for c in range(10):
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            len(jogo)
        if len(jogo) >= 6:
            break
    jogos.append(jogo[:])
    jogo.clear()
for jog in jogos:
    con += 1
    print(f'jogo {con}: ', end='')
    print(jog)

#lista = list()
#cont = 0
#print('-'*20)
#print('JOGA NA MEGA SENA'.center(20))
#print('-'*20)
#n = int(input('Quantos jogos você quer que eu sorteie? '))
#for jogo in range(n):
#    cont += 1
#    sorteados = sample(range(1, 61), 6)
#    sorteados.sort()
#    print(f'Jogo {cont}: {sorteados}.')
#print('-'*15, end='')
#print('BOA SORTE'.center(20), end='')
#print('-'*15)
