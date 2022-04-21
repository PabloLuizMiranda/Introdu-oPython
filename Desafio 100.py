from random import randint


def sortear(num):
    lista = list()
    for num in range(num):
        r = randint(1, 21)
        lista.append(r)
    print(f'Sorteando {num + 1} da lista: {lista} PRONTO! ')
    par(lista)


def par(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    print(f'Somando os valores pares de {lista}, temos {soma}')


# Programa principal.
num = int(input('Quantos valores você quer sortear: '))
sortear(num)
