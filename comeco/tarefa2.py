idade = int(input('Qual é a sua idade: '))
peso = int(input('Qual é o seu peso: '))
altura = float(input('Qual é a sua altura '))

if idade >= 18 and peso >= 60 and altura >= 1.70:
    print('Voce esta apto para servir ao exercito')
else:
    print('Voce não esta apto para servir ao exercito')
