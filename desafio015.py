km1 = float(input('Digite a quantidade de quilômetros percorridos: '))
ndias = int(input('Digite a quantidade de dias pelos quais o carro foi alugado: '))

print('O preço a pagar pelo carro pelos dias usados é {} reais, pelos km percorridos é {} reais, totalizando {} reais.'.format(ndias*60,km1*0.15,((ndias*60)+km1*0.15)))