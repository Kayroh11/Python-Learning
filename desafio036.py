import math

valorCasa = float(input('Digite o valor da casa: '))
salPessoa1 = float(input('Digite o seu salário: '))
anosEmp = int(input('Digite em quantos anos você planeja pagar o empréstimo: '))
minimo = salPessoa1 * 0.3
prestacaoMens = valorCasa / (anosEmp * 12)
prestacaoMens = math.ceil(prestacaoMens)

print('O mínimo pro empréstimo aprovado com o seu salário será: {} reais'.format(minimo))
if prestacaoMens < salPessoa1 * 0.30:
    print('Empréstimo negado')
else:
    print('Empréstimo aprovado')
