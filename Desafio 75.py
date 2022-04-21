conjunto = (int(input('Digite um número: ')),
            int(input('Digite mais um número: ')),
            int(input('Digite outro número: ')),
            int(input('Digite o último número: ')))
print(f'Você digitou os valores {conjunto}')
print(f'O valor 9 apareceu {conjunto.count(9)} vezes.')
if 3 in conjunto:
    print(f'O primeiro três foi digitado na {conjunto.index(3)+1}° posição.')
else:
    print('O valor 3 não foi encontrado.')
print(f'Os valores pares digitados foram: ', end='')
for c in conjunto:
    if c % 2 == 0:
        print(c, end=' ')
