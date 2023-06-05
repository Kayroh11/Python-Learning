from random import randint

numeroAleatorio = randint(0, 10)
tentativas = 0
palpite = int(input('Advinhe o número que estou pensando entre 0 e 10: '))

while palpite != numeroAleatorio:
    palpite = int(input('Número errado, tente novamente: '))
    tentativas += 1
print('Parabéns, você acertou em {} tentativas, o número era: {}!'.format(tentativas, numeroAleatorio))