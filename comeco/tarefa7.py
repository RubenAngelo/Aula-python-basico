import requests
import json

while True:

    op = input('\nDigite: 1 - Para ver a cotação do dolar\n'
                 'Digite: 2 - Para ver o clima\n'
                 'Digite: 3 - Para sair\n\n'
                 '> ')

    if op == '1':
        try:
            requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')

            dicionario = json.loads(requisicao.text)

            list = dicionario['USDBRL'] ['high']

            print(f'\nValor do Dolar: {list} Reais')

        except:
            print('Falha na conexão')

    elif op == '2':
        try:
            cidade = input('\nDigite o nome de qualquer estado ou cidade do mundo: ')

            requisicao1 = requests.get(f'https://weather.contrateumdev.com.br/api/weather/city/?city={cidade}')

            dicionario1 = json.loads(requisicao1.text)

            list1 = dicionario1

            if list1['cod'] == '400':
                print('\nCidade ou estado não encontrado')
            else:
                temperatura = list1['main']['temp']
                temperatura_max = list1['main']['temp_max']
                temperatura_min = list1['main']['temp_min']
                temperatura_sen = list1['main']['feels_like']
                temperatura_tip = list1['weather'][0]['description']

                print(f'\nTemperatura: {temperatura}°C')
                print(f'Temperatura maxima: {temperatura_max}°C')
                print(f'temperatura minima: {temperatura_min}°C')
                print(f'Sensação termica: {temperatura_sen}°C')
                print(f'Clima: {temperatura_tip}')
        except:
            print('Falha na conexão')

    elif op == '3':
        break

    else:
        print('\nNumero invalido')
