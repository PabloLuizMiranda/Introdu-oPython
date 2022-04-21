frase = str(input('Insira a expressão: '))
frase.count('(')
frase.count(')')
if frase[0] == ')' and frase[-1] == '(':
    print('Operação invalida!')
elif frase.count('(') == frase.count(')'):
    print('Expressão válida!')
else:
    print('Expressão ínvalida!')
