lista = []
listaPar = []
listaImpar = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        listaPar.append(n)
    elif n % 2 != 0:
        listaImpar.append(n)

    q = str(input('Quer continuar? [S/N] ').upper().strip()[0])
    if q == 'N':
        break




print(f'Essa foi a lista: {lista}. Essa é a lista dos pares: {listaPar}, essa é a dos ímpares: {listaImpar}')