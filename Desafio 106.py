def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', cor='azul')
    print(cores['branco'])
    help(com)
    print(end=cores['sem'])


def título(msg, cor='sem'):

    tam = len(msg) + 6
    print(end=cores[cor])
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(end=cores['sem'])


# Programa Principal
cores = {'sem': '\033[m',
         'vermelho': '\033[1;41m',
         'verde': '\033[1;42m',
         'azul': '\033[1;44m',
         'branco': '\033[7m'}

while True:
    título('SISTEMA DE AJUDA PyHELP', cor='verde')
    comando = input('Função ou Biblioteca > ')
    if comando.upper() == 'FIM':
        break
    ajuda(comando)
título('ATÉ LOGO!', cor='vermelho')
