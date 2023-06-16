numDig = somaNum = qtNum = 0

while True:
    numDig = int(input('Digite um número (Digite 999 pra parar): '))
    if numDig == 999:
        break
    somaNum += numDig
    qtNum += 1
print(f'Você digitou {qtNum} números, a soma entre eles é: {somaNum}')