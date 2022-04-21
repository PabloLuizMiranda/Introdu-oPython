print('='*35)
print('LISTA DE PREÇOS'.center(35))
print('='*35)
produtos = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.00,
            'Caneta', 22.30,
            'Livros', 34.90)
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<25}', end='')
    else:
        print(f'{"R$"}{produtos[c]:>7.2f}')
print('='*35)
