import random

numero_Aleatório = random.randint(0,5)

n1 = int(input('Advinhe o número que a máquina informará de 0 - 5: '))

if numero_Aleatório == n1:
    print('Você venceu! O número era {}!'.format(numero_Aleatório))
else:
    print('Infelizmente você perdeu, o número gerado pela máquina era: {}!'.format(numero_Aleatório))