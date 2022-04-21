print('-=' * 20)
print('Analisar lados de um triangulo')
print('-=' * 20)
lado1 = float(input('Insira o primeiro lado: '))
lado2 = float(input('Insira o segundo lado: '))
lado3 = float(input('Insira o terceiro lado: '))
if lado1 + lado2 > lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('É um triângulo')
else:
    print('Não é triângulo')
