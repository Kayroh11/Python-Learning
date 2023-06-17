nota50 = 50
nota20 = 20
nota10 = 10
nota1 = 1
qnotas50 = qnotas20 = qnotas10 = qnotas1 = 0
resto = 0

while True:
    valorSaq = int(input('Digite em números o valor a ser sacado: '))
    if valorSaq >= 50:
        qnotas50 = int(valorSaq / nota50)
        resto = valorSaq % nota50
        qnotas20 = int(resto / nota20)
        resto = resto % nota20
        qnotas10 = int(resto / nota10)
        resto = resto % nota10
        qnotas1 = int(resto / nota1)

    elif 50 > valorSaq >= 20:
        qnotas20 = int(valorSaq / nota20)
        resto = valorSaq % nota20
        qnotas10 = int(resto / nota10)
        resto = resto % nota10
        qnotas1 = int(resto / nota1)

    elif 20 > valorSaq >= 10:
        qnotas10 = int(valorSaq / nota10)
        resto = valorSaq % nota10
        qnotas1 = int(resto / nota1)

    elif valorSaq < 10:
        qnotas1 = int(valorSaq / nota1)

    break

print(f'Você receberá {qnotas50} notas de 50 reais. {qnotas20} notas de 20 reais. {qnotas10} notas de 10 reais e '
      f'{qnotas1} notas de 1 real.')
