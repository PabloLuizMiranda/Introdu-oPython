def leiaInt(n):
    num = input(n)
    while True:
        if num.isnumeric():
            return num
        else:
            print(f'ERRO! DIGITE UM VALOR VÁLIDO!')
            num = input(n)


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
