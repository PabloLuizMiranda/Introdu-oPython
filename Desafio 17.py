from math import sqrt
adj = float(input('Digite o valor do cateto adjacente:'))
opo = float(input('Digite o valor do cateto oposto:'))
hip = sqrt(adj**2+opo**2)
print(f'O valor da hipotenusa é {hip:.2f}')
