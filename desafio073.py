tabelaBrasileirao = ('Botafogo', 'Grêmio', 'Flamengo', 'Chapecoense', 'Fluminense', 'Internacional', 'Bragantino',
                     'Fortaleza', 'Athletico - PR', 'Atlético - MG', 'São Paulo', 'Cruzeiro', 'Santos', 'Bahia',
                     'Corinthians', 'Cuiabá', 'Goias', 'América - MG', 'Vasco da Gama', 'Coritiba')

print(f'Os primeiros cinco colocados são: {tabelaBrasileirao[0:5]}\n')
print('-=-'*20)
print(f'Os últimos quatro colocados são: {tabelaBrasileirao[16:20]}\n')
print('-=-'*20)
print(f'A lista de times em ordem alfabética: {sorted(tabelaBrasileirao)}\n')
print('-=-'*20)
print(f'Chapecoense ficou na posição {tabelaBrasileirao.index("Chapecoense")}')
