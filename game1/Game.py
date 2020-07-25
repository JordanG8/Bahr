#from Players import real_player_list  Bring back when finished!!
from Players import real_player_list

defenderName = ""
# input of function - string
# output of function - the number of the defender in the players list

def defenderValidation():
    defenderName = input()
    i = 0
    while True:
    
        # Finds the defender's palce in real_player_list
        # + 
        # Makes sure he is in real_player_list
        if defenderName != real_player_list[i].name:
                if i + 1 >= len(real_player_list):
                    print("Please enter a player's name.\n")
                    i = 0
                    defenderName = input()
                    continue
                else:
                    i += 1
                    continue
        else:
            pass

        #Makes sure the defender if alive
        if real_player_list[i].live == False:
            print(real_player_list[i].name + " is already dead. Pick someone else to attack.")
            i = 0
            defenderName = input()
            continue
        else:    
            break
    return i

def attackOnDefender(defenderNum):

       while True:
            from DicesSet import d6_2Set
            roll = d6_2Set()
            print("Roll your dice!\n(press enter)")
            input()
            print("Your roll:" + str(roll))
            attackHP = sum(roll)
            real_player_list[defenderNum].HP -= attackHP
            print("-%s HP to %s. %s now has %s HP" % (attackHP, real_player_list[defenderNum].name, real_player_list[defenderNum].name, real_player_list[defenderNum].HP))
            print("(press enter)")
            input()
            if real_player_list[defenderNum].HP <= 0:
                real_player_list[defenderNum].live = False
                print(real_player_list[defenderNum].name + " is dead!\n")
            break

def attackByTurn():
    n = 0
    while True:
        print("%s's turn\nWho do you want to attack?" % real_player_list[n].name )
        defenderNum = defenderValidation()
        attackOnDefender(defenderNum)

        # Check if someone won.
        w = 0
        c = -1
        while True:
            c += 1
            if c + 1 > len(real_player_list):
                break
            if real_player_list[c].live == False:
                w += 1

        if w + 1 == len(real_player_list):
            while real_player_list[n].live == False:
                n +=1
            print(real_player_list[n].name + " has won!")
            break
            

        # Go to the next player in line.
        # (also regulates n)
        if n + 1 >= len(real_player_list):
            n = 0
        else:
            n += 1

        # Check if the palyer that's next in line is dead.
        # (also regulates n)
        while real_player_list[n].live == False:
            if n + 1 >= len(real_player_list):
                n = 0
            else:
                n += 1
        
