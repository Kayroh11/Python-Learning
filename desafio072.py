contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
            'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    numDig = int(input('Digite um número de 0 a 20: '))
    if 0 <= numDig <= 20:
        print(f'Você digitou: {contagem[numDig]}')
        break
    else:
        print('Tente novamente.')