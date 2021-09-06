from random import randrange

number = randrange(1000)
num = int(number)

choice = ''

while choice != 'exit':
    choice_not_int = input('Guess the number. ')
    choice = int(choice_not_int)
    if choice == num:
        print('You got it!')
        exit()
    elif choice > num:
        print('Lower')
    elif choice < num:
        print('Higher')

