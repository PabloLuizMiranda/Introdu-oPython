ced50 = ced20 = ced10 = ced5 = ced1 = 0
print('-'*20)
print('Banco do Cebola'.center(20))
print('-'*20)
total = int(input('Quanto deseja sacar? '))
while True:
    if total >= 50:
        total -= 50
        ced50 += 1
    elif total >= 20:
        total -= 20
        ced20 += 1
    elif total >= 10:
        total -= 10
        ced10 += 1
    elif total >= 5:
        total -= 5
        ced5 += 1
    elif total >= 1:
        total -= 1
        ced1 += 1
    else:
        break
print(f'Total de {ced50} cédulas de 50R$.')
print(f'Total de {ced20} cédulas de 20R$.')
print(f'Total de {ced10} cédulas de 10R$.')
print(f'Total de {ced5} cédulas de 5R$.')
print(f'Total de {ced1} cédulas de 1R$.')
