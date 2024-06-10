
print("Bem vindo a ilha do tesouro.")
print("Sua missão é encontrar o tesouso.")

# Primeira rodada
escolha = input('você encontra dois caminha o que quer fazer?\n "d" direita ou "e" esquerda\n')
escolha = escolha.lower()#Convertendo os dados da variável escolha para minúscula
if escolha == "d":
    print("agora você encontrou um lago o que deseja fazer")

    # Segunda rodada
    escolha = input(' "n" nadar ou "e" esperar o barco\n')
    escolha = escolha.lower()#Convertendo os dados da variável escolha para minúscula
    if escolha == "e":
        print("certo você continua sua jornada encontrou uma casa com três portas o que deseja fazer.")

        # Terceira rodada
        #\ também serve para indicar que não se trata de um código e sim de um símbolo como string também
        escolha = input('escolhe qual porta \'a\' azul "v" vermelha "m" marrom\n')
        escolha = escolha.lower()#Convertendo os dados da variável escolha para minúscula
        if escolha == "a":
            print("parabéns você encontrou o tesouro e agora é rico!")
            print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
        else:#fechamento última rodada
            print("Você escolheu a porta errada e foi morto por um palhaço assasino. Fim de jogo!")
    else:#fechamento segunda rodada
        print("você foi comido por um jacaré. Fim de jogo!")
else:#fechamento primeira rodada
    print("Escolha errada um urso pardo rasgou suas entranhas na estrada. Fim de jogo!")

#programa do curso

# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
# choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".\n').lower()

# if choice1 == "left":
#     choice2 = input('you\'ve come to a lake. there is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
#     if choice2 == "wait":
#         choice3 = input("you arrive at the island unharmed. There is a house with 3 dors. One read , One yellow and one blue. which colour do you choose?\n").lower()
#         if choice3 == "red":
#             print("It's a room full of fire. Game Over.")
#         elif choice3 == "yellow":
#             print("you found the treasure! You Win!")
#             print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
#         elif choice3 == "blue":
#             print("you enter a room of beasts. Game Over")
#         else: 
#             print("you choose a dor that doensn't exist. Game Over.")   
#     else:
#         print("you got attacke by an anngry trout. Game Over.")    
# else:
#     print("You fell into a hole. Game Over")



