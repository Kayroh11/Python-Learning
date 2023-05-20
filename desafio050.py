somaPar = 0
for soliRepet in range(1, 7):
    numDig = int(input('Digite o {}° número: '.format(soliRepet)))
    if numDig % 2 == 0:
        somaPar += numDig
print('A soma dos números pares é: {}'.format(somaPar))