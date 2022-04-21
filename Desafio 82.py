list_tot = list()
list_par = list()
list_impar = list()
resp = ' '
while resp not in 'Nn':
    n = int(input('Insira um número: '))
    list_tot.append(n)
    if n % 2 == 0:
        list_par.append(n)
    if n % 2 == 1:
        list_impar.append(n)
    continuar = str(input('Quer continuar?[S/N] ')).strip()[0]
    if continuar in 'Nn':
        break
    if continuar not in 'SsNn':
        continuar = str(input('Quer continuar?[S/N] '))
list_tot.sort()
list_par.sort()
list_impar.sort()
print(f'A lista completa é {list_tot}')
print(f'A lista de pares é {list_par}')
print(f'A lista de impar é {list_impar}')
