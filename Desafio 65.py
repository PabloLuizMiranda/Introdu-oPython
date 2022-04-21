num = quant = soma = 0
cont = True
maior = 0
menor = 0
while cont:
    cont = True
    num = int(input('Insira um número: '))
    con = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    if con == 'S':
        cont = True
    else:
        cont = False
print(f'Você digitou {quant} números e a média foi {soma/quant}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
print('FIM')
