import datetime

ano1 = int(input('Digite o ano pra análise, coloque 0 pra analisar o ano atual: '))
if ano1 == 0:
    ano1 = datetime.date.today().year
if ano1 % 4 == 0 and ano1 % 100 != 0 or ano1 % 400 == 0:
    print('O ano {} é bissexto.'.format(ano1))
else:
    print('O ano {} não é bissexto.'.format(ano1))
