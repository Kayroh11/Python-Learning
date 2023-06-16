primeiroTerm = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão desejada: '))
resultPa = 0
numeroTermos = int(input('Digite quantos termos você quer mostrar: '))

print('{} ->'.format(primeiroTerm), end=' ')
while numeroTermos > 1:
    resultPa += primeiroTerm + razao
    print('{} ->'.format(resultPa), end=' ')
    numeroTermos -= 1
    if numeroTermos == 1:
        print('{}.'.format(resultPa+razao))
        numeroTermos = int(input('\nDigite quantos termos você quer mostrar a mais: '))
