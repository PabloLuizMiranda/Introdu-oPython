rmatriz = []
soma = somac3 = maior = 0
for l in range(3):
    for c in range(3):
        n = int(input(f'Insira um valor para [{l},{c}]: '))
        matriz.append(n)
        if n % 2 == 0:
            soma += n
        if c == 2:
            somac3 += n
        if l == 1:
            if n > maior:
                maior = n
print('-='*30)
print(f'[{matriz[0]:^5}] [{matriz[1]:^5}] [{matriz[2]:^5}]')
print(f'[{matriz[3]:^5}] [{matriz[4]:^5}] [{matriz[5]:^5}]')
print(f'[{matriz[6]:^5}] [{matriz[7]:^5}] [{matriz[8]:^5}]')
print('-='*30)
print(f'A soma dos valores pares é {soma}.')
print(f'A soma dos valores da terceira coluna são {somac3}.')
print(f'O maior valor da segunda linha é {maior}.')
