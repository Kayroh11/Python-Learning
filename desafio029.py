vel1 = int(input('Digite a velocidade do carro em KM/h: '))

if vel1 > 80:
    multa = (vel1 - 80)*7
    print('Você foi multado! O valor da multa é: {} reais'.format(multa))
else:
    print('Você está dentro do limite de 80KM/h, pois sua velocidade foi: {}KM/h'.format(vel1))
