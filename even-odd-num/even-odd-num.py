#Even or Odd number
while True:

    num = int(input('Enter a number: '))

    if num % 2 == 0:
        print(f'{num} is an even number.')
    else:
        print(f'{num} is an odd number.')
    stop = input('Do you want to continue? (y/n): ')
    if stop.lower() != 'y':
        print('Exiting the program.')
        break
    #End of program


