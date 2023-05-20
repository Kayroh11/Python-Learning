maioridade = 0
menoridade = 0

for i in range(1,8):
    anoNasc = int(input('Digite o ano de nascimento da {}° pessoa: '.format(i)))
    if (2023 - anoNasc) < 18:
        menoridade += 1
    elif (2023 - anoNasc) >= 18:
        maioridade += 1

print('{} pessoas ainda não atingiram a maioridade, {} pessoas já atingiram.'.format(menoridade,maioridade))