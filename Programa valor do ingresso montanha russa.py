altura = int(input("digite sua altura em Centimetros\n"))
if altura >= 120:
    print("voce pode andar na montanha russa")
    idade = int(input("Qual sua idade"))
    
    if idade < 13:
        print("o valor é 5 reais")
        valorEntrada = 5
    elif idade < 19:
        print("o valor é 7 reais")
        valorEntrada = 7
    elif idade < 23:
        print("o valor e 12 reais")
        valorEntrada = 12
    else:
        valorEntrada = 12
        print("o valor e 12 reais")
    #vamos colocar mais uma condiçao aqui TirarFoto, no mesmo nível da identação dos ifs elifs
    TirarFoto = input("Quer acrescentar uma foto sao 3 reais a mais y/sim  n/não\n")
    if TirarFoto == "y":
        valorEntrada = valorEntrada + 3
        print(f"o valor da entrada é {valorEntrada} Reais")
    else:
        print(f"o valor da entrada é {valorEntrada} Reais")
else:
    print("você ainda nao tem altura para andar na montanha russa")