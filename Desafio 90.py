aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
print('='*20)
print(f'- O nome do aluno é {aluno["nome"]}.')
print(f'- A média foi {aluno["media"]}.')
print(f'A situação do aluno é: ', end='')
if aluno["media"] < 5:
    aluno['situação'] = 'REPROVADO'
    print(aluno["situação"])
elif 5 <= aluno["media"] <= 6.9:
    aluno['situação'] = 'RECUPERAÇÃO'
    print(aluno["situação"])
else:
    aluno['situação'] = 'APROVADO'
    print(aluno["situação"])
print(aluno)
print(type(aluno))