from Welcome import welcome
welcome()

print("Let's start by adding players.\n(press enter)")
input()

from Players import addRealPlayers
addRealPlayers()

print("GAME ON\n(press enter)")
input()

from Game import attackByTurn
attackByTurn()

print("(press enter)")
input()
print ("GAME OVER")