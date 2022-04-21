def fatorial(num, show=False):
    """fatorial(num, show=False)
        Calcula o fatorial de um número
        :param num: O número a ser calculado
        :param show:(Opc) Mostrar ou não a conta.
        :return: O valor fatorial de um número num."""
    f = 1
    if show:
        for c in range(num, 0, -1):
            f *= c
            if c > 1:
                print(f'{c}', end=' x ')
            else:
                print(f'{c}', end=' = ')
        return f'{f}'
    else:
        for c in range(num, 0, -1):
            f *= c
        return f'{f}'


# Programa principal.
print(fatorial(5, True))
help(fatorial)
