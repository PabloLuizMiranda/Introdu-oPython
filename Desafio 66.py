n = c = s = 0
while n != 999:
    n = int(input('Digite um valor [Digite 999 para parar]: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'A soma dos {c} valores foi {s}. ')
