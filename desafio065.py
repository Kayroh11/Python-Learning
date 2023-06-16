desejo = 1
soma = qtNums = maior = menor = 0

while desejo == 1:

    n = int(input('Digite um número: '))
    soma += n
    qtNums += 1

    if qtNums == 1:
        menor = n

    if qtNums == 2:
        if n > menor:
            maior = n
        elif n < menor:
            maior = menor
            menor = n

    if qtNums >= 2:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

        q = str(input('Deseja continuar? (S/N): ')).upper().strip()[0] # Aqui o upper deixa em maiúsculo, o strip
                                                                      # retira espaços e o [0] pega só a primeira letra.

        if q == 'N':
            desejo = 0
        elif q == 'S':
            desejo = 1

        else:
            q = str(input('Opção inválida! Digite a opção correta entre S ou N: ').upper())

print('Média de todos os valores: {}. O maior número foi o {}, o menor foi o {}, a quantidade de números foi: {}.'.format(
    (soma / qtNums), maior, menor, qtNums))
