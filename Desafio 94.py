grupo = list()
pessoa = dict()
cont = soma = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).capitalize().strip()
    cont += 1
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    pessoa['sexo'] = str(input('Sexo[M/F] '))[0].strip()
    while pessoa['sexo'] not in 'MmFf':
        pessoa['sexo'] = str(input('Sexo ínvalido. Sexo[M/F]: '))
    grupo.append(pessoa.copy())
    continuar = str(input('Quer continuar?[S/N] '))[0].strip()
    while continuar not in 'SsNn':
        continuar = str(input('Opção invalida. Quer continuar?[S/N] '))[0].strip()
    if continuar in 'Nn':
        break
print(f'A) Ao todo temos {cont} pessoas cadastradas.')
print(f'B) A média de idade é de {soma/cont:.2f} anos.')
print(f'C) As mulheres cadastradasa foram: ', end='')
for c in grupo:
    if c['sexo'] in 'Ff':
        print(c['nome'], end=', ')
print(f'\nD) Lista de pessoas acima da média: ')
for c in grupo:
    if c['idade'] > soma/cont:
        print(f'nome = {c["nome"]}; sexo = {c["sexo"].upper()}; idade {c["idade"]};')
print('ENCERRADO')
