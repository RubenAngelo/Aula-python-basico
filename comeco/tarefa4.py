list_num = [1,50,0,40000000000]

def maior_numero(lista):
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    print(maior)

def menor_numero(list):
    menor = list[0]
    for item in list:
        if menor > item:
            menor = item
    print(menor)

maior_numero(list_num)
menor_numero(list_num)
