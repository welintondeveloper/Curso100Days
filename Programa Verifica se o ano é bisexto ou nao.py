# Meu programa
year = int(input("Qual o ano quer verificar se ele foi/é/será bisexto ou não"))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Ano bisexto")
    else:
      print("Ano não bisexto")
  else:
    print("Ano bisexto")
else:
  print("Ano não bisexto")

# # Programa do Curso
# year = int(input())

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year")
#     else:
#       print("Not leap year")
#   else:
#     print("Leap year")
# else:
#   print("Not leap year")
  