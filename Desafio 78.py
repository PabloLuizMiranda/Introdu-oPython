valores = []
LISTAmaior = []
LISTAminimo = []
for pos in range(5):
   valores.append(int(input(f'Digite um valor para a posição {pos}: ')))
max = max(valores)
min = min(valores)
print('-='*20)
print(f'Você digitou os valores {valores}')
for indice, valor in enumerate(valores):
    if valor == max:
        vmax = (indice+1)
        LISTAmaior.append(vmax)
    if valor == min:
        vmin = (indice+1)
        LISTAminimo.append(vmin)
print(f'O maior valor digitado foi {max} nas posições: {LISTAmaior}')
print(f'O menor valor digitado foi {min} nas posições: {LISTAminimo}')
