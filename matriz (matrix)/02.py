#################################################


# E: Crie duas matrizes 2x2, matriz_a e matriz_b,
# com valores de sua escolha. Escreva um código que calcule
# e imprima a matriz resultante da soma dessas duas matrizes.

matriz_a = [
    [1, 2],
    [3, 4]
]
matriz_b = [
    [5, 6],
    [7, 8]
]
matriz_c = [
    [
        matriz_a[i][j] + matriz_b[i][j] for i in range(len(matriz_a))
    ] for j in range(len(matriz_a[0]))
]

print(matriz_c)


#################################################