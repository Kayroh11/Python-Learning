
print('Bem vindo :)')
print('-=-'*10)
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
numTermos = int(input('Digite a quantidade de termos que deseja visualizar: '))
cont = 1

while cont <= numTermos:
    print(termo,'->', end=' ')
    termo += razao
    cont += 1

print('FIM')