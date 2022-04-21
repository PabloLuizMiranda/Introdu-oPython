from time import sleep
conti = 0
age = 0
contgen = 0
for c in range(1, 5):
    sleep(0.5)
    print(f'-----{c}° PESSOA-----')
    sleep(1)
    nome = str(input('Nome: ')).capitalize().strip()
    idade = int(input('Idade: '))
    sex = str(input('Sexo [H/F]: ')).lower().strip()
    if idade > 0:
        conti += idade
    if sex == 'h' and idade > age:
        age = idade
        position = nome
    if sex == 'f' and idade < 20:
        contgen += 1
print(f'A média de idade do grupo é {conti/4} anos.')
print(f'A pessoa mais velha se chama {position} e tem {age} anos.')
print(f'Ao todo são {contgen} mulheres com menos de 20 anos.')
