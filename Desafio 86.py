matriz = []
for l in range(3):
    for c in range(3):
        n = int(input(f'Insira um valor para [{l},{c}]: '))
        matriz.append(n)
print(f'[{matriz[0]:^5}] [{matriz[1]:^5}] [{matriz[2]:^5}]')
print(f'[{matriz[3]:^5}] [{matriz[4]:^5}] [{matriz[5]:^5}]')
print(f'[{matriz[6]:^5}] [{matriz[7]:^5}] [{matriz[8]:^5}]')
