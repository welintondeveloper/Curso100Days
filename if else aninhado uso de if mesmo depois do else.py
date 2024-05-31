temperatura = 12
estacao = "verão2" # aqui temos um erro de propósito para a string não ser igual a verão

if estacao == "verão":
    if temperatura >= 30:
        print("Está muito quente! É melhor vestir roupas leves e beber muita água.")
    else:
        print("Está quente, mas não é insuportável. Um bom dia para um passeio na praia!")
else:
    if temperatura <= 10:
        print("Está muito frio lá fora! Vista-se em camadas e não esqueça o casaco.")
    else:
        print("Está frio, mas não é tão ruim. Um bom tempo para desfrutar de uma xícara de chocolate quente!")