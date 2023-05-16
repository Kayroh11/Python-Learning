print('=-='*5,'Alistamento militar','=-='*5)

anoNasc = int(input('Digite o ano do seu nascimento: '))

if (2023 - anoNasc) < 18:
    print('Ainda falta/faltam {} ano(s) pra você se alistar'.format(18 - (2023 - anoNasc)))
elif (2023 - anoNasc)  == 18:
    print('Você deve se alistar nesse ano!')
else:
    print('Já passou/passaram {} ano/anos pra você se alistar, vá atrás do serviço militar mais próximo o mais breve possível.'.format((2023 - anoNasc) - 18))
