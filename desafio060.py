n1 = int(input('Digite o número pra ver seu fatorial: '))
fatorial = n1 - 1
resultado = (n1 * fatorial)
print('{}! = {} x'.format(n1, n1), end='')

while fatorial > 1:
    print(' {} x'.format(fatorial), end='')
    fatorial = fatorial - 1
    resultado *= fatorial
print(' {} ='.format(fatorial), end=' ')
print('{}'.format(resultado))
