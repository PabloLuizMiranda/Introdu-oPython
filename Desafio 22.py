nome = str(input('Digite seu nome completo: ')).strip()
div = nome.split()
print(f' Prazer em te conhecer {nome}!'
      f'\n Seu nome com as letras maiúsculas fica assim: {nome.upper()}'
      f'\n Seu nome com as letras minúsculas fica assim: {nome.lower()}'
      f'\n Seu nome possui {len(nome) - nome.count(" ")} letras'
      f'\n Seu primeiro nome possui {len(div[0])} letras')
