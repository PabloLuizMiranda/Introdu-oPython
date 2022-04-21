from random import randint
from operator import itemgetter
jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}
rank = dict()
for key, valor in jogo.items():
    rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for posicao, valor in enumerate(rank):
    print(f'{posicao+1}° lugar: {valor[0]} com {valor[1]}.')
