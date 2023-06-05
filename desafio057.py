sexo = input('Digite o sexo (M/F): ').strip().upper()

if sexo == 'M' or sexo == 'F':
    print(f'Sexo {sexo} registrado com sucesso!')
while sexo != 'M' and sexo != 'F':
    sexo = input('Resposta incorreta, por gentileza digite o sexo entre M ou F: ').strip().upper()
    if sexo == 'M' or sexo == 'F':
        print(f'Sexo {sexo} registrado com sucesso!')