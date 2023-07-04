valores = list()
menVal = list()
maiVal = list()


for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor pra posição {cont}: ')))
print(f'Você digitou os valores: {valores}')

for c, v in enumerate(valores):
    if v == min(valores):
        menVal.append(c)
    if v == max(valores):
        maiVal.append(c)
print(f"O menor valor digitado foi {min(valores)} nas posições {menVal}, e o maior foi {max(valores)} "
      f"nas posições {maiVal}!")
