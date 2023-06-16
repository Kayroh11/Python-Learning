inicia = True
qtNumeros = 0
soma = 0
while inicia == True:
    nDig = int(input('Digite um número: [999 para parar]: '))
    if nDig != 999:
        qtNumeros += 1
        soma += nDig
    if nDig == 999:
        inicia = False



print('Você digitou {} números, a soma deles é: {}.'.format(qtNumeros, soma))