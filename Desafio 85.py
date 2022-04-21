lista = [[], []]
for num in range(7):
    valor = int(input(f'Insira o {num+1}° número: '))
    if valor == 0:
        lista[0].insert(valor, 0)
    else:
        if valor % 2 == 0:
            lista[0].append(valor)
        else:
            lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares foram: {lista[0]}')
print(f'Os valores impares foram: {lista[1]}')
