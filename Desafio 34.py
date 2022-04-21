sal = float(input('Digite aqui seu salário:R$ '))
if sal <= 1250:
    resp = (sal * 0.15) + sal
else:
    resp = (sal * 0.1) + sal
print(f'O salário de {sal:.2f} com aumento será de {resp:.2f}.')
