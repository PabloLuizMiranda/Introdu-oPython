titulo = '10 TERMOS DE UMA PA'
print('='*30)
print(titulo.center(30))
print('='*30)
n1 = int(input('Primeiro termo: '))
r = int(input('razão: '))
for c in range(n1, n1+9*r+1, r):
    print(c, end=' → ')
print('ACABOU!')
