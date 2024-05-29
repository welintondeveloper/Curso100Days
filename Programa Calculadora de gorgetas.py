# Isere o valor total da conta
print("Bem vindo ao programa Calculadora De Gorjetas")
ValorConta = float(input("Qual o valor Total Da Conta?\n"))
# Insere qual a porcentagem de gorjeta gostaria de dar
PorcentagemGorgeta = float(input("Qual a porcentagem de Gorgeta Ex: 10, 12, 15\n"))
# Insere quantas pessoas estão dividindo esta conta
QuantidadeADividir = float(input("Quantas pessoas vão dividir a conta?\n"))

calculoGojeta = (ValorConta*PorcentagemGorgeta)/100
TotalCadaum = (ValorConta+calculoGojeta)/QuantidadeADividir
print(f"a gojeta vai dar {round(calculoGojeta, 2)} \na quantidade que cada um precisa pagar é {round(TotalCadaum, 2)}")