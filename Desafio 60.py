n = int(input('Insira o número para descobrir seu fatorial: '))
cont = n
f = 1
while cont > 0:
    f *= cont
    cont -= 1
print(f)
