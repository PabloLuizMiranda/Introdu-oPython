n = int(input('Insira um número: '))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        cont += 1
if cont > 2 or n == 1:
    print(f'O número {n} foi divisível {cont} vezes. \nPortanto não é primo!')
else:
    print(f'O número {n} foi divisível {cont} vezes. \nPortanto é primo!')
