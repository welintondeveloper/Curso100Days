# Meu programa com correçao de erro 
# no primeiro segundo grau de imc que estava dando como se fosse abaixo do peso
# Enter your height in meters e.g., 1.55
height = float(input("Qual sua altura"))
# Enter your weight in kilograms e.g., 72
weight = int(input("Qual seu peso"))
# 🚨 Don't change the code above 👆 
#Write your code below this line 👇
AlturaSomada = height*height
Imc = weight/AlturaSomada
IndiceFormatado = round(Imc, 2)
if IndiceFormatado < 18.5:
  print(f"Your BMI is {IndiceFormatado}, you are underweight.")
elif IndiceFormatado <= 25:
  print(f"Your BMI is {IndiceFormatado}, you have a normal weight.")
elif IndiceFormatado <= 30:
  print(f"Your BMI is {IndiceFormatado}, you are slightly overweight.")
elif IndiceFormatado <= 35:
  print(f"Your BMI is {IndiceFormatado}, you are obese.")
elif IndiceFormatado <= 35:
  print(f"Your BMI is {IndiceFormatado}, you are clinically obese.")

#programa do curso

# # Enter your height in meters e.g., 1.55
# height = float(input())
# # Enter your weight in kilograms e.g., 72
# weight = int(input())
# # 🚨 Don't change the code above 👆 
# #Write your code below this line 👇
# Imc = weight / (height * height)
# Imc = round(Imc,15)

# if Imc < 18.5:
#   print(f"Your BMI is {Imc}, you are underweight.")
# elif Imc < 25:
#   print(f"Your BMI is {Imc}, you have a normal weight.")
# elif Imc < 30:
#   print(f"Your BMI is {Imc}, you are slightly overweight.")
# elif Imc < 35:
#   print(f"Your BMI is {Imc}, you are obese.")
# else:
#   print(f"Your BMI is {Imc}, you are clinically obese.")