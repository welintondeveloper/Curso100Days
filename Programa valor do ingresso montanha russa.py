altura = int(input("digite sua altura em Centimetros\n"))
if altura >= 120:
    print("voce pode andar na montanha russa")
    idade = int(input("Qual sua idade\n"))
    
    if idade < 13:
        print("o valor é 5 reais")
        valorEntrada = 5
    elif idade < 19:
        print("o valor é 7 reais")
        valorEntrada = 7
    else:
        valorEntrada = 12
        print("o valor e 12 reais")
    #vamos colocar mais uma condiçao aqui TirarFoto, no mesmo nível da identação dos ifs elifs
    TirarFoto = input("Quer acrescentar uma foto sao 3 reais a mais y/sim  n/não\n")
    if TirarFoto == "y":
        # é mais facil entender desta forma más poderia ser abreviado este calculo abaixo 
        # ao invés de ValorEntrada = ValorEntrada +3 também funcionaria se fosse simplesmente ValorEntrada += 3 
        valorEntrada = valorEntrada + 3
    print(f"valor total da entrada {valorEntrada}")# aqui está o segredo a identação um tab cria a identação
#___________________________________________________________________________________________________________
# este código comentado abaixo funcionaria mais podemos abreviar usar a identação para dizer ao programa
# que so se caso a pessoa escolher que vai querer a foto vamos acrescentar os 3 reais
# basta apenas colocar um print acima com a identaçao no mesmo lugar que o if que o compilador entende
#------------------------------------------------------------------------------------------------------------

    # else:
    #     print(f"o valor da entrada é {valorEntrada} Reais")
else:
    print("você ainda não tem altura para andar na montanha russa")