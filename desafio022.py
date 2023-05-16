n1 = str(input("Digite o nome completo: "))
n1_1 = n1.split()

print("Analisando seu nome...")
print("Seu nome em maiúsculo é: {}".format(n1.upper()))
print("Seu nome em minúsculo é: {}".format(n1.lower()))
print("A quantidade de letras do seu nome sem espaços é: {}".format(len(n1.replace(" ", ""))))
print("A quantidade de letras do seu primeiro nome é: {}".format(len(n1_1[0])))

