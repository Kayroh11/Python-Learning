print('*'*5,'Calculadora de descontos','*'*5)

valProd = float(input('Digite o valor do produto: '))

formPag = int(input("Digite:\n - 1 - pra pagamento à vista no dinheiro/cheque.\n - 2 - pra pagamento à vista no cartão. \n - 3 - pra pagamento em até 2x no cartão. \n - 4 - pra pagar em 3x ou mais no cartão.\n"))

if formPag == 1:
    print('O valor do produto é {} reais, e pagando à vista em dinheiro / no cheque será: {} reais.'.format(valProd, valProd - valProd * 0.10))
elif formPag == 2:
    print('O valor do produto é {} reais, e pagando à vista no cartão será: {} reais.'.format(valProd, valProd - valProd * 0.05))
elif formPag == 3:
    print('O valor do produto é {} reais, pagando em 2x no cartão.'.format(valProd))
elif formPag == 4:
    print('O valor do produto é {} reais, pagando em 3x ou mais no cartão fica {} reais devido aos juros.'.format(valProd, valProd + valProd * 0.20))
