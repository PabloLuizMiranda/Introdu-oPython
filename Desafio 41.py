from datetime import date
atual = date.today().year
ano = int(input('Insira o ano de nascimento do atleta: '))
idade = atual - ano
if idade <= 9:
    print(f'O atleta tem {idade} anos.'
          f'Classificação: Mirim.')
elif idade <= 14:
    print(f'O atleta tem {idade} anos.'
          f"\nClassificação: Infantil.")
elif idade <= 19:
    print(f'O atleta tem {idade} anos.'
          f'Classificação: Junior.')
elif idade <= 25:
    print(f'O atleta tem {idade} anos.'
          f'\nClassificação: Sênior.')
else:
    print(f'O atleta tem {idade} anos.'
          f'\nClassificação: Master.')
