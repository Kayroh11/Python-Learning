digitTres = 3

numDig = (int(input('Digite o primeiro número: ')),
          int(input('Digite o segundo número: ')),
          int(input('Digite o terceiro número: ')),
          int(input('Digite o quarto número: ')))
print(f'Você digitou a seguinte sequência: {numDig}')

print(f'O número 9 apareceu {numDig.count(9)} vezes.')

if 3 in numDig:
    print(f'O número 3 foi digitado a primeira vez na posição {numDig.index(3) + 1}.')
else:
    print('O número 3 não foi digitado nenhuma vez.')

print(f'Os números pares digitados foram: ', end=' ')
for par in range(len(numDig)):
    if numDig[par] % 2 == 0:
        print(numDig[par], end=' ')
