idade = 0
masc = fem = maior = 0

while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).upper().strip()
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        masc += 1
    elif sexo == 'F':
        if idade < 20:
            fem += 1
    else:
        sexo = str(input('Opção incorreta... Digite o sexo da pessoa entre [M/F]: ')).upper().strip()
    opcao = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if opcao == 'N':
        break
    elif opcao not in 'NS':
        opcao = str(input('Opção inválida... Deseja continuar? [S/N]: ')).upper().strip()[0]

print(f'Você cadastrou {maior} pessoas com 18 anos ou mais, {masc} homens, {fem} mulheres com menos de 20 anos. ')
