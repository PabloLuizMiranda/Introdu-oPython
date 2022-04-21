from datetime import date
ano = date.today().year
cont = 0
for c in range(1, 8):
    ano = str(input(f'Em que ano a {c}° pessoa nasceu: '))
    idade = date.today().year - int(ano)
    if idade >= 18:
        cont += 1
print(f'Ao todo tiveram: '
      f'\n{cont} pessoas maiores de idade.'
      f'\nE '
      f'\ntambém {7-cont} menores de idade.')
