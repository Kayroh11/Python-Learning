n1 = str(input('Digite uma frase: ').strip())

print("A letra A aparece {} vezes.".format(n1.upper().count('A')))
print("Aparece a primeira vez no caractere {}".format(n1.upper().find("A") + 1))
print("A última no caractere {}".format(n1.upper().rfind("A") + 1))
