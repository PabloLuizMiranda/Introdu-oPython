n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
opc = 0
while opc != 5:
    print('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior\n[ 4 ] novos número \n[ 5 ] sair do programa ')
    opc = int(input('Escolha uma opção: '))
    if opc == 1:
        n3 = n1 + n2
        print(n3)
    elif opc == 2:
        n3 = n1 * n2
        print(n3)
    elif opc == 3:
        if n1 > n2:
            print(n1)
        else:
            print(n2)
    elif opc == 4:
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    if opc > 5:
        input('Valor inválido tente novamente: ')
print('Fim do programa.')
