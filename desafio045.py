import random

print("""Escolha entre: 
1 - Pedra
2 - Papel
3 - Tesoura""")
escolha1 = int(input('Digite o número do escolhido: '))
escolhaMaq = random.randint(1, 3)

if escolha1 == escolhaMaq:
    print('Você escolheu {} e a máquina {}, por isso você empatou com a máquina!'.format(escolha1, escolhaMaq))
elif escolha1 == 1 and escolhaMaq == 2:
    print('Você escolheu {} e a máquina {}, por isso a máquina ganhou.'.format(escolha1, escolhaMaq))
elif escolha1 == 1 and escolhaMaq == 3:
    print('Você escolheu {} e a máquina {}, por isso você ganhou!'.format(escolha1, escolhaMaq))
elif escolha1 == 2 and escolhaMaq == 1:
    print('Você escolheu {} e a máquina {}, por isso você ganhou!'.format(escolha1, escolhaMaq))
elif escolha1 == 2 and escolhaMaq == 2:
    print('Você escolheu {} e a máquina {}, por isso você empatou com a máquina!'.format(escolha1, escolhaMaq))
elif escolha1 == 2 and escolhaMaq == 3:
    print('Você escolheu {} e a máquina {}, por isso a máquina ganhou.'.format(escolha1, escolhaMaq))
elif escolha1 == 3 and escolhaMaq == 1:
    print('Você escolheu {} e a máquina {}, por isso a máquina ganhou.'.format(escolha1, escolhaMaq))
elif escolha1 == 3 and escolhaMaq == 2:
    print('Você escolheu {} e a máquina {}, por isso você ganhou!'.format(escolha11, escolhaMaq))
elif escolha1 == 3 and escolhaMaq == 3:
    print('Você escolheu {} e a máquina {}, por isso você empatou com a máquina!'.format(escolha1, escolhaMaq))