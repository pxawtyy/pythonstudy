#################################################


# Dada uma string:

texto = "Exemplo de texto com vogais"

# E: Crie uma nova lista contendo apenas as
# consoantes presentes na string.

texto_sem_vogais = [char for char in texto if char not in ['a', 'e', 'i', 'o', 'u']]
print(texto_sem_vogais)


#################################################


# Dada a lista de tuplas:

lista_tuplas = [(1, 'a'), (2, 'b'), (3, 'a'), (4, 'c')]

# E: Crie uma nova lista contendo apenas o
# primeiro elemento das tuplas onde o segundo
# elemento é igual a 'a'.

# lista_final = [elemento for tupla in lista_tuplas for elemento in tupla if tupla[1] == 'a'] # lógica inicial, mas que resultava: [1, 'a', 3, 'a']
lista_final = [tupla[0] for tupla in lista_tuplas if tupla[1] == 'a']
print(lista_final)


#################################################


# Dada uma lista de listas representando uma
# matriz 2x3:

matriz = [[1, 2, 3], [4, 5, 6]]

# E: Crie uma nova lista de listas que represente
# a "transposta" onde as linhas se tornam colunas
# (neste caso, o resultado seria algo como
# [[1, 4], [2, 5], [3, 6]])

transposta = [
    [
        matriz[i][j] for i in range(len(matriz))
    ] for j in range(len(matriz[0]))
]

print(transposta)


#################################################


# E: Peça ao usuário para inserir um número n.

n = int(input('insira um número: '))

# Dada a lista de palavras:

palavras = ["casa", "carro", "bicicleta", "moto", "patinete"]

# E: Crie uma nova lista contendo apenas as
# palavras que têm mais de n letras.

filtro = [palavra for palavra in palavras if len(palavra) > n]
print(filtro)