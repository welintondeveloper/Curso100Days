# # meu programa
# import random
# #a função adicionar_nomes usa um input e recebe os nomes
# # e adiciona em nomes_str separados por uma virgula
# def adicionar_nomes():
#     nomes_str = input("Digite todos os nomes separados por vírgulas: ")
#     # colocar os nomes em uma lista remove os espaços e separa por uma virgula cada item para a lista
#     # 1- O método strip() remove quaisquer espaços em branco ao redor de cada nome.
#     # 2- A função split(',') divide a string em uma lista onde cada nome é um elemento da lista.
 
#     nomes = [nome.strip() for nome in nomes_str.split(',')]
#     return nomes# esta função retorna a variavel nomes para uso posterior 

# # A função escolher_pessoa_para_pagar recebe a lista de nomes.
# # Se a lista não estiver vazia, ela usa random.choice para selecionar um nome aleatoriamente.
# # Exibe o nome selecionado.
# # Se a lista estiver vazia, informa que nenhum nome foi adicionado.

# def escolher_pessoa_para_pagar(nomes):
#     if nomes:
#         escolhido = random.choice(nomes)#seleciona um nome aleatório na lista nomes
#         print(f"Hoje, quem vai pagar o jantar é: {escolhido}")
#     else:
#         print("Nenhum nome foi adicionado à lista.")
# # a função main escreve primeiro uma mensagem de boas vindas depois chama as funções
# # adicionar_nomes() e escolher_pessoa_para_pagar()
# def main():
#     print("Bem-vindo ao programa de seleção de quem vai pagar o jantar!")
#     nomes = adicionar_nomes()
#     escolher_pessoa_para_pagar(nomes)

# if __name__ == "__main__":
#     main()
# #programa do curso
