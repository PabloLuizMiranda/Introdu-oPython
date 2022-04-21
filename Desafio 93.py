dados = dict()
gols = list()
dados['nome'] = str(input('Nome do jogador: ')).capitalize()
partidas = int(input(f'Quantas partidas o {dados["nome"]} jogou? ')) + 1
tot = cont = 0
for c in range(1, partidas):
    gol = (int(input(f'Quantos gols na partida {c}: ')))
    tot += gol
    gols.append(gol)
    dados['gols'] = gols
    dados['total'] = tot
print('='*50)
print(dados)
print('='*50)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('='*50)
print(f'O nome do jogador é {dados["nome"]}')
print(f'lista de gols {dados["gols"]}')
print(f'Fez um total de {dados["total"]} gols.')
print('='*50)
print(f'O jogador {dados["nome"]} jogou 5 partidas.')
for j in range(1, partidas):
    print(f'=> Na partida {j}, fez {dados["gols"][cont]} gols')
    cont += 1
print(f'Foi um total de {dados["total"]} gols.')
