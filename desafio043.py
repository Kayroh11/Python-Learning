print('-'*8,'Calculadora de IMC', '-'*8)
pesoPessoa = float(input('Digite o seu peso: '))
altPessoa = float(input('Digite sua altura: '))

imc = pesoPessoa / (altPessoa*altPessoa)

if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif imc > 18.5:
    print('Você está no peso ideal.')
