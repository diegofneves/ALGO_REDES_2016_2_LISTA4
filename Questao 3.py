maior = 0

salarios = [

    [float(input("Digite seu salário: ")), float(input("Digite seu salário: ")), float(input("Digite seu salário: "))],
    [float(input("Digite seu salário: ")), float(input("Digite seu salário: ")), float(input("Digite seu salário: "))],
    [float(input("Digite seu salário: ")), float(input("Digite seu salário: ")), float(input("Digite seu salário: "))]

        ]

menor = salarios[0][0]

for linha in salarios:
    for salario in linha:

        if salario > maior:
            maior = salario

        elif salario < menor:
            menor = salario

print("Maior salário: ", maior)
print("Menor salário: ", menor)
