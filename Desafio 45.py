from random import randint
from time import sleep
pc = randint(0, 2)
opc = int(input('Suas opções:''\n[0] PEDRA\n[1] PAPEL\n[2] TESOURA\nQual é a sua jogada? '))
if opc == 0 or opc == 1 or opc == 2:
    print('JO...')
    sleep(1)
    print('KEN...')
    sleep(1)
    print('PÔ!!!')
    sleep(1)
    print('='*25)
    print(f'O computador jogou {itens[pc]}!'
        f'\nVocê jogou {itens[opc]}!')
    print('='*25)
    if opc == 0: #Escolhendo pedra.
        if pc == 0:
            print('EMPATOU!')
        elif pc == 1:
            print('PC GANHOU!')
        elif pc == 2:
            print('VOCÊ GANHOU!')
    elif opc == 1: #Escolhendo papel.
        if pc == 0:
            print('VOCÊ GANHOU!')
        elif pc == 1:
            print('EMPATOU!')
        elif pc == 2:
            print('PC GANHOU!')
    elif opc == 2: #Escolhendo tesoura.
        if pc == 0:
            print('PC GANHOU!')
        elif pc == 1:
            print('VOCÊ GANHOU!')
        elif pc == 2:
            print('EMPATOU!')
else:
    print('OPÇÃO INVALIDA!')
    exit()
