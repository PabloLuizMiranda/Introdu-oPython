from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['Ano de nascimento'] = datetime.now().year - int(input('Ano de nascimento: '))
dados['Carteira de trabalho'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['Carteira de trabalho'] == 0:
    print('='*20)
    print(f'- O nome é {dados["Nome"]}. ')
    print(f'- A idade é {dados["Ano de nascimento"]} anos.')
    print(f'- CTPS tem valor 0.')

else:
    dados['Ano de contratação'] = int(input('Ano de contração: '))
    dados['Sálario'] = float(input('Sálario: R$ '))
    dados['Aposentadoria'] = (dados['Ano de nascimento'] + dados['Ano de contratação'] + 35) - datetime.now().year
    print('='*20)
    print(f'- O nome é {dados["Nome"]}. ')
    print(f'- A idade é {dados["Ano de nascimento"]} anos.')
    print(f'- CTPS tem o valor de {dados["Carteira de trabalho"]}.')
    print(f'- O ano de contratação foi {dados["Ano de contratação"]}.')
    print(f'- O sálario tem o valor de R$ {dados["Sálario"]}.')
    print(f'- A aposentadoria será em {dados["Aposentadoria"]} anos.')

#for k, v ini dados.items(): isso vai pegar a key e o valor de cada item e fazer o for
#Logo, terá uma linha para cada item.