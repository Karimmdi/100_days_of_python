import random
try:

    while True:
        friends = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
        random_friend = random.choice(friends)

        print(f"Randomly selected friend: {random_friend}")


        # option 2
        #random_index = random.randint(0, len(friends) - 1)
        #print(f"Randomly selected friend by index: {friends[random_index]}")

        if input("Press Enter to continue or type 'exit' to quit: ") == 'exit':
            break
        print("Continuing to select a random friend...")
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")
