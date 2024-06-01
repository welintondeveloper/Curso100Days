# outro exemplo que nos dá uma explicação detalhada sobre como podemos até depois do else usar um if 
# mesmo depois de uma condição verdadeira ou falsa você pode colocar outras condições
# então se cair naquela condição terá outras a serem satisfeitas também


temperatura = 12
estacao = "verão2" # aqui temos um erro de propósito para a string não ser igual a verão
# se a estaçao for igual a verão caimos neste if e continuamos verificando se o resto é verdadeiro ou não
if estacao == "verão":
    if temperatura >= 30:
        # se a é verão e a temperatura e maior ou igual a 30 vamos imprimir este print
        
        print("Está muito quente! É melhor vestir roupas leves e beber muita água.")
    else:
        # mais se for verão e a temperatura for abaixo de 30 vamos imprimir isto abaixo
        print("Está quente, mas não é insuportável. Um bom dia para um passeio na praia!")
#se nao for verão caimos neste bloco abaixo
else:
    if temperatura <= 10:
        #caso não seja verão mais a temperatura for menor ou igual a 10 vamos dizer isto abaixo
        print("Está muito frio lá fora! Vista-se em camadas e não esqueça o casaco.")
    else:
        # caso nao for verão e a temperatura for maior do que 10 imprimirá esta frase abaixo
        print("Está frio, mas não é tão ruim. Um bom tempo para desfrutar de uma xícara de chocolate quente!")