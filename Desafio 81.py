resp = ' '
n = list()
cont = 0
decrescente = n.sort(reverse=True)
while resp not in 'Nn':
    n.append(int(input('Digite um valor: ')))
    cont += 1
    continuar = str(input('Quer continuar?[S/N] ')).strip()[0]
    if continuar in 'Nn':
        break
    if continuar not in 'SsNn':
        continuar = str(input('Quer continuar?[S/N] '))
print(f'Você digitou {cont} elementos.')
print(f'Os valores em ordem decrescente {sorted(n, reverse = True)}')
if 5 in n:
    print('O número 5 está presente na lista.')
else:
    print('O número 5 não está na lista.')
