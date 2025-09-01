date = input("Enter a date (YYYY-MM-DD): ")
mood = input("Enter your mood for the day 1 - 10: ")
thoughts = input("Enter what you've learned today: ")


with open(f"journal/{date}.txt", "w") as file:
    file.write(f"Mood: {mood}" + "\n" *2)
    file.write(f"Thoughts: {thoughts}\n")


print(f"Journal entry for {date} saved.")
# Simple Journal Entry Application
