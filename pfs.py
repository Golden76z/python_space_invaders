import random

player_choice = input("Choose Pierre, Feuille, Ciseau to play with : ")

def game():
    Iawin = 0
    playerwin = 0

    Ialist = ["Pierre","Feuille","Ciseau"]
    Ia_choice = random.choice(Ialist)

    if Ia_choice == player_choice:
        print("it's a tie, no points awarded")

    elif player_choice in ["Pierre","pierre","P","p"]:
        if Ia_choice == "Feuille":
            print("Ia chose Feuille and won -_-")
            Iawin += 1
            print("Ia score"+ str(Iawin)+ '\n' + "Your score" + str(playerwin))
            if Ia_choice == "Ciseau":
              print("Ia chose Ciseau and loose :)")
            playerwin += 1
            print("Ia score"+ str(Iawin)+ '\n' + "Your score" + str(playerwin))

    elif player_choice in ["Feuille","Feuille","F","f"]:
        if Ia_choice == "Ciseau":
            print("Ia chose Ciseau and won -_-")
            Iawin += 1
            print("Ia score"+ str(Iawin)+ '\n' + "Your score" + str(playerwin))
            if Ia_choice == "Pierre":
              print("Ia chose Pierre and loose :)")
            playerwin += 1
            print("Ia score"+ str(Iawin)+ '\n' + "Your score" + str(playerwin))

    elif player_choice in ["Ciseau","Ciseau","C","c"]:
        if Ia_choice == "Pierre":
            print("Ia chose Pierre and won -_-")
            Iawin += 1
            print("Ia score"+ str(Iawin)+ '\n' + "Your score" + str(playerwin))
            if Ia_choice == "Feuille":
              print("Ia chose Feuille and loose :)")
            playerwin += 1
            print("Ia score"+ str(Iawin)+ '\n' + "Your score" + str(playerwin))

def replay():
    realreplay = str(input("Would you like to play again? (YES/NO): "))
    if realreplay == "YES" :
        player_choice = input("Choose Pierre, Feuille, Ciseau to play with : ")
    elif realreplay != "YES" :
        exit()

while True:
    game()
    replay()