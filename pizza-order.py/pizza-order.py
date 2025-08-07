print('Welcome to the Pizza Order System! Please follow the prompts to place your order. \n')

size = input('What size pizza would you like? (S, M, L): ').strip().lower()

pepperoni = input('Would you like pepperoni for extra $2? (yes/no): ').strip().lower()

extra_cheese = input('Would you like extra cheese for extra $1 ? (yes/no): ').strip().lower()

bill = 0

if size == 's':
    bill += 15
    print(f'Small pizza: ${bill}')
    if pepperoni == 'yes':
        bill += 2
    if extra_cheese == 'yes':
        bill += 1

elif size == 'm':
    bill += 20
    print(f'Medium pizza: ${bill}')
    if pepperoni == 'yes':
        bill += 3
    if extra_cheese == 'yes':
        bill += 1

elif size == 'l':
    bill += 25
    print(f'Large pizza: ${bill}')
    if pepperoni == 'yes':
        bill += 3
    if extra_cheese == 'yes':
        bill += 1

print(f'Your total bill is: ${bill}. Thank you for your order!')
print('Have a great day!')

