from random import randint
cont = 0
print('-'*25)
print('VAMOS JOGAR PAR OU ÍMPAR:')
print('-'*25)
while True:
    nj = int(input('Diga um valor: '))
    escolha = input('PAR ou ÍMPAR? [P/I] ').upper().strip()[0]
    np = randint(0, 11)
    s = np + nj
    if s % 2 == 0 and escolha == 'P':
        print('-'*20)
        print(f'Você jogou {nj} e o computador {np}. Total de {s} deu ', end='')
        print('PAR.')
        print('-'*20)
        print('VOCÊ GANHOU!')
        print('-'*20)
        print('Vamos jogar novamente...')
        print('--------------------')
        cont += 1
    elif s % 2 == 1 and escolha == 'P':
        print('-'*20)
        print('VOCÊ PERDEU')
        print('-'*20)
        print(f'Você jogou {nj} e o computador {np}. Total de {s} deu ', end='')
        print(f'ÍMPAR')
        print(f'GAME OVER! Você venceu {cont} vezes')
        break
    elif escolha == 'I' and s % 2 == 1:
        print('-'*20)
        print(f'Você jogou {nj} e o computador {np}. Total de {s} deu ', end='')
        print('ÍMPAR.')
        print('-'*20)
        print('VOCÊ GANHOU!')
        print('-'*20)
        print('Vamos jogar novamente...')
        print('-'*20)
        cont += 1
    else:
        print('-'*20)
        print('VOCÊ PERDEU.')
        print('-'*20)
        print(f'GAME OVER! Você venceu {cont} vezes')
        break
