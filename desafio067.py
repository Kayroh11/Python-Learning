contador = 1

while True:
    n = int(input('Digite o número pra ver sua tabuada: '))
    if n > 0:
        while contador <= 10:
            print(f'{n} x {contador} = {n * contador}')
            if contador <= 10:
                contador += 1
        contador = 0
    else:
        break