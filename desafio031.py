dist1 = float(input('Digite a distância da viagem em KM: '))

if dist1 <= 200:
    print('O preço da passagem será: {}'.format(dist1*0.5))
else:
    print('O preço da passagem será: {}'.format(dist1*0.45))