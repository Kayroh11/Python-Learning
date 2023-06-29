from random import randint

randNumb = (randint(0, 100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))
print(f'Esses foram os números gerados: {randNumb}')
print(f"O menor é {sorted(randNumb)[0]}", f"o maior é {sorted(randNumb)[4]}")

