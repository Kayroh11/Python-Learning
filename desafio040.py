n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

if (n1+n2)/2 < 5:
    print('A média foi {}, o aluno foi REPROVADO.'.format((n1+n2)/2))
elif (n1+n2)/2 < 6.9 and (n1+n2)/2 > 5:
    print('A média foi {}, o aluno está de RECUPERAÇÃO.'.format((n1+n2)/2))
else:
    print('A média foi {}, o aluno foi APROVADO.'.format((n1+n2)/2))