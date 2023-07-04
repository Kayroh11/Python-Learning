lista = []
qtNum = 0

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    qtNum += 1
    q = str(input('Quer continuar? [S/N] ').upper().strip()[0])
    if q == 'N':
        break
print(f'Essa é a lista completa: {lista}')
print(f'Foram digitados {qtNum} números. A lista em ordem decrescente fica {sorted(lista, reverse=True)}.', end=' ')
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')
