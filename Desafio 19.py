import random
al1 = str(input('Digite o nome do primeiro aluno: '))
al2 = str(input('Digite o nome do segundo aluno: '))
al3 = str(input('Digite o nome do tercero aluno: '))
al4 = str(input('Digite o nome do quarto aluno: '))
alunos = [al1, al2, al3, al4]
sort = random.choice(alunos)
print(f'O aluno sorteado foi {sort}')
