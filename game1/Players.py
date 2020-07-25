class player_class:
    number = 0
    name = ""
    HP = 10
    live = True
    raceWeapon = ""
    comp = False

real_player_list = []
def addRealPlayers():
    n = 0
    real_player_list.append(player_class())
    print("Enter the first player's name:")
    real_player_list[n].name = input()
    real_player_list[n].number = n
    n += 1
    print("Would you like to add another player? (yes or no)")
    while True:
        inp1 = input()
        if inp1 == "no":
            break
        elif inp1 == "yes":
            real_player_list.append(player_class())
            print("Enter the player's name:")
            real_player_list[n].name = input()
            real_player_list[n].number = n
            n += 1
            print("Would you like to add another player? (yes or no)")
        else:
            print("Please enter yes or no")

#addRealPlayers()

#i = 0
#while i < len(real_player_list):
#    print(real_player_list[i].name)
#    i += 1