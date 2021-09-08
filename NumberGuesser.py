from random import randrange

choice = ''
num = randrange(1000)

while choice != 'q':
    try:
        choice = input('Enter a number: ')
    
        if int(choice) == num:
            print('You got it!')
            break
        if int(choice) > num:
            print('Lower')
        if int(choice) < num:
            print('Higher')
    except ValueError:
        print('Please enter a valid number.')