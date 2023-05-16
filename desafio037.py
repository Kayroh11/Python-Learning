numDig = int(input('Digite o número pra conversão: '))
opConv = int(input('Digite 1 se deseja converter o número pra binário, 2 pra octagonal e 3 pra hexadecimal: '))
binario = bin(numDig)
octagonal = oct(numDig)
hexadecimal = hex(numDig)

if opConv == 1:
    print('{} convertido em binário é: {}'.format(numDig, binario))
elif opConv == 2:
    print('{} convertido em octagonal é: {}'.format(numDig, octagonal))
else:
    print('{} convertido em hexadecimal é: {}'.format(numDig, hexadecimal))
