# Meu programa
print("The Love Calculator is calculating your score...")
name1 = "Brad Pitt" # What is your name?
name2 = "Jennifer Aniston" # What is their name?
# para converter todas as letras do nome para minúscula vamos usar a função lower()
nome1Convertido = name1.lower()
nome2Convertido = name2.lower()
# Juntando os nomes e colocando um E maiusculo no meio fica assim "fulano E fulana"
# Como o E nao foi na função lower() então ele não será contado pela função count()
nomesJuntos = nome1Convertido+" E "+nome2Convertido
ScoreTRUE = 0
contador = nomesJuntos.count("t")
ScoreTRUE += contador
contador = nomesJuntos.count("r")
ScoreTRUE += contador
contador = nomesJuntos.count("u")
ScoreTRUE += contador
contador = nomesJuntos.count("e")
ScoreTRUE += contador
#print(f"As letras da palavra TRUE aparecem {score1} vezes na palavra '{nomes}'.")
Resultado = ScoreTRUE * 10
#______________________________________________________________________________

ScoreLove = 0
contador = nomesJuntos.count("l")
ScoreLove += contador
contador = nomesJuntos.count("o")
ScoreLove += contador
contador = nomesJuntos.count("v")
ScoreLove += contador
contador = nomesJuntos.count("e")
ScoreLove += contador
total = Resultado + ScoreLove
#print(f"As letras da palavra TRUE LOVE aparecem {score} vezes na palavra '{nomes}'.")
if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
#______________________________________________________________________________________________________
#Programa do curso
print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# Your code below this line 👇
combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")