print('=-'*5,'Tabuada','-='*5)
valorDig = int(input('Digite o valor desejado: '))

for multip in range(1, 11):
    result = valorDig * multip
    print('{} * {:2} = {}'.format(valorDig, multip, result))
