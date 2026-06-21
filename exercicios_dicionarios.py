# Exercicio 1
# import os
# os.system('cls')
# pessoas = [
#     {'nome': 'Eduardo', 'idade': '20', 'cidade': 'Goiânia'},
#     {'nome': 'Maria Eduarda', 'idade': '19', 'cidade': 'Goiânia'},
#     {'nome': 'Mario', 'idade': '22', 'cidade': 'Porangatu'},
#     {'nome': 'Maria Eduarda', 'idade': '67', 'cidade': 'Anápolis'},
#     {'nome': 'Jordana', 'idade': '19', 'cidade': 'Trindade'}
# ]

# pesquisa = 'Maria Eduarda'
# encontrado = False

# for pessoa in pessoas:
#     if pessoa['nome'] == pesquisa:
#         print(pessoa)
#         encontrado = True

# if not encontrado:
#     print('Nenhum resultado.')

# -----------------------------------------------------

# Exercicio 2
# import os
# os.system('cls')
# pessoas = {'nome': 'Eduardo', 'idade': '20', 'cidade': 'Goiânia'}

# pessoas['idade'] = '21' # Alterando um dado de um dicionario
# pessoas['profissao'] = 'Estagiário' # Acidionando um dado 
# del pessoas['cidade'] # Removendo um item do dicionario

# print(pessoas)

# -----------------------------------------------------

# Exercicio 3
# import os
# os.system('cls')
# numeros_quadrados = {x: x**2 for x in range(1, 6)} # Cria um loop para ter o quadrado de cada número
# print(numeros_quadrados)

# -----------------------------------------------------

# Exercicio 4
# import os
# os.system('cls')
# pessoas = {'nome': 'Eduardo', 'idade': '20', 'cidade': 'Goiânia'}

# if 'nome' in pessoas:
#     print('Esta chave existe dentro do dicionário')
# else:
#     print('Esta chave não existe dentro do dicionário')

# -----------------------------------------------------

# Exercicio 5
# import os
# os.system('cls')
# frase = input('Escreva uma frase: ')
# contagem_de_palavras = {}
# palavras = frase.split()
# for palavra in palavras:
#     contagem_de_palavras[palavra] = contagem_de_palavras.get(palavra, 0) + 1
# print(contagem_de_palavras)