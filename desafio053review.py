frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
juntar = ''.join(palavras)
inverso = juntar[::-1]

if juntar == inverso:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo...')
