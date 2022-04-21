maior = 0
menor = 0
for c in range(1, 5):
    peso = float(input(f'Insira o peso da {c}° pessoa: '))
    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print(f'O maior peso lido é o {maior}kg.\nO menor peso lido foi o {menor}kg.')
