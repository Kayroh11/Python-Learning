nome1 = input ('Digite o seu nome: ')
idade1 = int (input ('Digite sua idade: '))
peso1 = float (input ('Digite seu peso: '))
anos = int(input ('Digite o número de anos que você deseja consultar: '))

print ('{}, você possui {} anos, seu peso é {}. Daqui a {} anos você terá {} anos'.format(nome1, idade1, peso1, anos, (idade1 + anos)))