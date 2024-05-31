# Meu programa
year = int(input("Qual o ano quer verificar se ele foi/é/será bissexto ou não"))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Ano bissexto")
    else:
      print("Ano não bissexto")
  else:
    print("Ano bissexto")
else:
  print("Ano não bissexto")

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
  