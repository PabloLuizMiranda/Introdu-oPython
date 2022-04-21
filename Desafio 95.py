grupo = list()
dados = dict()
gols = list()
tot = 0
while True:
    dados['nome'] = str(input('Nome do jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas o {dados["nome"]} jogou? ')) + 1
    for c in range(1, partidas):
        gol = (int(input(f'Quantos gols na partida {c}: ')))
        gols.append(gol)
        tot += gol
    dados['gols'] = gols[:]
    dados['soma'] = sum(gols)
    gols.clear()
    grupo.append(dados.copy())
    continuar = str(input('Quer continuar?[S/N] '))[0].strip()
    while continuar not in 'SsNn':
        continuar = str(input('Opção invalida. Quer continuar?[S/N] '))[0].strip()
    if continuar in 'Nn':
        break
print('=' * 50)
print(f'cod        Nome       gols                   total')
print('-' * 50)
for p, pessoa in enumerate(grupo):
    print(f'{p} {pessoa["nome"]:>13} {str(pessoa["gols"]).center(15)} {(str(pessoa["soma"])).rjust(18)}')
while True:
    cont = 0
    jogador = int(input('Mostrar dados de qual jogador? (999 para finalizar) '))
    if jogador == 999:
        break
    for numero in (grupo[jogador]['gols']):
        cont += 1
        print(f'    No jogo {cont} fez {numero} gols.')
