import math
ang = float(input('Digite ângulo desejado:'))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print(f'O seno do ângulo {ang:.2f} é {sen:.2f} e seu cosseno é {cos:.2f} e sua tangente é {tg:.2f}.')
