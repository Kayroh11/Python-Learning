print('-=-'*16)
print('Bem vindo ao programa de demonstração de termos!')
print('-=-'*16)

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão desejada: '))
cont = 1
numterm = int(input('Digite a quantidade de termos que deseja visualizar: '))

while cont <= numterm:
    print(termo, '->', end=' ')
    termo += razao
    cont += 1
    if cont == numterm + 1:
        cont = 1
        numterm = int(input('Digite quantos números a mais deseja ver. Caso não deseje, digite 0: '))
        if numterm == 0:
            print('Fim do programa')