def maior(*num):
    cont = m = 0
    print('Analisando os valores passados...')
    for n in num:
        cont += 1
        if n > m:
            m = n
        print(n, end=' ')
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor foi {m}.')
    print('='*20)


# programa principal.
maior(1, 7, 4, 10, 56, 3, 55, 2)
maior(4, 5, 6, 2)
maior(1, 3, 2)
maior(1)
maior()
maior(-2, 0)
