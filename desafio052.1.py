num = int(input('Digite um número: '))
tot = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(i), end=" ")
print('\033[36m \n O número é divisível \033[m{}\033[36m vezes.'.format(tot))
