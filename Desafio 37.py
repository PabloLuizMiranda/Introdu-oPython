nur = int(input('Insira um número: '))

opc = int(input(f'Digite a opção para conversão:'
                f'\n[1] converter para BINÁRIO'
                f'\n[2] converter para OCTAL'
                f'\n[3] converter para HEXADECIMAL \nSua opção: '))
if opc == 1:
    print(f'{nur} convertido para biário é {bin(nur)[2:]}')
elif opc == 2:
    print(f'{nur} convertido para octal é {oct(nur)[2:]}')
elif opc == 3:
    print(f'{nur} convertido para hex éf{hex(nur)[2:]}')
else:
    print('Opção invalida tente novamente!')
