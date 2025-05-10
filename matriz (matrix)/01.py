#################################################


# E: Elabore uma matriz 2x2 e atribua os valores
# 1 e 2 à primeira linha, e 3 e 4 à segunda linha, respectivamente.

matriz = [
    [1, 2],
    [3, 4]
]

# E: Recupere e imprima o valor que se encontra
# na segunda linha e na primeira coluna.

print(matriz[1][0])

# E: Altere o elemento localizado na primeira linha
# e na segunda coluna para o valor 5.
# Em seguida, imprima a matriz após a modificação.

matriz[0][1] = 5
print(matriz[0][1])


#################################################


matriz_base = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# E: Desenvolva um código para imprimir cada elemento
# da segunda coluna desta matriz, um abaixo do outro.

for elemento in matriz_base[1]:
    print(elemento)

# E: Calcule e imprima a soma de todos os elementos
# presentes na primeira linha.

print(sum(matriz_base[0]))