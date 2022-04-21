from datetime import date

ano = date.today().year
gen = int(input('[1] Homem.'
                '\n[2] Mulher.'
                '\nQual seu gênero? '))
if gen == 2:
    print('Não existe obrigatoriedade em se alistar.')
    exit()
elif gen == 1:
    nascimento = int(input(f'Ano de nascimento: '))
    final = ano - nascimento
print(f'Quem nasceu em {nascimento} tem {final} anos em {ano}.')
if final < 18:
    print(f'Ainda faltam {18 - final} para se alistar.'
          f'\nSeu alistamento será em {ano + (18 - final)}')
elif final == 18:
    print('Vá se alistar imediatamente!')
else:
    print(f'Você já deveria ter se alistado há {final - 18} anos.'
          f'\nSeu alistamento foi em {ano + (18 - final)}.')
