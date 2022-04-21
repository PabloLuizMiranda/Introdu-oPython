tabela = ('América', 'Athetico', 'Atlético', 'Atlético-MG', 'Avaí', 'Botafogo', 'Ceará'
          'Corinthians', 'Coritiba', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza',
          'Goiás', 'Internacional')
tabel = print(f'Lista de times do brasileirão {tabela}:')
print('='*200)
cincoprimeiros = print(f'Os cinco primeiros times são: {tabela[0:5]}.')
print('='*200)
ultimosquatro = print(f'Os últimos quatro times são: {tabela[-4:]}.')
print('='*200)
alfa = print(f'A lista em ordem alfabética: {sorted(tabela)}')
print('='*200)
cuiaba = print(f'O Cuiabá se emcontra na {tabela.index("Cuiabá")+1}° posição.')
