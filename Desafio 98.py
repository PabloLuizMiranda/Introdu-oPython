from time import sleep


def contador(i, f, r):
    if i < 0 or f < 0:
        if r > 0:
            for num in range(i, f - 1, -r):
                print(num, end=' ')
                sleep(0.5)
            print('FIM!')
            sleep(0.5)
            print(f'=' * 30)
            sleep(0.5)
        elif r < 0:
            for num in range(i, f + 1, -r):
                print(num, end=' ')
                sleep(0.5)
            print('FIM!')
            print(f'=' * 30)
        elif r == 0:
            print('O passo igual a 0 é invalido.')
    else:
        if r > 0:
            for num in range(i, f + 1, r):
                print(num, end=' ')
                sleep(0.5)
            print('FIM!')
            sleep(0.5)
            print(f'=' * 30)
            sleep(0.5)
        elif r < 0:
            for num in range(i, f - 1, r):
                print(num, end=' ')
                sleep(0.5)
            print('FIM!')
            print(f'=' * 30)
        elif r == 0:
            print('O passo igual a 0 é invalido.')


# programa principal.
contador(1, 10, 1)
contador(10, 0, -2)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
