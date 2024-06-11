import random
# import randomicos
# first_digit = int(10)
# second_digit = int(5)
# score = int(str(first_digit) + str(second_digit))
# print(score)

# numero_inteiro = 42
# numero_string = str(numero_inteiro)
# print(numero_string)  # Isso imprimirá "42"

# palavra = "ExEmPLO"
# palavra_minuscula = palavra.upper()
# print(palavra_minuscula)  # Saída: exemplo
# randomicoss = random.random()
# print(randomicoss)
# print(randomicos)

# lista = ['maçã', 'banana', 'laranja', 'uva']
# fruta_aleatoria = random.choice(lista)
# print(fruta_aleatoria)
# Embaralhar uma lista
#Para embaralhar os elementos de uma lista:
lista = ['maçã', 'banana', 'laranja', 'uva']
random.shuffle(lista)
print(lista)

# Seleciona 2 elementos aleatórios da lista sem reposicao
amostra = random.sample(lista, 2)  
print(amostra)

# Seleciona 2 elementos aleatórios da lista com reposicao
fruta_aleatoria = random.choices(lista,k=2)
print(fruta_aleatoria)

#cria um numero inteiro aleatorio entre 1 e 100
love_score = random.randint(0, 100)
print(f"you love_score is {love_score} ")

numero_uniforme = random.uniform(1.5, 3.5)
print(numero_uniforme)

random.seed(42)
numero_reprodutivel = random.random()
print(numero_reprodutivel)
