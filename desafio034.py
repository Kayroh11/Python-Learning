sala1 = float(input('Digite o salário: '))
sala2 = float

if sala1 > 1250:
    sala2= sala1 + sala1 * 0.10
    print('O salário aumentou para: {}. O aumento foi de: {}.'.format(sala2,sala1*0.10 ))
else:
    sala2 = sala1 + sala1 * 0.15
    print('O salário aumento para: {}. O aumento foi de: {}.'.format(sala2, sala1*0.15))
