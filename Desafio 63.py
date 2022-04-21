from math import floor
print('Sequência de Fibonacci')
n = int(input('Quantos termos você quer mostrar? '))
cont = 0
p = -1
r = 1
if n == 1:
    print('0')
if n % 2 == 0:
    while cont < (n/2):
        r = r + p
        p = p + r
        cont += 1
        print(r*-1, end=' -> ')
        print(p*-1, end=' -> ')
else:
    while cont < floor(n/2):
        r = r + p
        p = p + r
        cont += 1
        print(r * -1, end=' -> ')
        print(p * -1, end=' -> ')
    r = r + p
    print(r * -1, end=' -> ')
print('ACABOU')
