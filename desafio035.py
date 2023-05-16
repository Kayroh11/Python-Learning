comp1 = int(input('Digite o comprimento da primeira reta: '))
comp2 = int(input('Digite o comprimento da segunda reta: '))
comp3 = int(input('Digite o comprimento da terceira reta: '))

if comp1 + comp2 > comp3 and comp2 + comp3 > comp1 and comp3 + comp1 > comp2:
    print('É possível formar um triângulo com as medidas informadas!')
else:

    print('Não é possível formar um triângulo com as medidas informadas...')