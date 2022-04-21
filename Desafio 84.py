lista = list()
parcial = list()
continuar = 'S'
cont = maior = menor = 0
while True:
    if continuar in 'Ss':
        pessoa = str(input('Nome: '))
        parcial.append(pessoa)
        peso = float(input('Peso: '))
        parcial.append(peso)
        if cont == 0:
            maior = menor = peso
        else:
            if peso >= maior:
                peso = maior
            if peso <= menor:
                menor = peso
        lista.append(parcial[:])
        parcial.clear()
        cont += 1
        continuar = str(input('Você quer continuar?[S/N] '))
    else:
        break
print(f'Ao todo, você cadastrou {cont} pessoas.')
print(f'O maior peso foi de {maior}. Peso de ')
for item in lista:
    if item[1] >= maior:
        print(item[0], end=',')
print(f'O menor peso foi de {menor}. Peso de ')
for item in lista:
    if item[1] <= menor:
        print(item[0], end=',')
