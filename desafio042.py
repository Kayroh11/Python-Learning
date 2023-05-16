l1 = float(input('Digite o tamanho do primeiro lado do triângulo: '))
l2 = float(input('Digite o tamanho do segundo lado do triângulo: '))
l3 = float(input('Digite o tamanho do terceiro lado do triângulo: '))

if l1 + l2 > l3 and l3 + l1 > l2 and l1 + l3 > l2:
    print('A figura pode formar um triângulo ', end='')
    if l1 == l2 == l3:
        print('EQUILÁTERO.')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO.')
    elif l1 == l2 != l3 or l2 == l3 != l1:
        print('ISÓSCELES.')
else:
    print('A figura não pode formar um triângulo.')

