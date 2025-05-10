#################################################


# Dada a lista de palavras:

palavras = ["sol", "lua", "estrela", "planeta"]

# E: Crie uma nova lista que contenha o comprimento
# de cada palavra.

comprimentos = [len(palavra) for palavra in palavras]
print(comprimentos)


#################################################


# Dada a lista de frutas:

frutas = ["maçã", "banana", "uva", "abacaxi", "melão", "Melancia"]

# E: Crie uma nova lista contendo apenas as frutas que
# começam com a letra 'm'.

frutas_m = [fruta for fruta in frutas if fruta.startswith('m') or fruta.startswith('M')]
print(frutas_m)


#################################################


# Dada a lista:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# E: Crie uma nova lista que contenha o quadrado de
# cada número ímpar.

quadrado_impares = [numero ** 2 for numero in numeros if numero % 2 != 0]
print(quadrado_impares)