def notas(*num, sit=False):
    """notas(*n, sit=False)
            Função para analisar rnotas e situações de vários alunos.
            :param num: uma ou mais notas dos alunos (aceita várias)
            :param sit: valor opcional, indicando se deve ou não adicionar a situação)
            :return: dicionário com várias informações sobre a situação da turma."""

    dados = dict()
    tot = maior = menor = soma = 0
    for n in num:
        soma += n
        tot += 1
        if tot ==1:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
    med = soma/tot
    dados['maior'] = maior
    dados['menor'] = menor
    dados['total'] = tot
    dados['soma'] = soma
    dados['média'] = med
    if sit:
        if med < 6:
            dados['situação'] = 'Ruim'
        elif med >= 8:
            dados['situação'] = 'BOM'
        else:
            dados['situação'] = 'MÉDIO'
    return dados


# Programa principal.
aluno1 = notas(6, 2.5, 1.5, 5, sit=True)
print(aluno1)
#help(notas)