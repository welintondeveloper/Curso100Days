altura = int(input("digite sua altura em Centimetros\n"))
if altura >= 120:
    print("voce pode andar na montanha russa")
    idade = int(input("Qual sua idade"))

    if idade < 13:
        print("o valor é 5 reais")
    elif idade < 19:
        print("o valor é 7 reais")
    elif idade < 23:
        print("o valor e 12 reais")
    else:
        print("o valor e 12 reais")
else:
    print("você ainda nao tem altura para andar na montanha russa")  
