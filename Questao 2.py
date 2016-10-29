matriz = [[-7,-3],[4,8],[-1,-6]]

cont_negativos = 0
soma_positivos = 0
cont_impares = 0
cont_pares = 0

for linhas in matriz:
    for numero in linhas:
        if numero < 0:
            cont_negativos = cont_negativos + 1

        else:
            soma_positivos = soma_positivos + numero

        if numero % 2 == 0:
            cont_pares = cont_pares + 1

        else:
            cont_impares = cont_impares + 1

print("Total de números negativos: ", cont_negativos)
print("Soma dos positivos: ", soma_positivos)
print("Total de números pares: ", cont_pares)
print("Total de números impares: ", cont_impares)
