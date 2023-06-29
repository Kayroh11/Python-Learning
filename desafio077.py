import string

nomes = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
         'MERCADO', 'PROGRAMADOR', 'FUTURO')

for c in nomes:
    print(f'Na palavra {c} temos:', end=' ')
    for letra in c:
        if letra.upper() in 'AEIOU':
            print(letra, end='')
    print('\n')