# Aula 2 - Variáveis, tipos, entrada, saída e operadores matemáticos ---------------------------------------------------
#
# print('Hello World!')
# print('Segundo print')
# print('Hello world! Segundo print')
# print('Hello world!\nSegundo print')
# print('Hello world!\tSegundo print')
#
# nome = 'Guilherme'
# idade = 27
# altura = 1.78
# tipo_nome = type(nome)
# tipo_idade = type(idade)
# tipo_altura = type(altura)
# frase = nome + ' tem ' + str(idade) + ' anos e ' + str(altura) + ' de altura'
#
# print(nome)
# print(idade)
# print(altura)
# print(tipo_nome)
# print(tipo_idade)
# print(tipo_altura)
#
# print(f'{nome}\n{tipo_nome}\n{idade}\n{tipo_idade}\n{altura}\n{tipo_altura}')
# print(nome + ' tem ' + str(idade) + ' anos e ' + str(altura) + ' de altura')
# print(frase)
# print(f'{nome} tem {idade} anos e {altura} de altura')
#
# nome = input('Escreva seu nome: ')
# idade = input('Escreva sua idade: ')
# altura = input('Escreva sua altura: ')
#
# print(f'{nome} tem {idade} anos e {altura} de altura')
# print(type(nome), type(idade), type(altura))
#
# numero1 = 27
# numero2 = 53
# resultado = numero1 + numero2
#
# print(resultado)

# Aula 3 - Operadores lógicos e estruturas de decisões (IF e ELSE) -----------------------------------------------------

# var_verdade = True
# var_falso = False
#
# print(type(var_verdade), type(var_falso))
#
#
# var_verdade = True
# var_falso = False
#
# if var_verdade == True:
#     print(f'Var_verdade é: {var_verdade}')
#
# if True:
#     print(f'Var_verdade é: {var_verdade}')
#
# if False:
#     print(f'Var_verdade é: {var_verdade}')
#
#
# a = 2
# b = 20
#
# if a > b:
#     print(f'{a} é maior do que {b}')
# else:
#     print(f'{a} não é maior do que {b}')
#
# if b > a and 'abacaxi' == 'uva':
#     print(f'{a} é maior do que {b}')
# else:
#     print('Não deu certo ')
#
# if (a > b and 'joao' == 'maria') or 2 == 2:
#     print('Deu certo')
# else:
#     print('Não deu certo')
#
# print(not True)
#
# idade = 50
#
# if not idade == 50:
#     print('Voce não tem 50 anos')
# else:
#     print('Voce tem 50 anos')
#
#
# print('Menu: '
#       '\n1 = Escreve Guilherme'
#       '\n2 = Escreve João'
#       '\n3 = Escreve Maria')
#
# opcao = input('Escolha um opção: ')
#
# if opcao == '1':
#     print('Guilherme')
# elif opcao == '2':
#     print('João')
# elif opcao == '3':
#     print('Maria')
# else:
#     print('opção invalida')

# Aula 4 - Strings e listas --------------------------------------------------------------------------------------------

# lista_nomes = ['joao', 'maria', 'guilherme', 'diego']
# frase = 'Oi, tudo bem?'
#
# print(frase)
# print(frase[0])
# print(frase[0:5])
# print(frase[0:13:2])
# print(frase[::-1])
# print(frase.lower())
# print(frase.upper())
# frase_separada = frase.split(',')
# print(frase_separada)
# print(frase_separada[0])
# frase_nova = frase + ' Como vai voce?'
# print(frase_nova)
# print(f'\n{type(lista_nomes)}')
# print(lista_nomes[0])
# print(lista_nomes)
# print(lista_nomes[0:3])
# print(lista_nomes[-1])
# lista_nomes.append('Geralda')
# print(lista_nomes)
# lista_nomes.remove('maria')
# print(lista_nomes)
# lista_nomes.insert(1, 'Luis')
# print(lista_nomes)
# lista_nomes[0] = 'Julia'
# print(lista_nomes)
# print(lista_nomes.pop())
# print(lista_nomes)
# contador = lista_nomes.count('Julia')
# print(contador)
# print(len(lista_nomes))
# lista_nomes.clear()
# print(lista_nomes)

# Aula 5 - Estruturas de laço (WHILE e FOR) ----------------------------------------------------------------------------

# nomes = ['Guilherme', 'Marcelo', 'João', 'Julia']
#
# for nome in nomes:
#     print(nome)
#
# lista_numeros = range(5, 10, 2)
#
# for item in lista_numeros:
#     print(item)
#
# for i in range(len(nomes)):
#     print(nomes[i])
#     nomes.append('oii')
#
#
# palavra = 'guilherme Junqueira'
#
# for letra in palavra:
#     print(letra)
#
#
# i = 0
#
# while i < 10:
#     print(f'i ainda é menor que 10 {i}')
#
#     i += 1
#
# print(f'Acabou o while: {i}')
#
# while i < 10 and 10 == 10:
#     print(f'i ainda é menor que 10 {i}')
#
#     i += 1
#
# print(f'Acabou o while: {i}')
#
# while True:
#     print(f'i ainda é menor que 10: {i}')
#
#     if i > 8:
#         break
#     i += 1
#
# print(f'Acabou o while: {i}')

# Aula 6 - Tuplas, dicionários e conjuntos -----------------------------------------------------------------------------

# minha_lista = ['Gui', 'joao']               #List: varias coisas dentro, sempre ordenado, mutavel,
#                                             # um objeto de cada vez, ifinita.
#
# minha_tupla = ('Gui', 'joao')               #Tuple: Não é mutavel, pegar valor, modificar valor.
#
# meu_dicionario = {'nome': 'Guilherme', 'idade': 27}             #Dict: uma chave e um valor, mutavel.
#
# meu_conjunto = {'Gui', 'joao'}              #Set: Não existe itens repetidos, mutavel, não tem ordem.
#
# print(type(minha_tupla))
# print(minha_tupla[0])
# print(meu_dicionario)
# print(meu_dicionario['nome'])
#
# if 'Guilhermme' in meu_dicionario.values():
#     print('Guilherme esta no dicionario')
#
# for chaves in meu_dicionario.keys():
#     print(chaves)
#
# meu_dicionario['endereço'] = 'Rua dois'
# print(meu_dicionario)
# meu_dicionario.pop('endereço')
# print(meu_dicionario)
# print(meu_conjunto)
# meu_conjunto.add('Maria')
# print(meu_conjunto)
# if 'Gui' in meu_conjunto:
#     print('Foi encontrado')
#
#
# lista = []
# tupla = ()
# dicionario = {}
# conjunto = set()
# loucura = [(1,2), (3,4), (5,6), ({'joao', 'maria'}, {'gabriel'})]

# Aula 7 - Funções e Métodos -------------------------------------------------------------------------------------------

# def soma(numero1, numero2):
# resp = numero1 + numero2
# return resp
#
# retorno = soma(75, 1289)
#
# print(retorno)
#
#
# def imprime_oi():
# print('OI')
#
# imprime_oi()
#
#
# def tem_sete_itens(argumento):
# if len(argumento) == 7:
#     return True
# else:
#     return False
#
# print(tem_sete_itens('fala'))
#
# if tem_sete_itens('1234567'):
# print('realmente tem sete itens')
#
# # Aula 8 - Argumentos de linha de comando ----------------------------------------------------------------------------
#
# def exemplo1A8():
# import sys
#
# argumentos = sys.argv
#
# def soma(n1, n2):
#     return n1 + n2
#
# def sub(n1, n2):
#     return n1 - n2
#
# if argumentos[1] == 'soma':
#     resp = soma(float(argumentos[2]), float(argumentos[3]))
# elif argumentos[1] == 'sub':
#     resp = sub(float(argumentos[2]), float(argumentos[3]))
#
# print(resp)

# Aula 10 - Entrada e saída de arquivos --------------------------------------------------------------------------------

# open('arquivo.txt', 'r')                 Ler o arquivo
# open('arquivo.txt', 'w')                 Escrever o arquivo
# open('arquivo.txt', 'r+')                Ler e escrever arquivo
# open('arquivo.txt', 'a')                 Adicionar ao arquivo
# open('arquivo.txt', 'b')                 Abrir arquivo que não é de texto
# open('arquivo.txt', 'rb')                Ler o arquivo que não é de texto
#
#
# arquivo = open('arquivo.txt', 'w')
# arquivo.write('E ai pessoal')
# for i in range(0, 1001):
#     arquivo.write('Numero'+str(i)+'\n')
#
# :
# arquivo = open('arquivo.txt', 'a')
# arquivo.write('E ai pessoal')
# for i in range(0, 1001):
#     arquivo.write('Numero' + str(i) + '\n')
#
#
# arquivo = open('arquivo.txt', 'r')
# print(arquivo.read())
# for linha in arquivo:
#     print(linha)
#
#
# arquivo = open('arquivo.png', 'rb')
# print(arquivo.read())

# Aula 11 - Tratamentos de erros e exceções (TRY e EXCEPT) -------------------------------------------------------------

# def abre_arquivo():
#     try:
#         arquivo = open('arquivo.txt')
#         return True
#     except NameError:
#         print('Voce digtou alguma coisa errada')
#     except ZeroDivisionError:
#         print('Divisão por zero, não da pra fazer')
#     except Exception as erro:
#         print(f'Aconteceu algum erro {erro}')
#     except:
#         print('Erro desconhecido')
#         return False
#
# while not abre_arquivo():
#     print('tentando abrir o arquivo')
#
# print('Arquivo aberto')

# Aula 12 - Bibliotecas, PIP e Requisições Web -------------------------------------------------------------------------

# import requests
#
# cabecalho = {'User-agent': 'windows 12', 'Referer': 'https://google.com', 'cf-ipcountry': 'us'}
#
# meus_cookies = {'Ultima-visita': '10-10-2020'}
#
# dados = {'username': 'guigui', 'password': 'guigui123'}
#
# texto = None
#
# try:
#     requisicao = requests.post('http://putsreq.com/', headers=cabecalho, cookies=meus_cookies, data=dados)
#
#     texto = requisicao.text
#
# except Exception as e:
#     print(f'Requesição de erro {e}')
#
# print(texto)

# Aula 13 - API, JSON e consultando listas de filmes -------------------------------------------------------------------

# import requests
# import json
#
# def requisicao(titulo):
#     try:
#         req = requests.get('http://www.omdbapi.com/?t=' + titulo + '&type=movie')
#         dicionario = json.loads(req.text)
#         return dicionario
#     except:
#         print('Erro na conexão')
#         return None
#
# def printar_detalhes(filme):
#     print('Titulo: ', filme['Title'])
#     print('Ano: ', filme['Year'])
#     print('Diretor: ', filme['Diretor'])
#     print('Atores: ', filme['Actors'])
#     print('Nota: ', filme['imdbRating'])
#     print('Premios: ', filme['Awards'])
#     print('Poster: ', filme['Poster'])
#
# sair = False
# while not sair:
#     op = input('Escreva o nome de um filme ou SAIR para fechar: ')
#
#     if op == 'SAIR':
#         sair = True
#         print('Saindo...')
#     else:
#         filme = requisicao(op)
#         if filme['Response'] == 'False':
#             print('Filme não encontrado')
#         else:
#             printar_detalhes(filme)

# Aula 14 - Expressões regulares, procurando por e-mails ---------------------------------------------------------------

# import requests
# import re
#
# https//regex101.com
# string = 'o gatos é bonito'
# string1 = 'o gato, a gata, os gatinhos, os gatoes e gat'
#
# padrao = re.search(r'gat.', string)
# padrao1 = re.search(r'gat\w\w', string)
# padrao2 = re.findall(r'gat\w+', string1)
# padrao3 = re.findall(r'gat\w*', string1)
# padrao4 = re.findall(r'[gat]', string1)
# padrao5 = re.findall(r'[gat]+', string1)
# padrao6 = re.findall(r'[gat]+\w+', string1)
#
# if padrao:
# print(padrao.group())
# print(padrao1.group())
# print(padrao2)
# print(padrao3)
# print(padrao4)
# print(padrao5)
# print(padrao6)
# else:
# print('Padrão não encontrado')
#
#
# requisicao = requests.get('https://loucosporcoxinha.com.br/')
#
# padrao7 = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao.text)
#
# if padrao7:
# print(padrao7)
# else:
# print('Padrão não encontrado')
