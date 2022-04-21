valores = list()
while True:
    v = int(input(f'Digite um valor: '))
    if v not in valores:
        valores.append(v)
        print('Adicionado com sucesso!')
    else:
        print('Não adicionado, valor repetido!!')
    continuar = input('Deseja continuar? [S/N] ').strip()
    if continuar in 'Nn':
        break
    if continuar not in 'Ss':
        continuar = input('Deseja continuar? [S/N]').strip()
valores.sort()
print(valores)
