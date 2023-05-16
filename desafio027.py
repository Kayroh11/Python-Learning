n1 = str(input('Digite o seu nome completo: ').strip())
n2 = n1.split()
print('O seu primeiro nome é: {}'.format(n2[0]))
print('O seu último nome é: {}'.format(n2[len(n2)-1]))
