c = 1
while True:
    n = int(input('Digite o número pra ver sua tabuada: '))
    print('-'*40)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
        c += 1
    print('-'*40)
print('Fim do programa, volte sempre!')