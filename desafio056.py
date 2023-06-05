"""Programa que leia nome idade e sexo de 4 pessoas, diga a média de idade, nome do homem mais velho e quantas mulheres
têm menos de 20 anos"""


somaIdade = 0 #Variável que soma a idade pra fazer a média solicitada na atividade
homemmaisVelho = '' #Variável string pra acomodar o nome do homem mais velho
idadehomemVelho = 0 #Variável pra acomodar a idade do homem mais velho pra que o nome dele seja emitido
mulheresmenos20 = 0 #Variável pra somar a quantidade de mulheres menores que 20 anos

for i in range (4): #Loop de 0 a 3 (4 repetições) pra obter os dados de 4 pessoas
    print('Pessoa {}: '.format(i+1)) #i+1 pois o primeiro i é 0, somamos 1 pra simbolizar a primeira até quarta pessoa
    nome = (str(input('Digite o nome da pessoa: ')))
    idade = (int(input('Digite a idade da pessoa: ')))
    sexo = (str(input('Digite o sexo da pessoa (H/M): ').upper())) #Aqui usei o Upper pra não ter erro na obtenção do sexo
    somaIdade += idade
    if sexo == "H" and idade > idadehomemVelho:
        idadehomemVelho = idade
        homemmaisVelho = nome
    if sexo == "M" and idade < 20:
        mulheresmenos20 += 1

print('Média da idade: {:.2f}, nome do homem mais velho: {}, {} mulher(es) possui(em) menos de 20 anos.'.format(somaIdade / 4, homemmaisVelho, mulheresmenos20))

