def calculate_tip():
    print("Welcome to the Tip Calculator!")

    try:
        total_bill = float(input("Enter the total bill amount: $"))
        tip_percent = float(input("Enter the tip percentage (e.g., 10, 12, or 15): "))
        people_count = int(input("How many people to split the bill? "))

        if people_count <= 0:
            print("Number of people must be greater than zero.")
            return

        tip_amount = total_bill * (tip_percent / 100)
        total_amount = total_bill + tip_amount
        amount_per_person = total_amount / people_count

        print(f"Each person should pay: ${amount_per_person:.2f}")
        return amount_per_person

    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

calculate_tip()