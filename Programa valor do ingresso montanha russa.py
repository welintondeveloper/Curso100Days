altura = int(input("digite sua altura em Centimetros\n"))
if altura >= 120:
    print("você pode andar na montanha russa")
    idade = int(input("Qual sua idade\n"))
    
    if idade < 13:
        print("o valor é 5 reais")
        valorEntrada = 5
# se a entrada de idade fosse 7 anos, e abaixo tivesse um outro if ao inves de elif 
# não daria erro mais iria imprimir os dois valores 5 reis e 7 reais pois ele iria ser < 19 e < 13
    elif idade < 19:
        print("o valor é 7 reais")
        valorEntrada = 7
    # se quisermos cobrir uma idade podemos dizer se apenas acima de 44 pra incluir apenas do 45 en diante
    # no caso do 55 podemos colocar um >=  para pegar apenas aquela abaixo de 55 ou igual a 55 56 já não inclui
    elif idade > 44 and idade <= 55 :
        valorEntrada = 0
        print("Que legal você tem um desconto especial sua entrada será gratuita")
    else:
        valorEntrada = 12
        print("o valor é 12 reais")
    #vamos colocar mais uma condiçao aqui TirarFoto, no mesmo nível da identação dos ifs elifs
    TirarFoto = input("Quer acrescentar uma foto são 3 reais a mais y/sim  n/não\n")
    if TirarFoto == "y":
        # é mais facil entender desta forma más poderia ser abreviado este calculo abaixo 
        # ao invés de ValorEntrada = ValorEntrada +3 também funcionaria se fosse simplesmente ValorEntrada += 3 
        valorEntrada = valorEntrada + 3
    print(f"valor total da entrada {valorEntrada} Reais")# aqui está o segredo a identação um tab cria a identação
    if idade > 44 and idade < 56:
        print("por você estar na meia idade você tem entrada gratuita")
#___________________________________________________________________________________________________________
# este código comentado abaixo funcionaria mais podemos abreviar usar a identação para dizer ao programa
# que só se caso a pessoa escolher que vai querer a foto vamos acrescentar os 3 reais
# basta apenas colocar um print acima com a identaçao no mesmo lugar que o if que o compilador entende
#------------------------------------------------------------------------------------------------------------

    # else:
    #     print(f"o valor da entrada é {valorEntrada} Reais")
else:
    print("você ainda não tem altura para andar na montanha russa")