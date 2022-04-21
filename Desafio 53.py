frase = str(input('Insira a frase: ')).strip().upper()
lista = frase.split()
fras = ''.join(lista)
invert = ''.join(lista)[::-1]
if fras == invert:
    print(f'A frase {frase} é um palindromo!')
else:
    print(f'A frase {fras} não é um palindromo!')
