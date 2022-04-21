dist = float(input('Qual a distância da viagem em Km? '))
if dist <= 200:
    print(f'O preço da passagem será {dist*0.5:.2f}!')
else:
    print(f'O preço da passagem será {dist*0.45:.2f} devido a uma promoção!')
