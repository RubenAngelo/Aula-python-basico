from cliente import Cliente
from conta import Conta
from banco import Banco

print('\nBem vindo ao UwU Bank'
      '\n\n-------------------------------------------------------'
      '\n\nAgora vamos fazer seu cadastro de cliente UwU'
      '\n\n-------------------------------------------------------\n')

while True:

    while True:
        uwubank = Banco(input('Ola, por favor, digite seu nome completo > ').upper())
        if uwubank.cadastro == '':
            print('\n* Não deixe o nome em branco *\n')
        elif ' ' in uwubank.cadastro:
            break
        else:
            print('\n* Por favor seu nome completo *\n')
    nomenome = uwubank.cadastro
    nomesep = nomenome.split(' ')
    primeironome = nomesep[0].lower()
    primeironome1 = primeironome.split(primeironome[0])
    primeironome2 = primeironome1[1]
    nomecerto = primeironome[0].upper() + primeironome2
    while True:
        uwubank_idade = uwubank.idade(input(f'Quantos anos voce tem {nomecerto}? > '))
        if uwubank_idade == '':
            print(f'\n* {nomecerto}, não deixe sua idade em branco *\n')
        elif int(uwubank_idade) < 18:
            print(f'\n* {nomecerto}, voce é muito novo pra estar aqui *\n')
        else:
            break
    while True:
        uwubank_cpf = uwubank.cpf(input(f'{nomecerto}, digite seu cpf > '))
        if uwubank_cpf == '':
            print(f'\n* {nomecerto}, não deixe seu cpf em branco *\n')
        elif len(uwubank_cpf) < 11 or len(uwubank_cpf) > 11:
            print(f'\n* {nomecerto}, digite um cpf valido *\n')
        else:
            break
    while True:
        uwubank_senha = uwubank.senha(input(f'{nomecerto}, crie uma senha para sua conta UwU > '))
        if uwubank_senha == '':
            print(f'\n* {nomecerto}, não deixe sua senha em branco *\n')
        else:
            break

    if uwubank.cadastro == '' and uwubank_idade == '' and uwubank_cpf == '' and uwubank_senha == '':
        print(f'\n* Preencha o cadastro *\n')
    elif uwubank.cadastro == '' or uwubank_idade == '' or uwubank_cpf == '' or uwubank_senha == '':
        print(f'\n* voce esqueceu de preencher alguma coisa *\n')
    else:
        break

user = Cliente(uwubank.cadastro, int(uwubank_idade), uwubank_cpf, uwubank_senha)

print(f'\n-------------------------------------------------------'
      f'\n\n{nomecerto}, agora voce vai fazer login no nosso sistema UwU'
      f'\n\n-------------------------------------------------------\n')

while True:
    conf_cpf = input(f'{nomecerto}, digite seu cpf para fazer login em sua conta UwU > ')
    conf_sen = input(f'{nomecerto}, a sua senha agora > ')

    if conf_cpf == uwubank_cpf and conf_sen == uwubank_senha:
        break
    elif conf_cpf == '' and conf_sen == '':
        print(f'\n* {nomecerto}, digite o cpf e a senha *\n')
    elif conf_cpf == '':
        print(f'\n* {nomecerto}, esqueceu o cpf *\n')
    elif conf_sen == '':
        print(f'\n* {nomecerto}, esqueceu a senha *\n')
    elif conf_cpf != uwubank_cpf and conf_sen != uwubank_senha:
        print(f'\n* {nomecerto}, esqueceu o cpf e senha *\n')
    elif conf_cpf != uwubank_cpf:
        print(f'\n* {nomecerto}, voce digitou seu cpf errado *\n')
    elif conf_sen != uwubank_senha:
        print(f'\n* {nomecerto} voce digitou a senha errada *\n')

print(f'\n-------------------------------------------------------\n\n'
      f'{nomecerto}, agora vamos mexer na sua conta UwU\n\n'
      f'-------------------------------------------------------\n')

cont = Conta(float(input(f'{nomecerto}, digite o valor que voce quer transferir de um banco antigo para'
                         f' o UWU Bank > ')))

while True:
    dif_cont = int(input(f'\n{nomecerto}'
                         f'\nDigite 1: Para depositar o valor que voce deseja.'
                         f'\nDigite 2: Para sacar o valor que voce deseja.'
                         f'\nDigite 3: Para consultar seu saldo.'
                         f'\nDigite 4: Para conferir suas informações.'
                         f'\nDigite 5: Para sair do sistema.'
                         f'\n\n > '))
    if dif_cont == 1:
        cont_dep = cont.depositar(float(input(f'\n{nomecerto}, digite o valor para depositar > ')))
    elif dif_cont == 2:
        cont.sacar(float(input(f'\n{nomecerto} digite o valor para sacar > ')))
    elif dif_cont == 3:
        cont_consu = cont.saldo
        print(f'\n------------------ {nomecerto}o seu saldo é de {cont_consu} R$ ------------------')
    elif dif_cont == 4:
        print(f'\n------------------ Suas informações ---------------------'
              f'\n\n------------------ NOME: {user.nome} ------------------'
              f'\n------------------ IDADE: {int(user.idade)} ------------------'
              f'\n------------------ CPF: {user.cpf} ------------------'
              f'\n------------------ SENHA: {user.senha} ------------------')
    elif dif_cont == 5:
        print(f'\n{nomecerto}, ate a proxima')
        break
    else:
        print(f'\n------------------ * {nomecerto}, numero não identificado * ------------------')
