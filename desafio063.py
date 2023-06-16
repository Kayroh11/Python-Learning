print('Bem vindo ao programa que mostra a sequência de Fibonacci :)')

n1 = 0
n2 = 1
n3 = n1 + n2
n4 = 0
ntermos = int(input('Digite a quantidade de termos que deseja visualizar: '))
cont = 1

while cont <= ntermos:
    if cont == 1:
        print(n1, ' -> ', end=' ')
    if cont == 2:
        print(n2, " -> ", end=' ')
    if cont > 2:
        print(n3, ' -> ', end=' ')
        n4 = n3
        n3 += n2
        n2 = n4
    cont += 1

print('FIM')
