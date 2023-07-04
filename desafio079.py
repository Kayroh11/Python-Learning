numList = list()
numDig = 0

while True:
    numDig = int(input('Digite o número desejado: '))

    if numDig in numList:
        print('Esse número já foi digitado. Por gentileza digite outro: ')
    elif numDig not in numList:
        numList.append(numDig)

    resp = str(input('Deseja continuar? [S/N] ').upper().strip()[0])
    if resp == 'N':
        break

print(f'Esses foram os valores digitados em ordem: {sorted(numList)}')
