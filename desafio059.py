"""Programa que lê dois valores e mostre um menu da seguinte forma:
[1]somar

[2]multiplicar

[3]maior

[4]novos números

[5]sair do programa"""


N1 = int(input('Digite o primeiro número: '))

N2 = int(input('Digite o segundo número: '))

Execute = True

Operacao = 0

while Execute == True:
    if Operacao == 0:
        print('Bem vindo ao programa de operações. As opções são: ')
        Operacao += 1
    print(""" 
    [1] somar 
    [2] multiplicar 
    [3] mostrar o maior 
    [4] digitar novos números 
    [5] sair do programa""")
    Opcaodigitada = int(input('\nDigite a opção desejada: '))
    if Opcaodigitada == 1:
        print('\nO resultado da soma é: {}!'.format(N1 + N2))

    elif Opcaodigitada == 2:
        print('\nO resultado da multiplicação é: {}!'.format(N1 * N2))

    elif Opcaodigitada == 3:
        if N2 < N1:
            print('\n{} é maior que {}!'.format(N1, N2))

        elif N2 > N1:
            print('\n{} é maior que {}!'.format(N2, N1))

    elif Opcaodigitada == 4:
        N1 = int(input('\nDigite o primeiro número: '))
        N2 = int(input('\nDigite o segundo número: '))

    elif Opcaodigitada == 5:
        Execute = False

print('\nFim da execução do programa, espero que tenha aproveitado suas funcionalidades!')

