print('=' * 20, end='')
print('LOJAS PB', end='')
print('=' * 20)
valor = float(input('Preço das compras: R$ '))
print('FORMAS DE PAGAMENTO:'
      '\n[1] à vista dinheiro/cheque'
      '\n[2] à vista cartão'
      '\n[3] 2x no cartão'
      '\n[4] 3x ou mais no cartão')
forma = int(input('Qual é a opção? '))
if forma == 1:
    print(f'Sua compra de R${valor:.2f} vai custar R${valor - valor*0.1:.2f} no final.')
elif forma == 2:
    print(f'Sua compra de R${valor:.2f} vai custar R${valor - valor*0.05:.f} no final.')
elif forma == 3:
    print(f'Sua compra será parcelada em 2x de R${valor / 2} cada  SEM JUROS.')
    print(f'Sua compra será parcelada em 2x e vai custar R${valor:.2f} no final.')
elif forma == 4:
    parcelas = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em {parcelas:}x de R${valor*0.2:.2f}'
          f'\nSua compra de R${valor:.2f} vai custar R${valor*1.2:.2f} no final. ')
else:
    total = 0
    print('OPÇÃO INVÁLIDA DE PAGAMENTO.')
