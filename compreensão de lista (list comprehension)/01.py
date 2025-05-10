#################################################


# Dada a lista:

numeros = [5, 10, 15, 20]

# E: Crie uma nova lista que contenha o dobro
# de cada número da lista original.

dobro = [numero * 2 for numero in numeros]
print(dobro)


#################################################


# Dada a lista de nomes:

nomes = ["ana", "maria", "joão", "pedro"]

# E: Crie uma nova lista com todos os nomes em
# letras maiúsculas.

nomes_maiusculos = [nome.upper() for nome in nomes]
print(nomes_maiusculos)


#################################################


# Dada a lista:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# E: Crie uma nova lista que contenha apenas os
# números pares.

pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)