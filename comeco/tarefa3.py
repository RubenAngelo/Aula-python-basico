num_c = int(input('Quantas pessoas serão convidadas para a festa: '))

val_c = num_c + num_c

list_c = []

while True:
    list_c.append(input('Digite o nome do convidado: '))

    num_c += 1

    if num_c == val_c:
        break

print(f'\nForam convidados {len(list_c)} pessoas para festa\n\nSão elas:\n')

for nomes in list_c:
    print(nomes)


