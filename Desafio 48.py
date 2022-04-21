num = int(input('Escolha um número: '))
soma = 0
cont = 0
if num > 500:
    print('O limite maximo é 500.')
    exit()
for c in range(1, num+1, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print(f'A soma dos {cont} valores solicitados é {soma}.')
