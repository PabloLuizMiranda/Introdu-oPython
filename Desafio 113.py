def leiaInt(n):
    while True:
        try:
            num = int(input(n))
        except (ValueError, TypeError):
            print(f'ERRO! DIGITE UM VALOR VÁLIDO!')
        else:
            return num


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
