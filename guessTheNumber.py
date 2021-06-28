import random
#
# def guess(x):
#     guess = 0
#     rand_num = random.randint(1, x)
#     while guess != rand_num:
#         guess = int(input(f'Guess a number between 1 and {x}: \n'))
#         if guess < rand_num:
#             print('Sorry! You guessed wrong please try again...(too low)')
#         elif guess > rand_num:
#             print('Sorry! You guessed wrong please try again...(too high)')
#
#     print(f'Whoooaa! you guessed the {rand_num} correctly!')
# guess(20)
x = int(input('choose a number for guessing random number between 1 and yours: '))
def guess(x):
    guess = 0
    rand_num = random.randint(1, x)
    while guess != rand_num:
        guess = int(input(f'Guess a number between 1 and {x}: \n'))
        if guess < rand_num:
            if rand_num - guess > 5:
                print('Sorry! You guessed wrong please try again...(too low)')
            else:
                print('Sorry! You guessed wrong please try again...(youre close guess higher number)')

        elif guess > rand_num:
            if guess - rand_num > 5:
                print('Sorry! You guessed wrong please try again...(too high)')
            else:
                print('Sorry! You guessed wrong please try again...(youre close guess lower number)')

    print(f'Whoooaa! you guessed the {rand_num} correctly!')
guess(x)