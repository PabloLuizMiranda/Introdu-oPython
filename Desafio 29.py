vel = float(input('Qual a velocidade do carro? '))
multa = (vel-80) * 7
if vel <= 80.0:
    print('Está tudo certo! Pode prosseguir e mantenha-se atento!')
    print('MULTADO! Essa velocidade é extremaente perigosa e está acima do limite da rodovia. \nSua multa'
          f'será de {multa:.2f}!!!')
