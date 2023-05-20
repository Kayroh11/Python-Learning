n = int(input('Digite o número pra analisarmos se é primo ou não: '))

if n < 2:
    print('O número {} não é primo. '.format(n))

for i in range (2, int(n**0.5) + 1):
    if n % i == 0:
        print('O número {} não é primo'.format(n))
       break
else:
    print('O número {} é primo.'.format(n))