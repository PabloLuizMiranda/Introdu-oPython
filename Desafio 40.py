n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
med = (n1 + n2) / 2
if med >= 7:
    print(f'Parabéns você foi aprovado com a média de {med:.1f}.')
elif 5 <= med <= 6.9:
    print(f'Você quase conseguiu, porém com a média {med:.1f} você pode fazer a recuperação.')
else:
    print(f'Com a média de {med:.1f} você reprovou!')
