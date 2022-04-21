n = 0
c = 0
n2 = 1
while n != 999:
    n = int(input('Ditie um número [999 para parar]: '))
    if n != 999:
        c += n
        n2 += 1
print(f'Você digitou {n2} e a soma deles foi {n}.')
print(n2-1)
