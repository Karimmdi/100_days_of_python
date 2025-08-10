print("Welcome to Treasure Island! Your mission is to find the treasure.")

choice = input("You're at a crossroad. Do you want to go left or right? ").lower()

if choice == "left":
    choice = input('You come to a lake. Do you want to swim across or wait for a boat? (swim/wait) ').lower()
    if choice == "wait":
        choice = input('You arrive at a house with three doors. One red, one yellow, and one blue. Which color do you choose? ').lower()
        if choice == "red":
            print("It's a room full of fire! Game Over.")
            exit()
        elif choice == "yellow":
            print("You found the treasure! You Win!")
            exit()
        elif choice == "blue":
            print("You enter a room of beasts! Game Over.")
            exit()
        else:
            print("You chose a door that doesn't exist! Game Over.")
            exit()

    elif choice == "swim":
        print("You swam across and were eaten by a shark! Game Over.")
        exit()
else:
    print("You fell into a trap! Game Over.")
    exit()

