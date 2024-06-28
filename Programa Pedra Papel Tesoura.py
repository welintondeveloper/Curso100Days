# #Meu Programa
# import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# #Write your code below this line 👇

# maquina = random.randint(0, 2)
# jugador = int(input("Escolha 0 para pedra 1 para papel 2 tesoura"))
# if jugador == 0 and maquina == 2:
#     print(
#         f"você escolheu pedra {rock} a maquina escolheu tesoura {scissors} você ganhou"
#     )

# elif jugador == 1 and maquina == 0:
#     print(
#         f"você escolheu papel {paper} a maquina escolheu pedra {rock} você ganhou"
#     )

# elif jugador == 2 and maquina == 1:
#     print(
#         f"você escolheu{scissors} a maquina escolheu papel {paper} você ganhou"
#     )

# elif jugador == 0 and maquina == 1:
#     print(
#         f"você escolheu pedra {rock} a maquina escolheu papel {paper} você perdeu"
#     )

# elif jugador == 1 and maquina == 2:
#     print(
#         f"você escolheu papel {paper} a maquina escolheu tesoura {scissors} você perdeu"
#     )

# elif jugador == 2 and maquina == 0:
#     print(f"você escolheu tesoura {scissors} a maquina escolheu pedra {rock} você perdeu")

# elif jugador == 0 and maquina == 0:
#     print(f"você escolheu pedra {rock} a maquina escolheu{rock} empate")

# elif jugador == 1 and maquina == 1:
#     print(
#         f"você escolheu papel {paper} a maquina escolheu papel {paper} empate")

# elif jugador == 2 and maquina == 2:
#     print(
#         f"você escolheu tesoura {scissors} a maquina escolheu tesoura {scissors} empate"
#     )

# else:
#     print("você escolheu um numero invalido começe de novo.")

#Meu programa 2 
# import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# computador = random.randint(0, 2)
# escolha_usuario = int(input("escolha 0 para pedra 1 papel ou 2 tesoura"))
# if escolha_usuario == 0:
#     if computador == 2:
#         print("voce ganhou")
#         print(computador)
#     elif computador == 0:
#         print("empate")
#         print(computador)
#     elif computador == 1:
#         print("voce perdeu")
#         print(computador)
# elif escolha_usuario == 1:
#     if computador == 0:
#         print("voce ganhou")
#         print(computador)
#     elif computador == 1:
#         print("empate")
#         print(computador)
#     elif computador == 2:
#         print("voce perdeu")
#         print(computador)
# else:
#     if computador == 2:
#         print("empate")
#         print(computador)
#     elif computador == 0:
#         print("voce perdeu")
#         print(computador)
#     else:
#         print("voce ganhou")
#         print(computador)


#programa do curso
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
user_choice = int(input("what do you chose? type 0 for rock, 1 para paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice <0:
    print("you typed a invalid number, you lose")
else:
    print(game_images[user_choice])
    computer_choice = random.randint(1, 2)
    print(game_images[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print("you win!")
    elif computer_choice == 0 and computer_choice == 2:
        print("you lose!")
    elif computer_choice > user_choice:
        print("you Lose!")
    elif user_choice > computer_choice:
        print("you win!")
    elif computer_choice == user_choice:
        print("empate!")

