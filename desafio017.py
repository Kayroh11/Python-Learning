import math

catOp = float(input('Informe o comprimento do cateto oposto: '))
catAdj = float(input('Informe o comprimento do cateto adjacente: '))

print('A hipotenuza do triângulo em questão é: {:.2f}'.format(math.hypot(catOp,catAdj)))