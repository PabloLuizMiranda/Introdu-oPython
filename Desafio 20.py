from random import sample
al1 = str(input('Insira o nome do primeiro aluno: '))
al2 = str(input('Insira o nome do segundo aluno '))
al3 = str(input('insira o nome do terceiro aluno '))
al4 = str(input('Insira o nome do quarto aluno '))
lista = [al1, al2, al3, al4]
ordem = sample(lista, 4)
print(f'A ordem escolhida foi {ordem}')
