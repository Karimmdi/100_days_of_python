while True:

    weight = int(input("Enter your weight in kg: "))

    height = float(input("Enter your height in centimeters: "))
    height = height / 100  # Convert height to meters

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        print(f'underweight {bmi:.2f}')
    elif 18.5 <= bmi < 25:
        print('normal weight')

    elif 25 <= bmi < 30:
        print(f'overweight{ bmi:.2f}')

    else:
        print(f'obese ({bmi:.2f})')
    stop = input("Do you want to calculate again? (yes/no): ").strip().lower()
    if stop != 'yes':
        break
print("Thank you for using the BMI calculator!")


