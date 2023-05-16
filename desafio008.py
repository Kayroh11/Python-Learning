n1 = float(input('\033[1;30mDigite um valor em metros: '))

print('\033[1;30m{}{}{} metros é possui {}{}{} centímetros e {}{}{} milímetros\033[m'.format('\033[1;32m',n1,'\033[m','\033[1;31m',(n1*100),'\033[m','\033[1;34m',(n1*1000),'\033[m'))