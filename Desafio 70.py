caro = barato = soma = cont = cont1 = 0
prodcaro = prodbarato = 0
while True:
    print('-'*20)
    print('LOJA PM'.center(20))
    print('-'*20)
    cont += 1
    prod = input('Nome do produto: ')
    preco = float(input('Preço do produto:R$ '))
    soma += preco
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').upper().strip()[0]
    if cont == 1:
        prodcaro = prodbarato = prod
        barato = caro = preco
    if preco > caro:
        caro = preco
        prodcaro = prod
    if preco < barato:
        barato = preco
        prodbarato = prod
    if preco > 1000:
        cont1 += 1
    if continuar == 'N':
        break
print(f'O total da sua compra foi {soma}.')
print(f'Temos {cont1} custando mais de 1000 reais.')
print(f'O produto mais barato foi {prodbarato} custando {barato} reais e o mais caro foi {prodcaro} custando {caro} reais.')
