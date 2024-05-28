#________________________________________ Tipos de dados ______________________________________________#
# quando colocamos que queremos ver um caractere especifico sempre começa a contagem do 0 ex 0,1,2
# aqui temos o caractere H de Hello impresso 
# pegando a primeira letra da string
# print("Hello"[0])
# pegando a ultima letra da string
# print("Hello"[4])

# tipo de dados em python
# Números:

# int: Inteiro, como 5 ou -3.
# float: Ponto flutuante, como 3.14 ou -0.001.
# complex: Número complexo, como 3 + 2j.
# Booleanos:

# bool: Valor booleano, True ou False.

# Sequências:

# str: String, uma sequência de caracteres, como "Olá, mundo!".
# list: Lista, uma sequência mutável de itens, como [1, 2, 3].
# tuple: Tupla, uma sequência imutável de itens, como (1, 2, 3).
# Conjuntos:

# set: Conjunto, uma coleção não ordenada e sem elementos duplicados, como {1, 2, 3}.
# frozenset: Conjunto imutável, como frozenset({1, 2, 3}).
# Mapeamentos:

# dict: Dicionário, uma coleção de pares chave-valor, como {"chave": "valor"}.
# NoneType:

# None: Tipo especial que representa a ausência de valor.
# Sequências binárias:

# bytes: Sequência imutável de bytes, como b"hello".
# bytearray: Sequência mutável de bytes, como bytearray(b"hello").
# memoryview: Visualização de memória de um objeto, como memoryview(b"hello").
# Tipos de dados adicionais:

# range: Sequência imutável de números, como range(5) ou range(1, 5).
# enumerate: Função que retorna uma tupla contendo um contador e o valor correspondente de uma sequência.
# zip: Função que combina elementos de duas ou mais sequências em tuplas.

# para nao dar erro na hora de somar string com numeros temos alguns exemplos de como fazer isso
# nete exemplo abaixo nos daria um erro porque estamos tentando somar letras com numeros
# numero_de_letras = len(input("qual seu nome"))
# print("seu nome tem: "+numero_de_letras+" letras")

# uma solução e converter quando a funçao len conta ela retorna um número inteiro ai convertemos ela para string
# numero_de_letras = str(len(input("qual seu nome\n")))
# print("seu nome tem: "+numero_de_letras+" letras")

# outra soluçao tambem seria usar uma formatação com f string
# numero_de_letras = len(input("qual seu nome\n"))
# print(f"seu nome tem {numero_de_letras} letras")

# # para conferir o tipo do dado que retorna uma variavel e bem simples podemos usar a função type()
# print(type(numero_de_letras))
# print(type(print))


#colocar o input dentro de uma variável
entrada = input("digite um numero com duas casa ex: 48\n")
# pegar um caractere de uma string e converter para inteiro
primeiro_digito = int(entrada[0])
# pegar um caractere de uma string e converter para inteiro
segundo_digito = int(entrada[1])
# somar e imprimir os dois caracteres convertidos em inteiro
print(primeiro_digito + segundo_digito)
