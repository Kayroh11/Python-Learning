
print('=-='*3,'Comparação de números','=-='*3)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O número {} é maior que o número {}'.format(n1, n2))
elif n1 < n2:
    print('O número {} é menor que o número {}'.format(n1,n2))
else:
    print('Não existe maior, os números são iguais')