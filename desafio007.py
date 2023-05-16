n1 = int(input('\033[1mDigite a primeira nota: '))
n2 = int(input('\033[1mDigite a segunda nota: '))

print('\033[1mA média do aluno foi: {}{}{}'.format('\033[1;32m',(n1+n2)/2,'\033[m'))
