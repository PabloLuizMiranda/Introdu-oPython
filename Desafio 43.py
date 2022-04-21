peso = float(input('Qual o seu peso?(Kg) '))
altura = float(input('Qual a sua altura?(m) '))
imc = peso / altura ** 2
print(f"O IMC dessa pessoa é: {imc:.1f}")
if imc < 18.5:
    print('Está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Está no peso ideal!')
elif 25 <= imc < 30:
    print('Está em sobrepeso!')
elif 30 <= imc < 40:
    print('Está em obesidade!')
else:
    print('Esta em obesidade mórbida!')
