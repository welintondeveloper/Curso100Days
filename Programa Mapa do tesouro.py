import random
# meu programa
# Cria o mapa (uma grade 3x3 para simplicidade)
mapa = [["🟩", "🟩", "🟩"], ["🟩", "🟩", "🟩"], ["🟩", "🟩", "🟩"]]

# Converte coordenadas (ex: 'a1') para índices de lista
def coordenadas_para_indices(coordenada):
    letras = {'a': 0, 'b': 1, 'c': 2}
    return letras[coordenada[0]], int(coordenada[1]) - 1

# Escolhe uma posição aleatória para o tesouro
tesouro_x = random.randint(0, 2)
tesouro_y = random.randint(0, 2)

# Função para imprimir o mapa
def imprimir_mapa(mapa):
    for linha in mapa:
        print(" ".join(linha))

# O jogo começa aqui
print("Bem-vindo ao jogo da Caça ao Tesouro!")
imprimir_mapa(mapa)

# Solicita uma tentativa do jogador
tentativa = input("Adivinhe onde está o tesouro (ex: a1, b2, c3): ").lower()

# Converte a tentativa em índices de lista
x, y = coordenadas_para_indices(tentativa)

# Verifica se a tentativa está correta
if x == tesouro_x and y == tesouro_y:
    print("Parabéns! Você encontrou o tesouro!")
    mapa[x][y] = "🏆"
else:
    print("Que pena! Tente novamente.")
    mapa[x][y] = "❌"
    mapa[tesouro_x][tesouro_y] = "🏆"

# Imprime o mapa final com o resultado
imprimir_mapa(mapa)
