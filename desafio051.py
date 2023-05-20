numDig = int(input('Digite o número desejado: '))
razao = int(input('Digite a razão: '))
decimo = numDig + (10 - 1) * razao

for i in range (numDig, decimo + razao, razao):
    print(i, end=' -> ')

print('Acabou')