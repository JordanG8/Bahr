def welcome():
    print("Hello players! Welcome to Bahr's Digital Dice Games!\nTo try out your digital dice enter 'roll'\nYou can also pass by entering 'pass'")
    while True:
        inp1 = input()
        if inp1 == "roll":
            from DicesSet import d6_2Set
            print("Great!\nYour roll is:" + str(d6_2Set()))
            break
        elif inp1 == "pass":
            print("Okay")
            break
        else:
            print("Please enter either 'roll' or 'pass'.")