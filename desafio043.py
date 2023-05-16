print('-'*8,'Calculadora de IMC', '-'*8)
pesoPessoa = float(input('Digite o seu peso: '))
altPessoa = float(input('Digite sua altura: '))

imc = pesoPessoa / (altPessoa*altPessoa)

if imc < 18.5:
    print('Seu IMC é: {:.2f} você está abaixo do peso ideal.'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é: {:.2f} Você está no peso ideal.'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é: {:.2f} Você está com sobrepeso.'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é: {:.2f} Você está com obesidade.'.format(imc))
elif imc >= 40:
    print('Seu IMC é: {:.2f} Você está com obesidade mórbida.'.format(imc))
