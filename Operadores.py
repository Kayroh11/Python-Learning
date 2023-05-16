nome = input("Digite o seu nome: ")
print("Prazer em te conhecer, {:-^20}.".format(nome))

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

print ('A soma de {} e {} é: {}'.format(n1,n2,(n1+n2)))
print ('A divisão de {} por {} é: {}'.format(n1,n2,(n1/n2)))
print ('A multiplicação de {} por {} é: {}'.format(n1,n2,(n1*n2)))
print('O resto da divisão de {} por {} é: {}'.format(n1,n2,(n1%n2)))
print('A divisão inteira de {} por {} é: {}'.format(n1,n2,(n1//n2)))
print('{} elevado a {} é: {}'.format(n1,n2,(n1**n2)))