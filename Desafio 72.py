numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco')
choice = int(input('Escolha um número entre 0 e 5: '))
contiuar = ' '
while True:
    if 0 <= choice <= 5:
        print(f'O número escolhido foi {numero[choice]}.')
        continuar = input('Deseja continuar? [S/N]').strip().upper()[0]
        if continuar == 'S':
            choice = int(input('Escolha um número entre 0 e 5: '))
        else:
            break
    else:
        choice = int(input('Tente novamente: Escolha um número entre 0 e 5: '))
