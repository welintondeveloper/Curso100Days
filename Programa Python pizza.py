# #########################_________________________Python pizza_______________________####################
# # meu programa
# print("Obrigado por escolher a python pyzza!")
# size = input("Qual tamanho da pizza você vai querer") # What size pizza do you want? S, M, or L
# add_pepperoni = input("Quer adicionar mais calabresa?\n") # Do you want pepperoni? Y or N
# extra_cheese = input("Quer adicionar mais queijo?\n") # Do you want extra cheese? Y or N
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇

# conta = 0
# if size == "p":
#     conta += 15
#     if add_pepperoni == "y":
#         conta += 2
#     if extra_cheese == "y":
#         conta += 1

#     print(f"Your final bill is: ${conta}.")

# elif size == "m":
#     conta += 20
#     if add_pepperoni == "y":
#         conta += 3
#     if extra_cheese == "y":
#         conta += 1

#     print(f"Your final bill is: ${conta}.")

# elif size == "g":
#     conta += 25
#     if add_pepperoni == "y":
#         conta += 3
#     if extra_cheese == "y":
#         conta += 1

#     print(f"Your final bill is: ${conta}.")
# else:
#     print("Por favor insira dados válidos")


####################################____________programa do curso___________#######################################
print("Obrigado por escolher a python pyzza!")
size = input("Qual tamanho da pizza você vai querer") # What size pizza do you want? S, M, or L
add_pepperoni = input("Quer adicionar mais calabresa?\n") # Do you want pepperoni? Y or N
extra_cheese = input("Quer adicionar mais queijo?\n") # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
bill = 0
if size == "s":
    bill += 15
elif size == "m":
    bill +=20
else:
    bill == 25

if add_pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill +=3
if extra_cheese == "y":
    bill += 1

print(f"Your final bill is: ${bill}.")




