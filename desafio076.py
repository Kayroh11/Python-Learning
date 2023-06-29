produtos = ('Chocolate', 5,
            'Arroz', 25,
            'Bolacha', 3,
            'Feijão', 20)

print('Produto        |      Valor')
print('_'*30)

for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<21}',end='')
    elif c % 2 != 0:
        print(f'R${produtos[c]:>3}')
