tabela = list()
parcial = list()
continuar = 'S'
while True:
    nome = str(input('Nome: '))
    parcial.append(nome)
    nota1 = float(input('Nota 1: '))
    parcial.append(nota1)
    nota2 = float(input('Nota 2: '))
    parcial.append(nota2)
    media = ((nota1 + nota2) / 2)
    parcial.append(media)
    tabela.append(parcial[:])
    parcial.clear()
    continuar = str(input('Quer continuar?[S/N] '))[0].strip()
    while continuar not in 'SsNn':
        continuar = str(input('Opção invalida. Quer continuar?[S/N] '))[0].strip()
    if continuar in 'Nn':
        break
print('-'*40)
print('No.''    ''NOME''            ''MÉDIA')
print('-'*40)
for pos, pessoa in enumerate(tabela):
    print(f'{pos:<7}{pessoa[0]:<15}{pessoa[3]:>5}')
while True:
    mostrar = int(input('Mostrar qual aluno? (999 interrompe)'))
    if mostrar == 999:
        break
    else:
        print(f'Notas de {tabela[mostrar][0]} são {tabela[mostrar][1:3]}')
