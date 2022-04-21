vc = float(input('Qual o valor da casa? R$ '))
sal = float(input('Qual o seu salário?R$ '))
temp = int(input('Em quanto tempo você vai pagar em anos? '))
prest = vc/(temp*12)
min = sal * 0.3
if prest < min:
    print(f'Para o salário de R${sal} a prestação é de R${prest} durante {temp} anos \nEmpréstimo Aprovado!')
else:
    print(f'Para o salário de R${sal} a prestação é de R${prest} durante {temp} anos \nEmpréstimo negado!')
