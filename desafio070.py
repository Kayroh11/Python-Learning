totalGasto = produtosMil = maisBarato = 0
nomeBarato = ' '

while True:
    nomeProd = str(input('Digite o nome do produto: ')).upper()
    valorProd = int(input('Digite o valor do produto em R$ (Apenas números): '))
    totalGasto += valorProd
    if maisBarato == 0:
        maisBarato = valorProd

    if valorProd > 1000:
        produtosMil += 1

    if valorProd < maisBarato:
        maisBarato = valorProd
        nomeBarato = nomeProd
    opcao = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if opcao == 'N':
        break
print(f'Fim do programa. O total gasto foi: {totalGasto}. \n{produtosMil} produtos custam mais de R$ 1000. \n{nomeBarato} '
      f'é o mais barato. ')

