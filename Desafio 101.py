def voto(nasc):
    from datetime import date  # Para importações usadas apenas na função, use dentro do def (economiza memoria)
    atual = date.today().year
    idade = atual - nasc
    if 16 <= idade <= 17 or idade > 65:
        return f'Com {idade} anos. O voto é OPCIONAL.'
    elif 18 <= idade <= 60:
        return f'Com {idade} anos. O voto é OBRIGATORIO.'
    else:
        return f'Com {idade} anos. O voto é NEGADO.'


# Programa principal.
nasc = int(input('Ano de nascimento: '))
print(voto(nasc))
