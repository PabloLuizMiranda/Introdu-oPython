palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM',
            'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR',
            'TRABALHAR', 'MERCADO', 'PROGRAMADOR',
            'FUTURO', 'PRATICAR',)
vogal = 'A', 'E', 'I', 'O', 'U'
for palavra in palavras:
    print(f'\nNa palavra {palavra} tem as vogais: ', end='')
    for letra in palavra:
        if letra in 'AEIOU':
            print(letra, end=' ')
