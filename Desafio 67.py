n = c = 0
while n >= 0:
    n = int(input(f'------------------------------------\nQuer ver a tabuada de qual valor? '))
    print('------------------------------------')
    if n < 0:
        break
    for t in range(1, 11):
        print(f'{n} x {t} = {n * t}')
        c += 1
print('Programa de tabuada encerrado, volte sempre!')
