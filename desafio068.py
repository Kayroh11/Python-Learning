from random import randint

vitorias = 0
escolhaMaq = randint(1, 10)
print('-='*7,'Bem vindo ao jogo do PAR ou ÍMPAR ', '=-'*7)

while True:
    opcao = str(input('Digite se a sua escolha é PAR ou ÍMPAR [P/I]: ')).upper().strip()[0]
    numEscol = int(input('Digite o número escolhido: '))
    resultado = (escolhaMaq + numEscol) % 2

    if opcao == 'P':
        if resultado != 0:
            print(f'Você escolheu PAR e o número {numEscol}. A máquina escolheu {escolhaMaq}. Por isso o resultado '
                  f'foi ÍMPAR... Você perdeu...')
            break
        if resultado == 0:
            print(f'Você escolheu PAR e o número {numEscol}. A máquina escolheu {escolhaMaq}. Por isso o resultado '
                  f'foi PAR. Você venceu!')
            vitorias += 1
    if opcao == 'I':
        if resultado != 0:
            print(f'Você escolheu ÍMPAR e o número {numEscol}. A máquina escolheu {escolhaMaq}. Por isso o resultado '
                  f'foi ÍMPAR. Você venceu!')
            vitorias += 1
        if resultado == 0:
            print(f'Você escolheu ÍMPAR e o número {numEscol}. A máquina escolheu {escolhaMaq}. Por isso o resultado '
                  f'foi PAR... Você perdeu...')
            break

print(f'FIM DE JOGO. Essa foi a sua quantidade de vitórias: {vitorias}')