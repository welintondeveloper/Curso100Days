# # meu programa
# # Isere o valor total da conta
# print("Bem vindo ao programa Calculador De gorgeta")
# ValorConta = float(input("Qual o valor Total Da Conta?\n"))
# # Insere qual a porcentagem de gorjeta gostaria de dar
# PorcentagemGorgeta = float(input("Qual a porcentagem de Gorgeta Ex: 10, 12, 15\n"))
# # Insere quantas pessoas estão dividindo esta conta
# QuantidadeADividir = float(input("Quantas pessoas vão dividir a conta?\n"))

# calculoGojeta = (ValorConta*PorcentagemGorgeta)/100
# TotalCadaum = (ValorConta+calculoGojeta)/QuantidadeADividir
# print(f"a gojeta vai dar {round(calculoGojeta, 2)} \na quantidade que cada um precisa pagar é {round(TotalCadaum, 2)}")

# programa do curso

# Which number do you want to check?
# number = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
print("Bem vindo ao Calculador de Gorgetas")
bill = float(input("Qual o valor total da conta? $\n"))
tip = int(input("Qual a porcentagem de gojeta gostaria de dar 10, 12, 15? "))
people = int(input("Quantas pessoas vão dividir a conta\n"))
tip_as_percent = tip / 100
total_tip_ammount = bill * tip_as_percent
total_bill = bill + total_tip_ammount
bill_per_person = total_bill / people
final_ammount = round(bill_per_person, 2)
# este código nos daría um erro de formatação então vamos formatar primeiro
# print(f"Cada pessoa pagará: ${final_ammount}")

# aqui abaixo está uma forma de escrever este código mais é um código mais longo
# final_ammount = "{:.2f}".format(bill_per_person)
# print(f"Cada pessoa pagará: $ {final_ammount}")

# esta é a forma mais compacta de formatar um numero sempre com duas casas após o ponto
print(f"Cada pessoa pagará: $ {final_ammount:.2f}")