tot18 = totH = totM = 0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA'.center(30))
    print('-'*30)
    idade = int(input('IDADE: '))
    if idade > 18:
        tot18 += 1
    sexo = str(input('SEXO[M/F]: '))[0].strip()
    if sexo in 'Mm':
        totH += 1
    if sexo in 'Ff' and idade < 20:
        totM += 1
    continuar = str(input('Deseja continuar?[S/N] '))[0].strip()
    while continuar not in 'SsNn':
        continuar = str(input('Opção invalida. Digite uma válida[S/N]: '))
    if continuar in 'Nn':
        break
print(f'Total de pessoas com com mais de 18 anos: {tot18}.')
print(f'Ao todo temos {totH} homens cadastrados.')
print(f'E temos {totM} com menos de 20 anos.')
