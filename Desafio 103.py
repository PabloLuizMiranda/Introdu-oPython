def dados(n="<desconhecido>", g=0):
    print(f'O jogador {n} fez {g} gol(s).')


# Programa principal.
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    n = '<desconhecido>'
dados(n, g)
