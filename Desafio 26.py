letra = str(input('Qual letra você quer procurar? ')).upper()
frase = str(input('Digite a frase: ')).upper()
print (f'\nA letra {letra} apareceu: {frase.count(letra)} vezes'
       f'\nA primeira letra {letra} apareceu na posição:{frase.find(letra)+1}'
       f'\nA ultima letra {letra} apareceu na poisção: {frase.rfind(letra)+1}')